from fastapi import FastAPI, Depends
from routers import products, users

app = FastAPI()

#Products Page
app.include_router(products.router)

#Users Page
app.include_router(users.router)
