from models import User, Item
from db import db


users = db.query(User).all()
print(users)

user = db.query(User).get(1)
print(user.__dict__)
