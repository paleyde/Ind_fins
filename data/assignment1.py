import pandas as pd
company = pd.read_csv('/home/pallabeedey/Downloads/company-data.csv')
company1=company.rename(columns={'Co_Code':'comp_code','Year End':'date','Co_Name':'comp_name','Sector':'sector','Industry':'industry','Stock Exchange':'stock_code','Equity Paid Up':'equity_paid_up','Net Sales':'net_sales','Debt-Equity Ratio[Latest]':'debt_equity_ratio[Latest]'})
#company   
comp=company1.groupby('comp_code').agg({'comp_name': "first"})
comp=comp.reset_index(level=None)
comp.to_csv("comp.csv")
#exchange 
col1=company1['stock_code'].unique()
l=len(col1)
s=['National Stock Exchange','National Stock Exchange-small and medium enterprise']
a=pd.DataFrame({'exch_code':col1,'exch_name':s})
#a.to_csv("exchn.csv")
#company_financials    
data=company1.rename(columns={'Year End':'date'})
comp_finc = company1[['comp_code', 'date', 'equity_paid_up', 'net_sales', 'PAT', 'PBIDT', 'debt_equity_ratio[Latest]', 'PBIDTM (%)[Latest]' ]].set_index(['comp_code', 'date'])
#comp_finc.to_csv("company_financial.csv")
#sector
col3=company1['sector'].unique()
l1=len(col3)
s1=[]
for i in range(0,l1):
    s1.append(str('S')+str(i))
b=pd.DataFrame({'sector_code':s1,'sector_name':col3})
#b.to_csv("sec2.csv")
#industry
col4=company1['industry'].unique()
l2=len(col4)
s2=[]
for i in range(0,l2):
    s2.append(str('I')+str(i))
c=pd.DataFrame({'industry_code':s2,'industry_name':col4})
#c.to_csv("ind2.csv")
#stock
stock=company1.groupby('comp_code').agg({'NSE Symbol': "first",'stock_code':"first"})
stck=stock.rename(columns={'NSE Symbol':'stock_symbol','stock_code':'exch_code'})
#stck.to_csv("stock.csv")
df=company1.set_index(["comp_name","sector","industry"])
df=df["comp_code"]
df=df.reset_index(level=None)
df=df.groupby("comp_name").agg({"sector":"first","industry":"first"})
df=df.sort_values(by='industry', ascending=0)
df=df.reset_index(level=None)
#company_sector_industry
sec = pd.read_csv('/home/pallabeedey/Indian_fins/data/sec2.csv')
ind = pd.read_csv('/home/pallabeedey/Indian_fins/data/ind2.csv')
company = pd.read_csv('/home/pallabeedey/Downloads/company-data.csv')
company1=company.rename(columns={'Co_Code':'comp_code','Year End':'date','Co_Name':'comp_name','Sector':'sector','Industry':'industry','Stock Exchange':'stock_code','Equity Paid Up':'equity_paid_up','Net Sales':'net_sales','Debt-Equity Ratio[Latest]':'debt_equity_ratio[Latest]'})

df=company1.set_index(["comp_name","sector","industry"])
df=df["comp_code"]
df=df.reset_index(level=None)
df=df.groupby("comp_name").agg({"sector":"first","industry":"first"})
df=df.sort_values(by='industry', ascending=0)
df=df.reset_index(level=None)
e=[]
f=[]
for i in range(0,1754):
    comp=df["sector"][i]
    for j in range(0,72):
        sect = sec["sector_name"][j]
        if comp==sect :
            e1=sec["sector_code"][j]
            e.append(e1)
            
        else:
            f=sec["sector_code"][j]
E=pd.DataFrame(e,columns=["sector_code"]) 
df1=pd.concat([df, E], axis=1)
df1["sector_code"]=df1["sector_code"].str.replace("S"," ")
#industry
e3=[]
f3=[]
for i in range(0,1754):
    comp1=df["industry"][i]
    for j in range(0,281):
        indu = ind["industry_name"][j]
        if comp1==indu :
            e4=ind["industry_code"][j]
            e3.append(e4)
            
        else:
            f3=ind["industry_code"][j]
E1=pd.DataFrame(e3,columns=["industry_code"]) 
df11=pd.concat([df, E1], axis=1)
df11["industry_code"]=df11["industry_code"].str.replace("I"," ")
n1=df1["comp_name"]
n2=df1["sector_code"]
n3=df1["sector"]
n4=df1["industry"]
n5= df11["industry_code"]
new=pd.DataFrame({'company':n1,'sector_name':n3,'industry_name':n4,'sector_code':n2,'industry_code':n5})
#nw=pd.read_csv('/home/pallabeedey/c_s_i.csv')
new["industry_code"]=pd.to_numeric(new["industry_code"])
new["sector_code"]=pd.to_numeric(new["sector_code"])
new=new.sort_values(by='sector_name', ascending=1)
new=new.reset_index(level=None)
#new.to_csv("company_industry_sector_data.csv")
new1=new.groupby("sector_name").agg({"industry_name":"nunique","company":"nunique"})
new1=new1.reset_index(level=None)
new1=new1.rename(columns=({"company":"comp_nos","industry_name":"ind_nos"}))
#new1.to_csv("sector_company_industry_by_nos.csv")
