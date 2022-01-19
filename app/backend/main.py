from fastapi import FastAPI
# import mysql.connector
# import os

# MYSQL_ROOT_PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD")

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd=PASSWORD,
# )


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
