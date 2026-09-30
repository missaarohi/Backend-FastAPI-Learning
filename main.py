from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to Telusko Trac"

products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10),
    Product(id=2, name="laptop", description="gaming laptop", price=999, quantity=6),
    Product(id=3, name="laptop", description="gaming laptop", price=999, quantity=6),
    Product(id=4, name="laptop", description="gaming laptop", price=999, quantity=6),
]

@app.get("/products")
def get_all_products():
    return products