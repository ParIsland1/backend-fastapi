# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, get_db
from .models import Base
from . import models, crud
from app.schemas import ProductSchema, CartItemSchema
from typing import List

app = FastAPI()

@app.get("/products", response_model=List[ProductSchema])
def read_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@app.post("/products", response_model=ProductSchema)
def create_product(product: ProductSchema, db: Session = Depends(get_db)):
    try:
        db_product = models.Product(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/cart", response_model=CartItemSchema)
def add_to_cart(item: CartItemSchema, db: Session = Depends(get_db)):
    try:
        return crud.add_cart_item(db, item)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))