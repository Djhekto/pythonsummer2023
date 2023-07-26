import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABASE_URL = "postgresql://postgresql:pass@localhost/fastapi_db"
#DATABASE_URL = "postgresql://postgresql:pass@localhost:5432/fastapi_db"

#https://docs.sqlalchemy.org/en/20/core/pooling.html#pool-disconnects
engine = _sql.create_engine(DATABASE_URL)#, pool_pre_ping=True)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
#Base = _orm.declarative_base()
