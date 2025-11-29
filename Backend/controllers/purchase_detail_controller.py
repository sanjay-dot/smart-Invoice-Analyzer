import logging
from sqlalchemy.orm import Session
from models.purchaseDetail import PurchaseDetail
from models.categories import Category
from models.brand import Brand
from models.productType import ProductType
from models.invoice import Invoice
from schemas import PurchaseDetailResponse
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from datetime import datetime



class PurchaseDetailController:
    
    def create_purchase_details(data: dict, db: Session):
        # print("Inside create_purchase_details with data:", data)  # Debugging line
        try:
            purchase_entries = []
            for item in data.get("purchase_details", []):
                description = item.get("description", "")
                if "-" not in description:
                    logging.warning(f"Skipping invalid description: {description}")
                    continue
                categories = db.query(Category).all()
                print("Categories:")
                for category in categories:
                    print(f"ID: {category.id}, Name: {category.category_name}")
                # brand = db.query(Brand).all()
                # product_type = db.query(ProductType).all()

                print("category:", category)
                return
                # brand_name, product_type_name = [part.strip() for part in description.split("-", 1)]
                # category = db.query(Category).filter_by(category_name=item.get("category")).first()
                # brand = db.query(Brand).filter_by(brand_name=brand_name).first()
                # product_type = db.query(ProductType).filter_by(product_type=product_type_name).first()

                if not all([category, brand, product_type]):
                    logging.warning(f"Missing relation: Category({item.get('category')}), Brand({brand_name}), ProductType({product_type_name})")
                    continue

                purchase_entry = PurchaseDetail(
                    product_name=description,
                    category_id=category.id,
                    brand_id=brand.id,
                    product_type_id=product_type.id,
                    quantity=item.get("quantity"),
                    unit_price=item.get("unit_price"),
                    total_price=item.get("total")
                )
                print("Adding purchase entry:", purchase_entry)
                return
                purchase_entries.append(purchase_entry)

            if purchase_entries:
                db.add_all(purchase_entries)
                db.commit()
                # logging.info(f"{len(purchase_entries)} purchase details added for invoice ID {invoice_id}")

        except Exception as e:
            logging.error(f"Error in create_purchase_details: {e}", exc_info=True)
