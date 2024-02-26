import random
import string
from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
fake = Faker()

class SalesTerritory(Base):
    __tablename__ = 'sales_territory'

    sales_territory_id = Column(Integer, primary_key=True)
    sales_territory_country = Column(String)
    sales_territory_region = Column(String)
    sales_territory_city = Column(String)

def generate_random_data():
    country = fake.country()
    region = fake.state()
    city = fake.city()

    return SalesTerritory(
        sales_territory_country=country,
        sales_territory_region=region,
        sales_territory_city=city
    )

if __name__ == '__main__':
    try:
        engine = create_engine('postgresql://postgres:postgres@postgres/rembo')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Count the existing records in the table
        existing_records = session.query(SalesTerritory).count()

        if existing_records == 11:
            print("The table already contains 11 records. No additional records will be inserted.")
        elif existing_records < 11:
            for _ in range(11 - existing_records):  # Insert the difference in rows
                data = generate_random_data()
                session.add(data)
            session.commit()
            print("Sample data for territories inserted successfully.")
        else:
            print("Error: Table contains more than 11 records. Data insertion aborted.")

    except Exception as error:
        print("Error while inserting data:", error)

    finally:
        session.close()
