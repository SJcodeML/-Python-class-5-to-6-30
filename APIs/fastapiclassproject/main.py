from fastapi import FastAPI 
from models import Product


app = FastAPI()

@app.get("/")
def greet():
    return "Hello from main.py!"


# product = [
#     Product(id=1, name="Laptop", description="A high-performance laptop", price=999.99, quantity=10),
#     Product(id=2, name="Smartphone", description="A latest model smartphone", price =699.99, quantity=25),
#     Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=50)          
# ]

# @app.get("/product")
# def get_products():
#     return product

# @app.get("/product")
# def get_product_by_id(product_id: int):
#    return product[0]


