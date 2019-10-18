# Collection of Docker notes

## What is Docker
- Containers are completely isolated environments that share the same OS kernel
- Docker is a LXC
- You will not be able to run a windows based container on windows
- When you install a linux container on windows, docker is spinning up a linux VM to host the container 
- This does not have a performance draw back because it does not run a compelte OS

![Container vs VM](../images/container_vs_vm.png)

## Basics

1. Install the base docker applications from docker hub
2. Identify the image that you want to download
3. Create config files?

## General notes

> Dockers, unlike a VM, only runs until the service that it was ment to run is over. It is just a container to run a task. If there is no task it will die.

## Basic Commands

| Command | Description |
| ------- | -------- |
| `docker version` | List the version of docker that you are running |
| `docker images` | Display all the images that you have downloaded |
| `docker ps` | Show the running containers |
| `docker ps -a` | Displays all running and *previously* running dockers
| `docker stop <id/name>` | Stops a docker from running |
| `docker rm <name>` | Permenetly delete an image from disc |
| `docker images` | List all the images downloaded on disc |
| `docker pull` | Pulls a docker image without running it |
| `docker attach <id>` | If using `-d` to detach, you can re attach with this option |
| `docker exec <image> <command(cat /etc/passwd)>` | Run commands in your container |
| `docker exec -it <image> bash` | Get an interactive shell on the container |

### Run Commands
| Command | Description |
| ------- | -------- |
| `docker run <image>` | Runs the image if you have it downloaded, otherwise it will download it online |
| `docker run -d <image>` | `-d` will background your docker so it does not hijack your terminal |
| `docker run <image>:<tag>` | You can specify different versions or types of a container with the colon. Be default the <latest> tag will be used |


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
[Docker Tutorial](https://www.youtube.com/watch?v=fqMOX6JJhGo&t=1203s)  
[PostGres Image](https://hub.docker.com/_/postgres)  
[PG & Docker Tutorial](https://www.youtube.com/watch?v=aHbE3pTyG-Q)