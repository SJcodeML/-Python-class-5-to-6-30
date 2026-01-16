from fastapi import FastAPI 
from models import Product
app = FastAPI()

@app.get("/")
def greet():
    return "Hello from main.py!"


products = [
    Product(id=1, name="Laptop", description="A high-performance laptop", price=999.99, quantity=10),
    Product(id=2, name="Smartphone", description="A latest model smartphone", price =699.99, quantity=25),
    Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=50)          
]

@app.get("/products")
def get_products():
    return products




