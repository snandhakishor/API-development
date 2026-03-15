from fastapi import FastAPI
from . import model
from .database import engine
from .routers import posts, users, auth, votes
from fastapi.middleware.cors import CORSMiddleware

# model.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# async def is optional
@app.get('/') # decorator
def read_root():
    return {"Hello": "World!!!"}




app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)