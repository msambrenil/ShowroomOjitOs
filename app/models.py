from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    password: str
    role: str = "vendedor"  # admin, vendedor, cliente


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    productos: List["Product"] = Relationship(back_populates="categoria")


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    precio_revista: float
    precio_showroom: float
    precio_feria: float
    stock_actual: int
    stock_critico: int
    categoria_id: Optional[int] = Field(default=None, foreign_key="category.id")

    categoria: Optional[Category] = Relationship(back_populates="productos")


class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre_completo: str
    whatsapp: str
    email: Optional[str]
    nivel: str = "Plata"  # Plata, Diamante


class SaleItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sale_id: Optional[int] = Field(default=None, foreign_key="sale.id")
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    cantidad: int
    precio: float


class Sale(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cliente_id: Optional[int] = Field(default=None, foreign_key="client.id")
    fecha: datetime = Field(default_factory=datetime.utcnow)
    estado: str = "Armado"  # Armado, Entregado, Cobrado
    total: float = 0

