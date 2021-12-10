<<<<<<< HEAD
## Topic:
 - Stock
 - 옵션: Predicting Stock Market
    - Brief Summary: Predicting Stock Market
        - Getting Data: collect data from online (where and how)
        - Possible Questions: ?????? 
        - How it relates to CMPT 353: 
            - Inlcudes: Noise/outlier filtering - cleaning data, Defining problem, and analyzing stock market 
=======
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
>>>>>>> 87bef5570103f21a98f56406ea0a065c650263b2

## Contributors:
 - JIWON JUN
 - YOUNGSEONG Kim
 - JIEUNG PARK
 

## Required Libraries:
 - Install by using pip3 install **module_name** or installation method that fits your device
 - pandas
 - numpy
 - matplotlib
 - scikit-learn
 - statsmodels
 - tensorflow
 - keras

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
   
## Requirement
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
 
## Grading:
 - Acquiring/Cleaning data
 - Defining/refining the problem
 - Data analysis
 - How you well-explain the whole thing
=======
>>>>>>> 87bef5570103f21a98f56406ea0a065c650263b2
