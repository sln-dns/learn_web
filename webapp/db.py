from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('postgresql://tuifcwwp:wbxAMOPS26PoegAOZbvAXB-5xyrGRThF@hattie.db.elephantsql.com/tuifcwwp')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
