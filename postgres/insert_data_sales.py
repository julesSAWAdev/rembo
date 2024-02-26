import random
import string
from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import logging

Base = declarative_base()
fake = Faker()

class Sales(Base):
    __tablename__ = 'sales'

    sales_id = Column(Integer, primary_key=True)
    currencykey = Column(String)
    customerkey = Column(String)
    discount_amount = Column(String)
    duedate = Column(String)
    duedatekey = Column(String)
    extended_amount = Column(String)
    freight = Column(String)
    order_date = Column(String)
    order_quantity = Column(String)
    product_standard_cost = Column(String)
    revision_number = Column(String)
    sales_amount = Column(String)
    sales_order_line_number = Column(String)
    sales_order_number = Column(String)
    salesterritorykey = Column(String)
    shipdate = Column(String)
    tax_amt = Column(String)
    total_product_cost = Column(String)
    unit_price = Column(String)
    unit_price_discount_pct = Column(String)
    employee_id = Column(Integer, ForeignKey('employee.employee_id'))

class Employee(Base):
    __tablename__ = 'employee'

    employee_id = Column(Integer, primary_key=True)
    employee_name = Column(String)
    employee_territory_region = Column(String)

def generate_random_data(session):
    # Fetching all employee IDs from the Employee table
    employee_ids = session.query(Employee.employee_id).all()
    available_employee_ids = [employee[0] for employee in employee_ids]

    currencykey = fake.currency_code()
    customerkey = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    discount_amount = fake.random_number(2)
    duedate = fake.date_this_year().strftime('%Y-%m-%d')
    duedatekey = fake.date_this_year().strftime('%Y%m%d')
    extended_amount = fake.random_number(2)
    freight = fake.random_number(2)
    order_date = fake.date_this_year().strftime('%Y-%m-%d')
    order_quantity = fake.random_number(2)
    product_standard_cost = fake.random_number(2)
    revision_number = fake.random_number(2)
    sales_amount = fake.random_number(2)
    sales_order_line_number = fake.random_number(2)
    sales_order_number = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    salesterritorykey = fake.random_number(2)
    shipdate = fake.date_this_year().strftime('%Y-%m-%d')
    tax_amt = fake.random_number(2)
    total_product_cost = fake.random_number(2)
    unit_price = fake.random_number(2)
    unit_price_discount_pct = fake.random_number(2)
    employee_id = random.choice(available_employee_ids)

    return Sales(
        currencykey=currencykey,
        customerkey=customerkey,
        discount_amount=discount_amount,
        duedate=duedate,
        duedatekey=duedatekey,
        extended_amount=extended_amount,
        freight=freight,
        order_date=order_date,
        order_quantity=order_quantity,
        product_standard_cost=product_standard_cost,
        revision_number=revision_number,
        sales_amount=sales_amount,
        sales_order_line_number=sales_order_line_number,
        sales_order_number=sales_order_number,
        salesterritorykey=salesterritorykey,
        shipdate=shipdate,
        tax_amt=tax_amt,
        total_product_cost=total_product_cost,
        unit_price=unit_price,
        unit_price_discount_pct=unit_price_discount_pct,
        employee_id=employee_id
    )

if __name__ == '__main__':
    try:
        engine = create_engine('postgresql://postgres:postgres@postgres/rembo')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        for _ in range(500):  # Insert 50 records
            data = generate_random_data(session)
            session.add(data)
        session.commit()
        print("Sample data for sales inserted successfully.")

    except Exception as error:
        print("Error while inserting data:", error)

    finally:
        session.close()
