from app.database import SessionLocal
from app.models import Product

db = SessionLocal()


products = [
    Product(id=1, name="T-Shirt", price=19.99, size="M"),
    Product(id=2, name="Joggers", price=49.99, size="L"),
    Product(id=3, name="Jacket", price=99.99, size="XL"),
]

db.add_all(products)
db.commit()
db.close()
print("Seeded database with products.")