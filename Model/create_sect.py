import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import pandas as pd

engine = sqlalchemy.create_engine('sqlite:///sample4.db')
Base = declarative_base()

new = pd.read_csv('/home/pallabeedey/stock_exchange_comp.csv')
NEW=new.sort_values(by='exchange', ascending=1)
NEW=NEW.tail(100)
NEW=NEW.reset_index(level=None)
new2=NEW.groupby("exchange").agg({"company":"nunique","stock":"nunique"})
new2=new2.reset_index(level=None)
new2=new2.rename(columns=({"stock":"stock_nos","company":"company_nos"}))

class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('company.id'), primary_key=True)
    exchange_id = Column(Integer, ForeignKey('exchange.id'), primary_key=True)
    name = Column(String(80), nullable=False)

class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    
    name = Column(String(80), nullable=False)
    s = relationship('Stock', backref='company',
                         primaryjoin=id == Stock.company_id)    
                         
    def __init__(self, name):
        
        self.name = name

    def __repr__(self):
        return "Industry(ind_id={self.ind_id}, name={self.name})".format(self=self)
        
class Exchange(Base):
    __tablename__ = 'exchange'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    s = relationship('Stock', backref='exchange',
                         primaryjoin=id == Stock.exchange_id)
       
                         
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Stock {}>'.format(self.name)
        
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

s_id = 0
for i in range(0,2):
    exch = new2["exchange"][i]
    ex = Exchange(name= exch)
    l = new2["company_nos"][i]
    for j in range(0,l):
       ind = NEW["company"][s_id]
       comp = Company(name= ind)
       stck= NEW["stock"][s_id]
       stock = Stock(id= (s_id+1), exchange_id= ex.id, company_id= comp.id, name= stck)
       ex.s.append(stock)
       comp.s.append(stock)
       session.add(comp)
       s_id = s_id+1
    session.add(ex)
           
    
session.commit()
