# docker-notes
## TOC
- [About Docker](#1)
	- [Images vs Containers](#2)
- [Running Docker](#3)
	- [Docker through CLI](#4)
	- [Docker through Dockerfile](#5)
	- [Docker through docker-compose](#6)
- [Shortcuts](#7)
	- [Spinning up a quick python container](#8)
	- [Spinning up a quick python container with dockerfile](#9)
- [References](#0)
---
	
## About Docker <a name="1"></a>
- Containers are completely isolated environments that share the same OS kernel
- This means that hardware access has to go through the OS to communicate with the HAL API
- Docker is a LXC type of container 
- When you spin up a container on Windows it use to run on a Virtual Box shim. Now a days it runs on Hyper-V
- Docker is designed to run a specific task like a Meeseeks from 

![](Pasted%20image%2020210127162358.png)

### Images vs Containers <a name="2"></a>
Images are the OS's that someone has built. There is a few root ones that all others are essentially based on. A large majority of images are based on Debian, Pine or some other stripped down operating system. Then developers take those base images and tweak them for what they need. 

Let's take the [Postgres](https://github.com/docker-library/postgres/blob/ba302205a1300a5ad262ee770f7ac8a1038e8fde/13/Dockerfile) image as an example. Postgres is a well know database. Their image isn't just a Postgres binary, it's a `debian:buster-slim` operating system with the necessary Debian packages needed to run Postgres without any installation from the user. 

## Running Docker <a name="3"></a>
- There are 3 common ways to run docker.
	- Docker through CLI
	- Docker through Dockerfile
	- Docker through docker-compose

### Docker through CLI <a name="4"></a>
You can easily start up a docker container and run a single script all through a single command like the following.
```bash
docker run -it --rm --name my-running-script -p 80:80 -v "$PWD":/usr/src/app -w /usr/src/app node:8 node your-daemon-or-script.js
```
The line above will pull a node image if it's not already available and start a container with that image and run `your-daemon-or-script.js`. When it is done it will die, but if it's a daemon you'll need to kill it with `docker stop my-running-script`

There are even more switches that you can add to fine tune the container. This can lead to a gurthy command line. To avoid this you use Docker files to try to consolidate.

### Docker through Dockerfile <a name="5"></a>
A Dockerfile defines how an image is built, not how it is used. So you won't be able to port over all the CLI commands here.

Dockerfile is a textfile containing all the configurations needed to build an image. Unlike using the CLI, you can also add more configurations to it like using the `RUN` which runs OS level commands such as downloading additional packages for the OS.

The following is a Dockerfile the replaces the build portions of the CLI and adds extra build commands to showcase the power of it.
```Dockerfile
FROM node:8
WORKDIR /usr/src/app
EXPOSE 80/tcp
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.1/zsh-in-docker.sh)"

# Run your script
CMD ["node", "your-daemon-or-script.js"]

# Or suspend the container 
ENTRYPOINT ["tail", "-f", "/dev/null"]
```
With that file created, we can now build the image from that Dockerfile.
```bash
# Build using the docker file. The -t gives a tag name to the build
docker build -f /path/to/Dockerfile -t my-build-app .

# Containerize the image built; ommit the -d to attach a terminal
docker run -it -d --rm --name my-running-app --mount type=bind,source="$(pwd)",target=/usr/src/app my-build-app

# Connect to the container that is running
docker exec -it my-running-app /bin/bash
```

### Docker through docker-compose <a name="6"></a>
As we mentioned earlier, Dockerfile only describes how an image should be built, not how it should be used. With a docker-compose file we can describe how it should be used! On top of that, you can specify how to set up multiple containers at a time.

Here is an example how how I set up PantherLily
> panther_bot_dockerfile
```Dockerfile
FROM python:3.7-buster
WORKDIR /opt/project

RUN echo 'alias ll="ls -lart --color=auto"' >> ~/.bashrc
COPY requirements.txt requirements.txt

RUN python -m pip install ipython
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py", "--live" ]
```
> panther_daemon_dockerfile
```Dockerfile
FROM python:3.9-buster
WORKDIR /opt/project

RUN echo 'alias ll="ls -lart --color=auto"' >> ~/.bashrc
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
WORKDIR database
CMD ["python", "update_daemon.py"]
```
> docker-compose.yml
```yml
version: '3.7'
services:
  panther_bot:
    build:
      context: .
      dockerfile: panther_bot_dockerfile
    image: pantherlily:v3.0
    container_name: panther_bot3
    volumes:
      - .:/opt/project
    dns:
      - 1.1.1.1
      - 1.0.0.1
    networks:
      - panther_network

  panther_db:
    image: postgres
    container_name: panther_db
    env_file:
      - packages/private/database.env
    volumes:
      - panther_volume:/var/lib/postgresql/data/  # Path is where the container stores sql data
    ports:
      - 5432:5432
    networks:
      - panther_network

  panther_daemon:
    build:
      context: .
      dockerfile: panther_daemon_dockerfile
    image: panther_daemon:v1.0
    container_name: panther_daemon
    volumes:
      - .:/opt/project
    networks:
      - panther_network

volumes:
  panther_volume:
    external: true
    name: panther_volume

networks:
  panther_network:
    external: true
    name: panther_network

```

With the `docker-compose.yml` you can set up the instructions for all three containers at the same time. To build and start them you use the `docker-compose` command
```bash
# Build using the docker-compose.yml file
docker-commpose build

# Start all the containers
docker-compose up -d

```


## Shortcuts <a name="7"></a>
### Spinning up a quick python container <a name="8"></a>
Commands needed:
| switch          | Description                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------------- |
| -d              | Detached Mode                                                                                               |
| -i              | Allow interaction                                                                                                            |
| -p              | If you need ports exposed `-p 80:80`                                                                        |
| --name          | Better way to view your container instead of getting the ID of the container in `docker ps`                 |
| `image`         | Image you want always goes last on the command line i.e `docker run -it --name my-container image:version`  |
| -rm             | Clean up container and files as if it never ran                                                             |
| --entrypoint | Here we can change the entry point to something that will stall the container `["tail", "-f", "/dev/null"]` |
| --mount         | Set a bind of the current directory                                                                         |
| -w              | Set a working directory                                                                                     |

```bash
docker run -it -d --rm --name temp-container --mount type=bind,source="$(pwd)",target=/code -w /code --entrypoint /bin/bash python
```

### Spinning up a python container with some tweaks <a name="9"></a>
The `ENTRYPOINT` is going to suspend the container so that we can use it as a "VM"
```Dockerfile
FROM python:3
WORKDIR /code
RUN echo 'alias ll="ls -lart --color=auto"' >> ~/.bashrc

RUN python -m pip install ipython
RUN pip install --upgrade pip

ENTRYPOINT ["tail", "-f", "/dev/null"]
```

```bash
# Build the container from the image specified in the Dockerfile
docker build -f /path/to/dockerfile -t python-tag . 

# Start the container
docker run -it --rm -d --name python_container --mount type=bind,source="$(pwd)",target=/code python-tag

# Connect to the container that is running
docker exec -it python_container /bin/bash
```



---
## Metadata <a name="0"></a>
- `tags`: #stack #docker
- `Title`: docker-notes
- `Created`: [[20210127]] 15:21

==References==
- [Docker Tutorial](https://www.youtube.com/watch?v=fqMOX6JJhGo&t=2711s)
- [Docker Tutorial](https://www.youtube.com/watch?v=fqMOX6JJhGo&t=1203s) 
- [PostGres Image](https://hub.docker.com/_/postgres)  
- [PG & Docker Tutorial](https://www.youtube.com/watch?v=aHbE3pTyG-Q)
- [Docker install on WSL](https://medium.com/@sebagomez/installing-the-docker-client-on-ubuntus-windows-subsystem-for-linux-612b392a44c4)
- [Docker Install on WSL](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly)