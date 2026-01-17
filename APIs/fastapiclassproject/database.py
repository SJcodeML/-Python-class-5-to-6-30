from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# db_url = "postgresql://postgres:5rtxz@localhost:5432/fastapi_db"
db_url = "postgresql+psycopg2://postgres:89iop@localhost:5432/practice_db"
engine = create_engine(db_url)
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)