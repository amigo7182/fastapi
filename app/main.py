from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind = engine)

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
@app.get('/')
def test():
    return {"message": "Hello World!"}








# import psycopg
# from psycopg.rows import dict_row
# import time

# while True:
#     try:
#         conn = psycopg.connect(host = "localhost", 
#                             dbname = "fastapi_course", 
#                             user = "postgres", 
#                             password = "Taylorgang12", 
#                             row_factory = dict_row
#                             )
#         cursor = conn.cursor()
#         print("Database connection was successfull!")
#         break
#     except Exception as error:
#         print("Connecting to database failed.")
#         print("Error:", error)
#         time.sleep(2) 