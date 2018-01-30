from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modtab import Sector
import pandas as pd

engine = create_engine('sqlite:///orm2.db')

Session = sessionmaker(bind=engine)
session = Session()


exch = pd.read_csv('/home/pallabeedey/Indian_fins/data/sec2.csv')
l1=len(exch)

for i in range(0,l1):
    code= exch['sector_code'][i]
    name= exch['sector_name'][i]
    session.add(Sector(name, code))
    
session.commit()
