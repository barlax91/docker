from enum import auto
import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
#URL d'accès à la base de donnée
DATABASE_URL = "postgresql://myuser:gtrk972@localhost/fastapi_database"
#crée une nouvelle instance à partir de la bdd
engine = _sql.create_engine(DATABASE_URL)
#crée une session
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
