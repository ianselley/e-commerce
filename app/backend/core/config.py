import os

MYSQL_ROOT_PASSWORD=os.environ.get("MYSQL_ROOT_PASSWORD")
MYSQL_USER=os.environ.get("MYSQL_USER")
MYSQL_PASSWORD=os.environ.get("MYSQL_PASSWORD")
MYSQL_HOST=os.environ.get("MYSQL_HOST")
MYSQL_PORT=os.environ.get("MYSQL_PORT")
MYSQL_DATABASE=os.environ.get("MYSQL_DATABASE")

BACKEND_CORS_ORIGINS=os.environ.get("BACKEND_CORS_ORIGINS")
PORT=os.environ.get("PORT")

FRONT_END_PORT=os.environ.get("FRONT_END_PORT")