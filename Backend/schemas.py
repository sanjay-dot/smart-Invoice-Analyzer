from datetime import datetime
from pydantic import BaseModel, field_validator

class InvoiceResponse(BaseModel):
    id: int
    invoice_date: str
    subtotal: float
    discount: float
    tax_rate: float
    total_price: float
    invoice_number: str
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True

    @field_validator('created_at', 'updated_at', mode='before')
    def datetime_to_string(cls, v):
        if isinstance(v, datetime):
            return v.isoformat()
        return str(v) if v else None


class PurchaseDetailResponse(BaseModel):
    id: int
    product_name: str
    category_id: int
    brand_id: int
    product_type_id: int
    quantity: float
    unit_price: float
    total_price: float
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True

    @field_validator('created_at', 'updated_at', mode='before')
    def datetime_to_string(cls, v):
        if isinstance(v, datetime):
            return v.isoformat()
        return str(v) if v else None
