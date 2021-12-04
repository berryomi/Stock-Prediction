import pandas as pd
import numpy as np
import os
import requests as rq
import pandas_datareader as web
from datetime import date
import time
from tqdm import tqdm

'''
description : Get ticker from NASDAQ and then ticker cleansing (Get rid of SPAC, Preferred Shares, ETF, Fund) 
then Sort ticker by ascending order 
Parameter: N/A
Return value: N/A
'''
def get_ticker():
    url = 'https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&offset=0&download=true'
    headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}

    data = rq.get(url, headers=headers)
    data_json = data.json()['data']
    all_data = pd.DataFrame(data = data_json['rows'], columns = data_json['headers'])
    all_data = all_data.loc[~all_data.symbol.duplicated(keep = 'first'), :]


    all_data['marketCap'] = pd.to_numeric(all_data['marketCap']) 
    all_data = all_data.loc[all_data['marketCap'] != 0]
    all_data = all_data.loc[~all_data['symbol'].str.contains('\\^')]
    all_data = all_data.loc[~all_data['name'].str.contains('Preferred')]
    all_data = all_data.loc[~all_data['name'].str.contains('preferred')]
    all_data = all_data.loc[~all_data['name'].str.contains('ETF')]
    all_data = all_data.loc[~all_data['name'].str.contains('Fund')]
    all_data = all_data.loc[~all_data['name'].str.contains('%')]
    all_data['symbol'] = all_data['symbol'].str.replace('\\/', '-')
    all_data = all_data.sort_values(by = 'symbol')
    all_data = all_data.reset_index(drop=True)

    all_data.to_csv("data/US_ticker.csv")
    print("Complete for getting ticker from NASDAQ and save it to CSV")

'''
description : Get stock data 
Parameter: N/A
Return value: N/A
'''

def get_Stock_data():
    US_ticker = pd.read_csv('data/US_ticker.csv', index_col=0)
    error_list = []
    
    if not os.path.exists("data/US_price"):
        os.makedirs("data/US_price")
    
    for ticker in tqdm(range(0, len(US_ticker))):
        
        price = pd.DataFrame({"Price" : [np.nan]})
        price.index = [date.today().strftime("%Y-%m-%d")]
        
        name = US_ticker["symbol"][ticker]
        
        try:
            price = web.DataReader(name, "yahoo")
        except Exception as e:
            print(e)
            error_list.append(name)
        
        price.to_csv('data/US_price/'+name+'_price.csv')
        time.sleep(2)  
        
if __name__ == '__main__':
    get_Stock_data()