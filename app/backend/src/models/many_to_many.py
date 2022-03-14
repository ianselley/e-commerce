from sqlalchemy import Table, Column, ForeignKey, Integer

from src.database import Base


buyers_and_items = Table('buyers_and_items', Base.metadata,
    Column('buyersId', Integer, ForeignKey('buyers.id')),
    Column('itemsId', Integer, ForeignKey('items.id')),
)


orders_and_items = Table('orders_and_items', Base.metadata,
    Column('ordersId', Integer, ForeignKey('orders.id')),
    Column('itemsId', Integer, ForeignKey('items.id')),
)