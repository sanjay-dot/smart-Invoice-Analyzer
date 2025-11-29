from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import Category  # Absolute import


# Database connection string
# DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/pitcrew_local_v1"
DATABASE_URL = "postgresql+psycopg2://postgres:admin123@localhost:5432/postgres"


# Create the database engine
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Define categories
categories = {
    "Tops",
    "Bottoms",
    "Outerwear",
    "Ethnic & Traditional Wear",
    "Innerwear & Loungewear",
    "Activewear & Sportswear",
    "Accessories"
}

try:
    for category_name in categories:
        # Check if the category already exists
        existing_category = session.query(Category).filter_by(category_name=category_name).first()
        
        if not existing_category:
            new_category = Category(category_name=category_name)  # Ensure correct field name
            session.add(new_category)
            print(f"Inserted: {category_name}")
        else:
            print(f"Skipped (already exists): {category_name}")
    
    session.commit()
    print("Categories inserted successfully!")
except Exception as e:
    session.rollback()
    print("Error inserting categories: {e}")
finally:
    session.close()
