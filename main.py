from fastapi import FastAPI
from models import Product
from database import session
from database import session, engine
import database_models 

app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)
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
    db=session()
    db.query()
    return products

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id==id:
            return product
    return "product not found"

@app.get("/product")
def add_product(product: Product):
    products.append()
    return product

@app.put("/product")
def update_product(id:int, product: Product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]=product
            return "Product Added Successfully"

    return "Product not found"

app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return "Product Deleted"

    return "product not found"