from sqlalchemy import Column, ForeignKey, Integer, Date
from sqlalchemy.orm import relationship
import datetime

from src.database import Base
from .many_to_many import orders_to_items


'''
TODO
Hay que diferenciar entre un pedido de un usuario y un pedido de un vendedor.
El pedido de un usuario es una lista de todos los items que ha comprado, con la cantidad de cada uno,
y el pedido de un vendedor es una lista de los items que ha vendido a un usuario y que le pertenecen.
En otras palabras, el pedido de un vendedor es una lista parcial del pedido de un usuario.

Ejemplo:
  - Pedido usuario:
    - Movil_1: 3
    - Movil_2: 2
    - Ordenador: 2
  - Pedido vendedor (de moviles):
    - Movil_1: 3
    - Movil_2: 2
  - Pedido vendedor (de ordenadores):
    - Ordenador: 2
'''


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    date = Column(Date, default=datetime.datetime.now)
    quantity = Column(Integer, default=1)
    buyer_id = Column(Integer, ForeignKey("buyers.id"))

    buyer = relationship("Buyer", back_populates="orders")
    items = relationship("Item", secondary=orders_to_items, back_populates="orders")

