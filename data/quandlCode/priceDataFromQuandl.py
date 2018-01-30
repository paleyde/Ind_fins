import pandas as pd
import quandl
from datetime import datetime
import numpy as np
#data reading
company = pd.read_csv('/home/pallabeedey/Downloads/company-data.csv')
company1=company.rename(columns={'Co_Code':'comp_code','Year End':'date','Co_Name':'comp_name','Sector':'sector','Industry':'industry','Stock Exchange':'stock_code','Equity Paid Up':'equity_paid_up','Net Sales':'net_sales','Debt-Equity Ratio[Latest]':'debt_equity_ratio[Latest]'})
#quandl details
api_key = "8Htse_SZnFsygUz9xF58"
stck_name = company1['NSE Symbol'].unique()
#edit stock name
ln=len(stck_name)
name=[]
for i in range(0,ln):
    name.append(str('NSE/')+str(stck_name[i]))
#import data from quandl
df=pd.DataFrame()
for i in range(0,1752):
    try:
        data = quandl.get(name[i], authtoken= api_key,start_date='2016-01-08', end_date='2018-01-08')
        data=data.reset_index(drop = False)
        data['stock_name']=name[i]
        df = pd.concat([df, data], axis=0)  
    except Exception as e:
        print(str(e))

df.to_csv("stock_prices.csv") 
