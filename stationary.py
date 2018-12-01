
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import adfuller

#Inspired by
#https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/

def RollingMeanStdPlot(timeseries, period):
    rollmean = df.rolling(period).mean()
    rollstd = df.rolling(period).std()

    plt.plot(timeseries, label = 'Original')
    plt.plot(rollmean, label = 'Rolling mean')
    plt.plot(rollstd, label = 'Rolling std')
    plt.legend()
    plt.show()

#Removes trend and seasonality using decomposition
def make_stationary(timeseries):
    decomposition = sm.tsa.seasonal_decompose(timeseries, model='additive')
    timeseries = decomposition.resid

    return(timeseries)

#Returns p-value of augmented Dickey-Fuller unit root test
def check_stationary(timeseries, variable):
    timeseries = timeseries.dropna()
    dftest = adfuller(timeseries[variable].values)[1]

    return dftest

#TESTCODE

#Loading and preproccesing data
#Dataset: https://www.quandl.com/api/v3/datasets/FRED/M04108GBM318NNBR.csv

df = pd.read_csv("FRED-M04108GBM318NNBR.csv")
df['DATE'] = pd.to_datetime(df['DATE'])
df = df.set_index('DATE')
df = df.sort_values('DATE')

#Initial plot
print("Initial p-value: ", check_stationary(df,'VALUE'))
RollingMeanStdPlot(df, 12)

df = make_stationary(df)
print("After making stationary:", check_stationary(df,'VALUE'))
RollingMeanStdPlot(df, 12)
