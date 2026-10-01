from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import SessionLocal, engine
import database_models 
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://glowing-acorn-7vvvprj5r454hp9w9-3000.app.github.dev",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

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

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db=SessionLocal()

    count=db.query(database_models.Product).count()

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
init_db()

@app.get("/products")
def get_all_products(db: Session=Depends(get_db)):

    db_products=db.query(database_models.Product).all()

    
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id:int, db: Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return "product not found"

@app.post("/products")
def add_product(product: Product, db: Session=Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products")
def update_product(id:int, product: Product, db: Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name=product.name
        db_product.description=product.description
        db_product.price=product.price
        db_product.quantity=product.quantity
        db.commit()
        return "Product Updated"
    else:
        return "Product not found"

@app.delete("/products")
def delete_product(id: int, db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product Deleted"
    else:
        return "product not found"