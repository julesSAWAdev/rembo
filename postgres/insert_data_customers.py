import random
import string
from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

Base = declarative_base()
fake = Faker('en_US')

class Customer(Base):
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True)
    last_name = Column(String)
    address_line1 = Column(String)
    address_line2 = Column(String)
    birth_date = Column(Date)
    age = Column(Integer)
    commute_distance = Column(Integer)
    customer_alternate_key = Column(String)
    customer_key = Column(String)
    date_first_purchase = Column(Date)
    email_address = Column(String)
    english_education = Column(String)
    english_occupation = Column(String)
    french_education = Column(String)
    first_name = Column(String)
    french_occupation = Column(String)
    gender = Column(String)
    house_owner_flag = Column(String)
    marital_status = Column(String)
    middle_name = Column(String)
    name_style = Column(String)
    number_cars_owned = Column(Integer)
    number_children_at_home = Column(Integer)
    phone = Column(String)
    spanish_education = Column(String)
    spanish_occupation = Column(String)
    suffix = Column(String)
    title = Column(String)
    total_children = Column(Integer)
    yearly_income = Column(Integer)

def generate_random_data():
    last_name = fake.last_name()
    address_line1 = fake.street_address()
    address_line2 = fake.secondary_address()
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90)
    age = fake.random_int(min=18, max=90)
    commute_distance = fake.random_int(min=1, max=50)
    customer_alternate_key = uuid.uuid4().hex
    customer_key = uuid.uuid4().hex
    date_first_purchase = fake.date_this_century()
    email_address = fake.email()
    english_education = fake.random_element(elements=('High School', 'Bachelor', 'Master', 'PhD'))
    english_occupation = fake.random_element(elements=('Engineer', 'Doctor', 'Teacher', 'Lawyer'))
    french_education = fake.random_element(elements=('High School', 'Bachelor', 'Master', 'PhD'))
    first_name = fake.first_name()
    french_occupation = fake.random_element(elements=('Engineer', 'Doctor', 'Teacher', 'Lawyer'))
    gender = fake.random_element(elements=('Male', 'Female'))
    house_owner_flag = fake.random_element(elements=('Y', 'N'))
    marital_status = fake.random_element(elements=('Single', 'Married', 'Divorced'))
    middle_name = fake.first_name()
    name_style = fake.random_element(elements=('Mr.', 'Mrs.', 'Miss', 'Dr.'))
    number_cars_owned = fake.random_int(min=0, max=5)
    number_children_at_home = fake.random_int(min=0, max=5)
    phone = fake.phone_number()
    spanish_education = fake.random_element(elements=('High School', 'Bachelor', 'Master', 'PhD'))
    spanish_occupation = fake.random_element(elements=('Engineer', 'Doctor', 'Teacher', 'Lawyer'))
    suffix = fake.random_element(elements=('Jr.', 'Sr.', 'III'))
    title = fake.random_element(elements=('Manager', 'Director', 'Engineer', 'Doctor'))
    total_children = fake.random_int(min=0, max=10)
    yearly_income = fake.random_int(min=10000, max=150000)

    return Customer(
        last_name=last_name,
        address_line1=address_line1,
        address_line2=address_line2,
        birth_date=birth_date,
        age=age,
        commute_distance=commute_distance,
        customer_alternate_key=customer_alternate_key,
        customer_key=customer_key,
        date_first_purchase=date_first_purchase,
        email_address=email_address,
        english_education=english_education,
        english_occupation=english_occupation,
        french_education=french_education,
        first_name=first_name,
        french_occupation=french_occupation,
        gender=gender,
        house_owner_flag=house_owner_flag,
        marital_status=marital_status,
        middle_name=middle_name,
        name_style=name_style,
        number_cars_owned=number_cars_owned,
        number_children_at_home=number_children_at_home,
        phone=phone,
        spanish_education=spanish_education,
        spanish_occupation=spanish_occupation,
        suffix=suffix,
        title=title,
        total_children=total_children,
        yearly_income=yearly_income
    )

if __name__ == '__main__':
    try:
        engine = create_engine('postgresql://postgres:postgres@postgres/rembo')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        for _ in range(100):  # Insert 1000 rows 
            data = generate_random_data()
            session.add(data)
        session.commit()
        print("Sample data for customers inserted successfully.")

    except Exception as error:
        print("Error while inserting data:", error)

    finally:
        session.close()
