from sqlalchemy import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

#set up database and base classes
engine = create_engine('sqlite:///company.db')
Base = declarative_base()

#define Employee model
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer,Sequence('employee_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    department = Column(String(50))
    salary = Column(Integer)
#create the table
metadata = MetaData()
metadata.reflect(bind=engine)
Base.metadata.create_all(engine)
employees = metadata.tables['employees']

#reflect the emp teble to retrive details 
inspector = inspect(engine)
columns = inspector.get_columns('employees') #list of dict

print("Table employee details ")
for column in columns:
    print(f"Column: {column['name']} - type: {column['type']}")
    
#create sessions
Session = sessionmaker(bind = engine)
session = Session()

#Adding records
employees = [
    Employee(name='John Doe', age=30, department='IT', salary=50000),
    Employee(name='Jane Smith', age=28, department='HR', salary=45000),
    Employee(name='Alice Johnson', age=32, department='Finance', salary=60000)
]
session.add_all(employees)
session.commit()

#query the db
all_employees = session.query(Employee).all()
for emp in all_employees:
    print(f'{emp.id}:  {emp.name} - {emp.department}  - ${emp.salary}')