# e-commerce

### Website public at: http://141.94.176.83:8001/

&nbsp;

## About The Project

An e-commerce web inspired by Amazon and Wallapop.

## Getting Started

### Prerequisites

You need to have installed the following:

- git
- docker

### Installation

FOR THE MOMENT, IT IS NOT WORKING DUE TO A BUG IN THE DATABASE CONTAINER

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
IP_ADDRESS={your local ip address}
ACCESS_TOKEN={a random string}

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
MYSQL_ROOT_PASSWORD={root password}
MYSQL_USER={user name}
MYSQL_PASSWORD={user password}
MYSQL_HOST=db
MYSQL_PORT=3306
MYSQL_DATABASE=e-commerce

# [PHPMYADMIN]
PMA_ARBITRARY=1
PMA_HOST=db
PMA_PORT=3306
```

4. Fill the variables IP_ADDRESS, ACCESS_TOKEN and MYSQL credentials

5. Build and run the docker containers (this step will take a long time)

```
docker-compose up --build
```

Now you should be able to view the web at: http://[your-local-ip]
