from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = "postgresql+psycopg2://my_user:my_password@my_db_host_possibly_at.elephantsql.com:5432/my_database"

engine = create_engine(DATABASE_URL)
Connection = scoped_session(sessionmaker(bind=engine))

def db():
    connection = Connection()
    try:
        yield connection
    finally:
        connection.close()
