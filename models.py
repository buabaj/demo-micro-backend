from sqlalchemy import Column, Integer, String
from database import Base


class Waitlist(Base):
    __tablename__ = "waitlist"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    section = Column(String(100))

    def __init__(self, name, email, section):
        self.name = name
        self.email = email
        self.section = section
