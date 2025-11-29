from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import Brand  # Import your SQLAlchemy Category model

# Database connection string
# DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/pitcrew_local_v1"
DATABASE_URL = "postgresql+psycopg2://postgres:admin123@localhost:5432/postgres"


# Create the database engine
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# List of clothing brands to insert
brands = [
    "Gucci", "Louis Vuitton", "Prada", "Balenciaga", "Chanel", "Dior", "Versace", "Givenchy", "Hermès", "Burberry",
    "Zara", "H&M", "Uniqlo", "Forever 21", "Mango", "Topshop", "American Eagle", "Gap", "ASOS", "Urban Outfitters",
    "Nike", "Adidas", "Puma", "Under Armour", "Reebok", "New Balance", "Lululemon", "Columbia", "Fila", "The North Face",
    "Levis", "Wrangler", "Lee", "Diesel", "G-Star RAW", "True Religion", "Carhartt", "Dickies",
    "Supreme", "Off-White", "Fear of God", "Stüssy", "BAPE", "Palace", "Kith", "Billionaire Boys Club",
    "Patagonia", "Everlane", "Allbirds", "Stella McCartney", "Pangaia"
]

try:
    for brand_name in brands:
        # Check if the brand already exists
        existing_brand = session.query(Brand).filter_by(brand_name=brand_name).first()
        
        if not existing_brand:
            new_brand = Brand(brand_name=brand_name)
            session.add(new_brand)

    session.commit()
    print("Brands inserted successfully!")
except Exception as e:
    session.rollback()
    print(f"Error inserting brands: {e}")
finally:
    session.close()
