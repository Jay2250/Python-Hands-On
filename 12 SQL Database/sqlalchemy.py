import pandas as pd
from sqlalchemy import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

# set up database and base classes
engine = create_engine('sqlite:///company.db')
Base = declarative_base()

# define Employee model


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, Sequence('employee_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    department = Column(String(50))
    salary = Column(Integer)


# create the table
metadata = MetaData()
metadata.reflect(bind=engine)
Base.metadata.create_all(engine)
employees = metadata.tables['employees']

# reflect the emp teble to retrive details
inspector = inspect(engine)
columns = inspector.get_columns('employees')  # list of dict

print("Table employee details ")
for column in columns:
    print(f"Column: {column['name']} - type: {column['type']}")

# create sessions
Session = sessionmaker(bind=engine)
session = Session()

# Adding records
employees = [
    Employee(name='John Doe', age=30, department='IT', salary=50000),
    Employee(name='Jane Smith', age=28, department='HR', salary=45000),
    Employee(name='Alice Johnson', age=32, department='Finance', salary=60000)
]
session.add_all(employees)
session.commit()

# query the db
all_employees = session.query(Employee).all()
for emp in all_employees:
    print(f'{emp.id}:  {emp.name} - {emp.department}  - ${emp.salary}')

# -----------------------------------------------------------------------


# setup sqlalchemy
engine = create_engine('sqlite:///employee4.db', echo=True)
Base = declarative_base()

# define the employee model


class Employee(Base):
    __tablename__ = 'employees'
    # define columns
    employee_id = Column(Integer, primary_key=True,
                         autoincrement=True)  # Ensure primary key by 1
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
# create the table


def create_table():
    Base.metadata.create_all(engine)
    print("Table created successfully")
# insert sample data


def insert_sample_data():
    Session = sessionmaker(bind=engine)
    session = Session()
    # sample data
    employees = [
        Employee(name='John Doe', position='Manager', salary=50000),
        Employee(name='Jane Smith', position='Developer', salary=60000),
        Employee(name='Alice Johnson', position='Designer', salary=55000),
        Employee(name='Bob Brown', position='Developer', salary=62000)
    ]

    # Add and commit data
    session.add_all(employees)
    session.commit()
    print("Sample data inserted successfully")
    session.close()
# read data into a pandas dataframe


def read_data():
    # load data into DataFrame
    df = pd.read_sql_table('employees', engine)
    return df
# update data in the dataframe


def update_salary(df, employee_id, new_salary):
    df.loc[df['employee_id'] == employee_id, 'salary'] = new_salary
    return df
# delete data from the dataframe


def delete_employee(df, employee_id):
    df = df[df['employee_id'] != employee_id]
    return df
# Write updated data back to the database


def write_to_database(df):
    df.to_sql('employees', engine, if_exists='replace', index=False)
    print("Updated data written to database successfully")
# main function to perform the assignment task


def main():
    # create table and insert data(run only once)
    create_table()
    insert_sample_data()
    # read data
    df = read_data()
    print("Original data:")
    print(df)

    # update salary for employee with ID 2
    df = update_salary(df, employee_id=2, new_salary=65000)
    print("\nUpdated data:")
    print(df)

    # write updated data back in df
    write_to_database(df)
    print("\nUpdated data written to database:")

    # Read data
    df = read_data()
    print("Updated data frame ")
    print(df)


if __name__ == '__main__':
    main()

# ------------------------------------------------------------------------

