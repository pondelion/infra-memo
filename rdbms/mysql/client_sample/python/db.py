from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import Settings


engine = create_engine(
    f'mysql://{Settings.DB_USERNAME}:{Settings.DB_PASSWORD}@{Settings.DB_HOST}:{Settings.DB_PORT}/{Settings.DB_NAME}?charset=utf8',
    pool_pre_ping=True
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = Session()
print(engine.table_names())