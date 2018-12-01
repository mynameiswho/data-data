
import pandas as pd
from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm

#Inspired by
#https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/

#Removes trend and seasonality using decomposition
def make_stationary(timeseries):
    decomposition = sm.tsa.seasonal_decompose(timeseries, model='additive')
    timeseries = decomposition.resid

    return(timeseries)

#Returns p-value of augmented Dickey-Fuller unit root test
def check_stationary(timeseries, variable):
    timeseries = timeseries.dropna()
    dftest2 = adfuller(timeseries[variable].values)[1]

    return dftest2

#TESTCODE

#Loading and preproccesing data
#Dataset: https://www.quandl.com/api/v3/datasets/FRED/M04108GBM318NNBR.csv

df = pd.read_csv("FRED-M04108GBM318NNBR.csv")
df['DATE'] = pd.to_datetime(df['DATE'])
df = df.set_index('DATE')
df = df.sort_values('DATE')

#Initial plot
print("Initial p-value: ", check_stationary(df,'VALUE'))
df = make_stationary(df)
print("After making stationary:", check_stationary(df,'VALUE'))
