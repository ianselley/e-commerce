import os

FRONTEND = {
    "FRONT_END_PORT": os.getenv("FRONT_END_PORT"),
}

BACKEND = {
    "PORT": os.getenv("PORT"),
    "BACKEND_CORS_ORIGINS": os.getenv("BACKEND_CORS_ORIGINS"),
}

DATABASE = {
    "MYSQL_HOST": os.getenv("DB_HOST"),
    "MYSQL_PORT": os.getenv("DB_PORT"),
    "MYSQL_USER": os.getenv("DB_USER"),
    "MYSQL_PASSWORD": os.getenv("DB_PASSWORD"),
    "MYSQL_ROOT_PASSWORD": os.getenv("DB_ROOT_PASSWORD"),
    "MYSQL_DATABASE": os.getenv("DB_DATABASE"),

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