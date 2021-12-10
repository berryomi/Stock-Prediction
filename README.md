## Stock Market Price Prediction
 - Stock market prices are predicted by using Machine Learning Regression Models and Deep Learning Model.
    - Machine Learning Regression Models:
         - Linear Regression Model
         - K-nearest Neighbour (KNN) Regression Model
         - Random Forest Regression Model
    - Deep Learning Model:
         - Long Short-Term Memory (LSTM) Model   
 - The data used are gathered from our crawler program (crawler.py)
    - Stock price indices used are:
        - Nasdaq (IXIC)
        - Nikkei (N225)
    - Data pre-processing includes:
        - Data Cleaning
        - Noise Filtering (Short/Long Rolling Mean)

## Contributors:
 - Jiwon Jun
 - Kai Kim
 - Jieung Park

## Required Libraries:
 - 

## Execution Process:
 - Run Traiding.ipynb (Jupyter file)
 - Order of Execution and Expected Results:
     1. Importing Modules
     2. Gathering Data & Data Cleaning -> Produce raw data graph
     3. Noise Filtering -> Produce noise filtering methods comparison graph
     4. Linear Regression Short Rolling Mean -> Produce linear regression prediction graph (short rolling mean)
     5. Linear Regression Long Rolling Mean -> Produce linear regression prediction graph (long rolling mean)
     6. KNN Regression Short Rolling Mean -> Produce KNN regression prediction graph (short rolling mean)
     7. KNN Regression Long Rolling Mean -> Produce KNN regression prediction graph (long rolling mean)
     8. Random Forest Regression Best-fit Paramters -> Prints the best-fit paramters (n_estimators, min_samples_leafs, max_depth)
     9. Random Forest Regression Short Rolling Mean -> Produce Random Forest regression prediction graph (short rolling mean)
     10. Random Forest Regression Long Rolling Mean -> Produce Random Forest regression prediction graph (long rolling mean)
     11. Machine Learning Regression Models Validation Score -> Prints the validation score of each machine learning Models
     12. Data Descriptive Statistics -> Prints the raw data and machine learning model's descriptive Statistics
     13. Deep Learning Data Pre-processing & LSTM epoch run -> Produce LSTM prediction graph
     14. LSTM Loss Calculation -> Produce LSTM training loss and validation loss graph

