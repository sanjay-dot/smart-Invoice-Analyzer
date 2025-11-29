from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config import get_db
from controllers import invoice_controller
from schemas import InvoiceResponse
import logging  # For better error logging
from fastapi import File, UploadFile
import os

router = APIRouter()

@router.get("/invoices", response_model=List[InvoiceResponse])
def get_all_invoices(db: Session = Depends(get_db)):
    try:
        invoices = invoice_controller.get_invoices(db)
        return invoices
    except Exception as e:
        # Log the error message to help debug
        logging.error(f"Error fetching invoices: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")


#functionn to upload invoices

UPLOAD_DIR = "uploads" 
@router.post("/upload-invoice")
async def upload_invoice(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure directory exists
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as f:
            f.write(await file.read())  # Save ZIP file to disk

        invoice_data = invoice_controller.process_zip(file_path,db)  # Pass file path instead of UploadFile
        return {"filename": file.filename, "status": "processed successfully", "data": invoice_data}

    except Exception as e:
        logging.error(f"Error uploading invoice: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


