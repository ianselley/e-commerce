from sqlalchemy import Table, Column, ForeignKey, Integer

from src.database import Base


buyers_and_products = Table('buyers_and_products', Base.metadata,
    Column('buyersId', Integer, ForeignKey('buyers.id')),
    Column('productsId', Integer, ForeignKey('products.id')),
)


orders_and_products = Table('orders_and_products', Base.metadata,
    Column('ordersId', Integer, ForeignKey('orders.id')),
    Column('productsId', Integer, ForeignKey('products.id')),
)