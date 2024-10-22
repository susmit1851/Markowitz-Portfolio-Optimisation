import os
import pandas as pd
import numpy as np

df=pd.DataFrame()
var_df=pd.DataFrame()
variances=[]
for j in range(len(os.listdir('data'))):
    files=os.listdir('data')[j]
    filename=os.path.join('data', files)
    df1=pd.read_csv(filename)
    df1=df1.drop([0,1])
    close=np.array(list(df1['Close']), dtype=np.float64)
    returns=[]
    for i in range(1, len(close)):
        ret=(close[i]-close[i-1])/close[i-1]
        returns.append(ret)
    df[f'col_{j}']=returns
    var_val=np.var(np.array(close, dtype=np.float64))
    variances.append(var_val)
var_df['Volatility']=variances
var_df.to_csv('Volatility.csv')
df.to_csv('Data.csv')
print('Done!!')



