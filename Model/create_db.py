from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modtab2 import Base

engine = create_engine('sqlite:///orm2.db')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
