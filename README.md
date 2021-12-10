## Topic: *Stock prediction using machine learning and Deep learning models*
 - Stock
 - 옵션: Predicting Stock Market
    - Brief Summary: Predicting Stock Market
        - Getting Data: collect data from FinanceDataReader module and yahoo finance from our customized crawler
        - Possible Questions: 
            - Can we predict the future stock price movement based on the previous price data?
            - Can we use the predicted future stock data to either buy or sell stocks in the future?
        - How it relates to CMPT 353: 
            - Inlcudes: Noise/outlier filtering - cleaning data, Defining problem, and analyzing stock market 
================================================================================
## Models
 - Stock market prices are predicted by using Machine Learning Regression Models and Deep Learning Model.
    - Machine Learning Regression Models:
         - Linear Regression Model
         - K-nearest Neighbour (KNN) Regression Model
         - Random Forest Regression Model
    - Deep Learning Model:
         - Long Short-Term Memory (LSTM) Model   

=================================================================================
## Steps

 - The data used are gathered from our crawler program (crawler.py)
    - Stock price indices used are:
        - Nasdaq (IXIC)
        - Nikkei (N225)
    - Data pre-processing includes:
        - Data Cleaning
        - Noise Filtering (Short/Long Rolling Mean)
        - Data Normalization -> MinMaxscaler
    - Build and Train Models (Machine Learning)
        - Linear Regression - Short Rolling
        - Linear Regression - Long Rolling
        - K-nearest Neighbour Regression - Short Rolling
        - K-nearest Neighbour Regression - Long Rolling
        - Random Forest Regression - Best Parameters
            - Random Forest Regression - Short Rolling
            - Random Forest Regression - Long Rolling
    - Machine Learning Models Failure Analysis
    - Build and Train Models (Deep Learning)
        - Epoch 20
        - Epoch 100
    - Model Prediction and Visaulizing the Results
    - Model Analysis 
        - RMSE compare analysis
        - Validation loss and training loss by epochs
    - Ininital model with single hidden layer with LSTM model (For model testing)
        
==============================================================================================================

## Contributors:
 - Jiwon Jun (301335374), SFU SoSy
 - Jieung Park (301330362), SFU Comp Sci
 - Youngseong Kim (301283396), SFU Comp Sci
 

## Required Libraries:
 - pip install Keras
 - pip install --upgrade tensorflow
 - pip install -U finance-datareader
 - pip install tensorflow-gpu #for usage of GPU
 - pip install keras-gpu #for usage of GPU
 - pip install matplotlib
 - pip install -U scikit-learn
 - pip install -U statsmodels
 - pip install -U pandas
 - pip install -U numpy

## Execution Process:
 - Run Trading.ipynb (Jupyter file)
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

<<<<<<< HEAD
## Project Experience Summary
 - Must be included by each member (in addition to the 6 pages report)
 - Overview of the project (like a resume)
      - Focus on: skills, education, experience, knowledge as accomplishments (rather than duties and tasks)
 - Individual contributions
   

 
## Grading:
 - Acquiring/Cleaning data
 - Defining/refining the problem
 - Data analysis
 - How you well-explain the whole thing
=======
>>>>>>> 87bef5570103f21a98f56406ea0a065c650263b2
