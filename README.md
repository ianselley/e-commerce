# e-commerce

## About The Project

An e-commerce web app inspired by Amazon and Wallapop.

## Getting Started

### Prerequisites

You need to have installed the following:

- git
- docker

### Installation

In the terminal/command prompt write the following commands

1. Clone the repo

```
git clone https://github.com/ianselley/e-commerce.git
```

2. cd into the directory we just created named as the repo

```
cd e-commerce
```

3. Copy the following and paste it in a file called ".env"

```
IP_ADDRESS={your local IP address}  //<--REPLACE THIS
ACCESS_TOKEN={a random string}  //<--REPLACE THIS

# [FRONTEND]
FRONTEND_PORT=8080
PUBLIC_FRONTEND_PORT=8001

# [BACKEND]
MODULE_NAME=src.main
BACKEND_PORT=3030
PUBLIC_BACKEND_PORT=3001
BACKEND_CORS_ORIGINS='["http://${IP_ADDRESS}",
    "http://${IP_ADDRESS}:${PUBLIC_FRONTEND_PORT}",
]'

# [DATABASE]
MYSQL_ROOT_PASSWORD={root password}  //<--REPLACE THIS
MYSQL_USER={user name}  //<--REPLACE THIS
MYSQL_PASSWORD={user password}  //<--REPLACE THIS
MYSQL_HOST=db
MYSQL_PORT=3306
MYSQL_DATABASE=e-commerce

# [PHPMYADMIN]
PMA_ARBITRARY=1
PMA_HOST=db
PMA_PORT=3306
```

4. Inside app/frontend/src/ create a file called "config.json" and paste the following:

```
{
  "API_URL": "http://{your IP address}:3001" //<--REPLACE THIS
}
```


5. Fill the variables IP_ADDRESS, ACCESS_TOKEN and MYSQL credentials

6. Build and run the docker containers (this step will take a long time)

```
docker-compose up --build
```

Now you should be able to view the web at: http://{your ip address}:8001


<!-- TECH STACK -->

## Tech stack

- [Python 3](https://www.python.org)
- [JavaScript](https://www.javascript.com)
- [Tailwind](https://tailwindcss.com)
- [Docker](https://www.docker.com/)
- [Vuejs](https://vuejs.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [MySQL](https://www.mysql.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
