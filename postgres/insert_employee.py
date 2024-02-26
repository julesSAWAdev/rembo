import random
import string
from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
fake = Faker()

class SalesTerritory(Base):
    __tablename__ = 'sales_territory'

    sales_territory_id = Column(Integer, primary_key=True)
    sales_territory_country = Column(String)
    sales_territory_region = Column(String)
    sales_territory_city = Column(String)

class Employee(Base):
    __tablename__ = 'employee'

    employee_id = Column(Integer, primary_key=True)
    employee_name = Column(String)
    employee_territory_region = Column(String)

def generate_random_data(session):
    # Fetching all available regions from sales_territory table
    regions = session.query(SalesTerritory.sales_territory_region).distinct().all()
    available_regions = [region[0] for region in regions]

    name = fake.name()
    territory_region = random.choice(available_regions)

    return Employee(
        employee_name=name,
        employee_territory_region=territory_region
    )

if __name__ == '__main__':
    try:
        engine = create_engine('postgresql://postgres:postgres@postgres/rembo')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Count the existing records in the table
        existing_records = session.query(Employee).count()

        if existing_records >= 50:
            print("The table already contains 50 or more records. No additional records will be inserted.")
        else:
            for _ in range(50 - existing_records):  # Insert the difference in rows
                data = generate_random_data(session)
                session.add(data)
            session.commit()
            print("Sample data for employees inserted successfully.")

    except Exception as error:
        print("Error while inserting data:", error)

    finally:
        session.close()
