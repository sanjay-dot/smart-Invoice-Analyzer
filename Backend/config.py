from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:admin123@localhost:5432/postgres"

# Creating engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to get the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Check the database connection
def check_connection():
    db = next(get_db())
    try:
        # Run a simple query to check connection
        result = db.execute(text("SELECT 1;"))
        print("Database connection is successful")
        print(result.fetchone())  # Should print (1,) if successful
    except Exception as e:
        print("Error:", e)
    finally:
        db.close()

# Test the connection
check_connection()
