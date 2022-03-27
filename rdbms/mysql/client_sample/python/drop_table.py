from models import User, Item
from db import engine


Item.__table__.drop(engine)
User.__table__.drop(engine)
