from fastapi import FastAPI, Depends
from routers import products, users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#Products Page
app.include_router(products.router)

#Users Page
app.include_router(users.router)
