from sqlalchemy.orm import Session
from .models import Product, CartItem
from app.schemas import CartItemSchema

def get_products(db: Session):
    return db.query(Product).all()

def add_cart_item(db: Session, item: CartItemSchema):
    db_item = CartItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item