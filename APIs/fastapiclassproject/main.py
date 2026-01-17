from fastapi import FastAPI 
from models import Product


app = FastAPI()

@app.get("/")
def greet():
    return "Hello from main.py!"


product = [
    Product(id=1, name="Laptop", description="A high-performance laptop", price=999.99, quantity=10),
    Product(id=2, name="Smartphone", description="A latest model smartphone", price =699.99, quantity=25),
    Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=50)          
]

@app.get("/product")
def get_products():
    return product

@app.get("/product/{id}")
def get_product_by_id(id: int):
   for product_item in product:
       if product_item.id == id:
           return product_item
    




@app.post("/product")
def add_product(product_item :Product):
    product.append(product_item)
    return product_item

@app.put("/product/{id}")
def update_product(id: int, updated_product: Product):
    for i, product_item in enumerate(product):
        if product_item.id == id:
            product[i] = updated_product
            return updated_product
    


@app.delete("/product/{id}")
def delete_product(id:int) :
    for i , product_item in enumerate(product):
        if product_item.id == id:
            del product[i] 
            return f"Product with id {id} has been deleted."  