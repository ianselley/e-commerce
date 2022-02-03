import os

FRONTEND = {
    "FRONT_END_PORT": os.getenv("FRONT_END_PORT"),
}

BACKEND = {
    "PORT": os.getenv("PORT"),
    "BACKEND_CORS_ORIGINS": os.getenv("BACKEND_CORS_ORIGINS"),
}

DATABASE = {
    "MYSQL_HOST": os.getenv("MYSQL_HOST"),
    "MYSQL_PORT": os.getenv("MYSQL_PORT"),
    "MYSQL_USER": os.getenv("MYSQL_USER"),
    "MYSQL_PASSWORD": os.getenv("MYSQL_PASSWORD"),
    "MYSQL_ROOT_PASSWORD": os.getenv("MYSQL_ROOT_PASSWORD"),
    "MYSQL_DATABASE": os.getenv("MYSQL_DATABASE"),
}

AUTH0 = {
    "AUTH0_DOMAIN": os.getenv("AUTH0_DOMAIN"),
    "AUTH0_CLIENT_ID": os.getenv("AUTH0_CLIENT_ID"),
    "AUTH0_CLIENT_SECRET": os.getenv("AUTH0_CLIENT_SECRET"),
    "AUTH0_CALLBACK_URL": os.getenv("AUTH0_CALLBACK_URL"),
    "AUTH0_API_AUDIENCE": os.getenv("AUTH0_API_AUDIENCE"),
    "AUTH0_ISSUER": os.getenv("AUTH0_ISSUER"),
    "AUTH0_ALGORITHMS": os.getenv("AUTH0_ALGORITHMS"),
}