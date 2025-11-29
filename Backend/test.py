from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.invoice import Invoice
from models.products import Product
from sqlalchemy.orm import joinedload

# Replace with your actual database URL
DATABASE_URL = "postgresql+psycopg2://postgres:admin123@localhost:5432/postgres"

# Create the database engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = Session()

# Try to fetch invoices with products
invoices = db.query(Invoice).options(joinedload(Invoice.products)).all()

# Print the details of the invoices
for invoice in invoices:
    print(invoice)
    print(f"Invoice ID: {invoice.id}")
    print(f"Invoice Date: {invoice.invoice_date}")
    print(f"Subtotal: {invoice.subtotal}")
    print(f"Discount: {invoice.discount}")
    print(f"Tax Rate: {invoice.tax_rate}")
    print(f"Total: {invoice.total_price}")
    print(f"Invoice Number: {invoice.invoice_number}")
