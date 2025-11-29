from datetime import datetime
from sqlalchemy.orm import Session
from models.invoice import Invoice
from schemas import InvoiceResponse
import logging
import os
from fastapi import UploadFile
import re
import json
import camelot
import zipfile
import io
import numpy as np
from PyPDF2 import PdfReader
from controllers.purchase_detail_controller import PurchaseDetailController
# from db.session import get_db



def get_invoices(db: Session):
    try:
        invoices = db.query(Invoice).all()

        # Log the number of invoices fetched
        logging.info(f"Fetched {len(invoices)} invoices")

        # Ensure created_at, updated_at, and total_price are properly set
        for invoice in invoices:
            logging.info(f"Processing invoice ID: {invoice.id}")  # Log for each invoice
            if not invoice.created_at:
                invoice.created_at = datetime.now()
            if not invoice.updated_at:
                invoice.updated_at = datetime.now()

            if not invoice.total_price:
                invoice.total_price = invoice.subtotal - invoice.discount + invoice.tax_rate

        # Return the data as a list of InvoiceResponse models
        return [InvoiceResponse.model_validate(invoice) for invoice in invoices]

    except Exception as e:
        logging.error(f"Error in get_invoices: {e}", exc_info=True)
        raise



def process_pdf(pdf_path):
    try:
        print(f"Processing file: {pdf_path}")

        # Extract tables using Camelot
        tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream', strip_text='\n')
        purchase_data = []

        if tables.n > 0:
            table = np.array(tables[0].df)  # Convert to NumPy array
            # print("Extracted Table:\n", table)

            # Extract column headers from first row
            column_headers = [str(col).strip() for col in table[0]]
            table_data = table[1:]  # Remove header row

            # Manually define the column index mapping
            col_idx = {
                "description": 1,
                "qty": 3,
                "unit_price": 4,
                "total": 5
            }

            # Convert rows into dictionaries
            for row in table_data:
                try:
                    if not any(row):  # Skip empty rows
                        continue

                    no_value = str(row[0]).strip()
                    if not no_value.isdigit() or len(row) < 6:
                        continue

                    description = str(row[col_idx["description"]]).strip()
                    category = description.split("-")[-1].strip() if "-" in description else description
                    qty = str(row[col_idx["qty"]]).replace(",", "").strip()
                    unit_price = str(row[col_idx["unit_price"]]).replace(",", "").strip()

                    if not qty or not qty.replace(".", "", 1).isdigit():
                        continue

                    if not unit_price or not unit_price.replace(".", "", 1).isdigit():
                        continue

                    total = float(qty) * float(unit_price)

                    purchase_data.append({
                        "description": description,
                        "quantity": float(qty),
                        "unit_price": float(unit_price),
                        "total": total,
                        "category": category
                    })
                except Exception as e:
                    print(f"Row error: {e}")

        # Extract text for invoice details
        reader = PdfReader(pdf_path)
        pdf_text = " ".join(page.extract_text() or "" for page in reader.pages)

        patterns = {
            "invoice_number": r"INVOICE\s*NO\.?\s*(\d+)",
            "sub_total": r"SUBTOTAL\s+([\d,]+\.\d{2})",
            "discount": r"DISCOUNT\s+([\d,]+\.\d{2})",
            "tax_rate": r"TAX RATE\s+([\d.]+)%",
            "total_tax": r"TOTAL TAX\s+([\d,]+\.\d{2})",
            "total_amount": r"Total\s*[₹$]\s*([\d,]+\.\d{2})"
        }

        extracted = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                value = match.group(1).replace(",", "")
                extracted[key] = float(value) if key != "tax_rate" else value
            else:
                extracted[key] = 0.0 if key != "tax_rate" else "0.00"

        invoice_details = {
            "sub_total": extracted["sub_total"],
            "discount": extracted["discount"],
            "subtotal_less_discount": extracted["sub_total"] - extracted["discount"],
            "tax_rate": f"{extracted['tax_rate']}%",
            "total_tax": extracted["total_tax"],
            "total_amount": extracted["total_amount"]
        }

        return {
            "invoice_number": str(extracted.get("invoice_number", "Unknown")),
            "purchase_details": purchase_data,
            "invoice_details": invoice_details,
            "customer": {"name": "Unknown"}
        }

    except Exception as e:
        print(f"Failed to process {pdf_path}: {e}")
        return None

# Function to process ZIP file
def process_zip(zip_file_path: str, db: Session):
    invoice_data = []
    
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            if file_name.endswith(".pdf"):
                with zip_ref.open(file_name) as file:
                    file_data = io.BytesIO(file.read())
                    data = process_pdf(file_data)
                    if data:
                        invoice_data.append(data)
                        split_data(data, db)  # Pass db here
    return invoice_data



# function to split the data for insert
def split_data(data, db: Session):
    invoiceDetails = []

    if isinstance(data, dict):
        data = [data]

    for details in data:
        try:
            # print("details:", details)
            invoice_num = int(float(details["invoice_number"]))
        except (ValueError, TypeError):
            logging.warning(f"Invalid invoice_number format: {details['invoice_number']}")
            continue
        
        PurchaseDetailController.create_purchase_details(details, db)

        existing = db.query(Invoice).filter(Invoice.invoice_number == str(invoice_num)).first()
        if existing:
            logging.warning(f"Invoice {invoice_num} already exists. Skipping.")
            continue

        invoice = Invoice(
            invoice_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            invoice_number=invoice_num,
            subtotal=details["invoice_details"]["sub_total"],
            discount=details["invoice_details"]["discount"],
            tax_rate=float(details["invoice_details"]["tax_rate"].replace('%', '')),
            total_price=details["invoice_details"]["total_amount"]
        )

        db.add(invoice)
        invoiceDetails.append(invoice)

        # Optionally process category logic here

    db.commit()
    return invoiceDetails




