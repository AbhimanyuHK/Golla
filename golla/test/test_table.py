from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Text, Binary, Column, create_engine
from sqlalchemy.orm import sessionmaker
from golla.table import BaseChild

Base = declarative_base()

host = 'localhost'
user = 'postgres'
password = 'root'
data_base = 'postgres'
port = '5432'
URL = 'postgresql://{}:{}@{}:{}/{}'
URL = URL.format(user, password, host, port, data_base)
ds_schema = 'public'

engine = create_engine(URL, encoding='utf8')
engine.connect()
Connection = sessionmaker(bind=engine)()

BaseChild.Connection = Connection


class Employee(Base, BaseChild):
    __tablename__ = "employee"
    EMPID = Column("emp_id", Integer, primary_key=True)
    NAME = Column("NAME", String)
    Age = Column("Age", Integer)


e = Employee()
e.EMPID = 100
e.Age = 20
e.NAME = "b"

Employee().save(e)

print(Employee().get_by_id(EMPID=100).__dict__)
# {'Age': 30, 'NAME': 'a', 'EMPID': 100}

print(Employee().get_all())
# [<__main__.Employee object at 0x0000014258031E48>, <__main__.Employee object at 0x0000014258031EB8>]

Employee().delete_by_id(EMPID=100)

