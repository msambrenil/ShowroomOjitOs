from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    role: Optional[str] = "vendedor"

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class ClientBase(BaseModel):
    nombre_completo: str
    whatsapp: str
    email: Optional[str] = None
    genero: Optional[str] = "Otro"
    nivel: Optional[str] = "Plata"

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    nombre: str
    categoria: str
    precio_revista: float
    precio_showroom: float
    precio_feria: float
    stock_actual: int
    stock_critico: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class SaleBase(BaseModel):
    client_id: int
    estado: str

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int
    fecha_venta: datetime
    total: float

    class Config:
        orm_mode = True
