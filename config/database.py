from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://bryan007:123456@localhost/fotoreportedb"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Crea el motor de SQLAlchemy para PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crea la fábrica de sesiones para PostgreSQL
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declara la base de SQLAlchemy
Base = declarative_base()
