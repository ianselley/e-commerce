from sqlalchemy import Table, Column, ForeignKey, Integer

from db.database import Base


buyers_to_items = Table('buyers_to_items', Base.metadata,
    Column('buyers_id', Integer, ForeignKey('buyers.id')),
    Column('items_id', Integer, ForeignKey('items.id')),
)


buyers_to_addresses = Table('buyers_to_addresses', Base.metadata,
    Column('buyers_id', Integer, ForeignKey('buyers.id')),
    Column('addresses_id', Integer, ForeignKey('addresses.id')),
)





