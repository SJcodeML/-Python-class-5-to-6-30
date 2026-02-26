from database import session ,engine
from FastAPI import FastAPI, Depends
from sqlalchemy.orm import Session

 

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins = ["http://localhost:3000"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],

)

def get_db():
    db:session()
    try:
        yield db 
    finally:
        db.close()


def init_db():
    db = session():

    count = db.query(database_models.Product).count() 


    if count == 0 :

        for product_item in product:
            db.add(database_models.Product(**product_item.model_dump()))
            db.commit()

init_db()

@app.get("/")
def greet():
    return "Hello this is sidra "


@app.get("/products/{id}")
def get_product_by_id(id:int , db:Session = Depends(get_db)):
    db_products = db.query(database_models.Product).filter(database_models.Products.id == id).first()
    if db_products:
        return db_products


@app.post("/prosucts")
def add_products(product_item : Product , db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product(**product_item.model_dump()))
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.put("/products")
def updated_product(id :int , updated_product : Product , db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product :
        db_product.name = updated_product.name
        db_product.description = updated_product.description
        db_product.price = updated_product.price
        db_product.quantity = updated_product.quantity
        db.commit()
        db.refresh(db_product)
        return db_product



@app.delete("/products/{id}")
def delete_product(id:int , db :Session = Depends (get_db)):
    db_product = db.query(datbase_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message":f "Product with {id} has been deleted."}






# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# db_url = "postgresql:psycopg2://username:password@host:5432/databasename"
# engine =create_engine(db_url)
# session =sessionmaker(autocommit = False , autoflush= False , bind=engine)        