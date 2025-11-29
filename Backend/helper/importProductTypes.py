from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import Category, ProductType  # Import your SQLAlchemy models

# Database connection string
# DATABASE_URL = "postgresql://your_user:your_password@localhost/your_database"
# DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/pitcrew_local_v1"
DATABASE_URL = "postgresql+psycopg2://postgres:admin123@localhost:5432/postgres"



# Create the database engine
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Define categories and their respective product types
categories = {
    "Tops": ["T-Shirts", "Shirts", "Sweatshirts & Hoodies", "Sweaters & Cardigans", "Tank Tops"],
    "Bottoms": ["Jeans", "Trousers & Chinos", "Joggers & Sweatpants", "Cargo Pants", "Shorts"],
    "Outerwear": ["Jackets", "Blazers & Coats", "Trench Coats", "Parkas", "Windbreakers"],
    "Ethnic & Traditional Wear": ["Kurta & Pajama", "Sherwani", "Nehru Jacket", "Dhoti", "Pathani Suit"],
    "Innerwear & Loungewear": ["Undershirts & Vests", "Boxers & Briefs", "Thermal Wear", "Pajamas & Sleepwear"],
    "Activewear & Sportswear": ["Gym T-Shirts & Tank Tops", "Compression Wear", "Running Shorts", "Track Pants", "Sports Jackets"],
    "Accessories": ["Caps & Hats", "Gloves", "Scarves", "Belts & Suspenders", "Socks", "Ties & Bowties"]
}

try:
    for category_name, product_types in categories.items():
        # Fetch category ID from the category table
        category = session.query(Category).filter_by(category_name=category_name).first()
        
        if category:
            for product_type in product_types:
                existing_product_type = session.query(ProductType).filter_by(product_type=product_type, category_id=category.id).first()
                
                if not existing_product_type:
                    new_product_type = ProductType(
                        product_type=product_type,
                        category_id=category.id
                    )
                    session.add(new_product_type)
    
    session.commit()
    print("Product types inserted successfully!")
except Exception as e:
    session.rollback()
    print(f"Error inserting product types: {e}")
finally:
    session.close()
