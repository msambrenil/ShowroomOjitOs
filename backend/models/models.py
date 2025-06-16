from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from ..database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="vendedor")

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String, index=True)
    whatsapp = Column(String, unique=True, index=True)
    email = Column(String, nullable=True)
    genero = Column(String, default="Otro")
    nivel = Column(String, default="Plata")
    imagen = Column(String, nullable=True)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    categoria = Column(String, index=True)
    precio_revista = Column(Float)
    precio_showroom = Column(Float)
    precio_feria = Column(Float)
    stock_actual = Column(Integer, default=0)
    stock_critico = Column(Integer, default=0)
    imagen = Column(String, nullable=True)

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    fecha_venta = Column(DateTime, default=datetime.utcnow)
    estado = Column(String, default="Armado")
    total = Column(Float, default=0)

    client = relationship("Client")
