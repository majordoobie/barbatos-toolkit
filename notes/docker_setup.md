# Collection of Docker notes

## Basics

1. Install the base docker applications from docker hub
2. Identify the image that you want to download
3. Create config files?

## Basic Commands

| Command | Description |
| ------- | -------- |
| `docker version` | List the version of docker that you are running |
| `docker images` | Display all the images that you have downloaded |
| `docker ps` | Show the running containers |
| `docker stop <id>` | Stops a docker from running |

## Setting up PostGresSQL Docker

| Command | Description |
| ------- | -------- |
| `docker pull postgres` | Pulls the postgres socker image to your machine |
| `docker pull postgres:<tag>` | Can specify a version tag to pull others like older versions or smaller versions like the alphine one |
| `docker images` | You should be able to see your new image that you downloaded |
| `docker run --name <nickname> -e POSTGRES_PASSWORD=<passwd> -d postgres:<tag>` | Run the image that you downloaded by giving it an alias, an evironment variable and run it detached to get the terminal back just like & does with apps |
| `-p <port>:<5423>` | Specify the port that the OS should listen on to pass to the container, this is added befofore the image name *postgres* |
| `docker ps` | Show that the container is running |
| `docker exec -it <image from ps> bash` | Get an interactive shell with the image using bash |
| `psql -U postgres` | Get a admin shell to the DB |

## PostGresSQL Commands

| Command | Description |
| ------- | -------- |
| `psql -U postgres` | Get a db shell with the user, by default postgres is the admin user |
| `\du` | Display users with their roles |
| `create database <name>;` | Create a database under the context of the user you are logged on with |
| `\l` | List available databases |
| `\c <db>` | Connect to a DB |
| `\d` | List relations in the connected DB |
| `\d+ <table>` | Get more information on a table |
| `\q` | Quit out of the current db session |
| `\dt` | Show the tables in the current db you are connected to |


## Connecting to the Docker DB externally

```bash
psql -h 127.0.0.1 -p <port> -U postgres
# Promts for password
localhost:8080/api/v1/<db>
```

### Sample of a config

```
FROM Ubuntu # image base?
RUN apt-get update 
RUN apt-get install python

RUN pip install flask
RUN pip install flask-mysql

COPY . /opt/source-code

ENTRYPOINT FLASK_APPP=/opt/source-code/app.py flask run
```
---

## Sources
[Docker Tutorial](https://www.youtube.com/watch?v=fqMOX6JJhGo&t=2711s)  
[PostGres Image](https://hub.docker.com/_/postgres)  
[PG & Docker Tutorial](https://www.youtube.com/watch?v=aHbE3pTyG-Q)