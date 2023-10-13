# Janitor
A discord bot which performs multiple functions such as logging user messages

compose file:
```yml
version: '3'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - DC_TOKEN=${DC_TOKEN}
      - MYSQL_DATABASE=${DB_NAME}
      - MYSQL_USER=${DB_USER}
      - MYSQL_PASSWORD=${DB_PW}
    restart: unless-stopped
    
  db:
    hostname: db
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=${DB_ROOT_PW}
      - MYSQL_DATABASE=${DB_NAME}
      - MYSQL_USER=${DB_USER}
      - MYSQL_PASSWORD=${DB_PW}
    image: mariadb:latest
    volumes:
      - db_data:/var/lib/mysql

volumes:
  db_data:
    driver: local
```

In this `docker-compose.yml` we initiate a database container for storing usernames and messages. <br/>
The other container contains a python application to host a discord bot.

We utilize the following environment variables to configure the containers:
- `DC_TOKEN` - an env var to store the bot's discord token.
- `DB_NAME` - an env var to store the used database name.
- `DB_ROOT_PW` - an env var to store the Mariadb root password.
- `DB_USER` - an env var to store the Mariadb users name.
- `DB_PW` - an env var to store the Mariadb users password.
