from fastapi import FastAPI
from routers.invoice import router as invoice_router  # Ensure correct import

app = FastAPI()

# Include routers
app.include_router(invoice_router, prefix="/api/v1", tags=["Invoices"])

@app.get("/")
def home():
    return {"message": "Welcome to Smart Invoice Analyzer API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
