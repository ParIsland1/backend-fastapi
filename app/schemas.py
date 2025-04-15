from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
    id: int
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    size: str

    class Config:
        from_attributes = True

class CartItemSchema(BaseModel):
    id: int
    product_id: int
    quantity: int = Field(gt=0)

    class Config:
        from_attributes = True