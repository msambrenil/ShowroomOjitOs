from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import init_db
from app.routers import products, clients, sales, users, categories, tags

app = FastAPI(title="Showroom Natura OjitOs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")

app.include_router(products.router)
app.include_router(clients.router)
app.include_router(sales.router)
app.include_router(users.router)
app.include_router(categories.router)
app.include_router(tags.router)


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def read_root():
    return {"message": "Showroom Natura OjitOs API"}
