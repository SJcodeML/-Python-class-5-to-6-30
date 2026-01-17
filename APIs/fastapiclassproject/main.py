from fastapi import FastAPI , Depends 
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session ,engine
import database_models 
from sqlalchemy.orm import Session


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Hello from main.py!"


product = [
    Product(id=1, name="Laptop", description="A high-performance laptop", price=999.99, quantity=10),
    Product(id=2, name="Smartphone", description="A latest model smartphone", price =699.99, quantity=25),
    Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=50),          
              
    ]


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()    

def init_db():
    db = session()
    

    count = db.query(database_models.Product).count()

    if count == 0 :

        for product_item in product:
            db.add(database_models.Product(**product_item.model_dump()))
        db.commit()
    # db.close()


init_db()


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products= db.query(database_models.Product).all()
    return db_products
    
@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
   db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
   if db_product:
      return db_product




@app.post("/products")
def add_product(product_item: Product, db: Session = Depends(get_db)):
    db_product = database_models.Product(**product_item.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product      
    
   
@app.put("/products/{id}")
def update_product(id: int, updated_product: Product,db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = updated_product.name
        db_product.description = updated_product.description
        db_product.price = updated_product.price
        db_product.quantity = updated_product.quantity
        db.commit()
        db.refresh(db_product)
        return db_product

    
@app.delete("/products/{id}")
def delete_product(id:int,db: Session = Depends(get_db)) :
      db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
      if db_product:
        db.delete(db_product)
        db.commit()
        return f"Product with id {id} has been deleted."     

 