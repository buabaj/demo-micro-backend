
import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
load_dotenv()

SQLALCHEMY_DATABASE_URL = 'postgresql://ezjfckwlkbtqfp:19ea2be7e380045a0d941e0ab4e7e5391033d0829f4d34afd5097965ca5201fd@ec2-3-219-204-29.compute-1.amazonaws.com:5432/dcqa11k3fhjlus'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
