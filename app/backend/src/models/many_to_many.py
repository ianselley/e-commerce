from sqlalchemy import Table, Column, ForeignKey, Integer

from src.database import Base


buyers_and_products = Table('buyers_and_products', Base.metadata,
    Column('buyers_id', Integer, ForeignKey('buyers.id')),
    Column('products_id', Integer, ForeignKey('products.id')),
)


orders_and_products = Table('orders_and_products', Base.metadata,
    Column('orders_id', Integer, ForeignKey('orders.id')),
    Column('products_id', Integer, ForeignKey('products.id')),
)