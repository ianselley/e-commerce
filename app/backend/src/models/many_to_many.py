from sqlalchemy import Table, Column, ForeignKey, Integer

from src.database import Base


buyers_and_items = Table('buyers_and_items', Base.metadata,
    Column('buyers_id', Integer, ForeignKey('buyers.id')),
    Column('items_id', Integer, ForeignKey('items.id')),
)


orders_and_items = Table('orders_and_items', Base.metadata,
    Column('orders_id', Integer, ForeignKey('orders.id')),
    Column('items_id', Integer, ForeignKey('items.id')),
)