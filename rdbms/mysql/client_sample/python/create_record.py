from models import User, Item
from db import db


user = User(
    name='user001',
    email='user001@example.com',
    hashed_password='testpass000',
)
db.add(user)
db.commit()
db.refresh(user)
print(user)

item = Item(
    title='item1',
    description='This is item1',
    owner_id=user.id,
)
db.add(item)
db.commit()
db.refresh(item)
