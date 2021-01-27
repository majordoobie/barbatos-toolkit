# docker-notes
## About Docker
- Containers are completely isolated environments that share the same OS kernel
- This means that hardware access has to go through the OS to communicate with the HAL API
- Docker is a LXC type of container 
- When you spin up a container on Windows it use to run on a Virtual Box shim. Now a days it runs on Hyper-V
- Docker is designed to run a specific task like a Meeseeks

![](Pasted%20image%2020210127162358.png)

### Images vs Containers
Images are the OS's that someone has built. There is a few root ones that all others are essentially based on. A large majority of images are based on Debian, Pine or some other stripped down operating system. Then developers take those base images and tweak them for what they need. 

Let's take the [Postgres](https://github.com/docker-library/postgres/blob/ba302205a1300a5ad262ee770f7ac8a1038e8fde/13/Dockerfile) image as an example. Postgres is a well know database. Their image isn't just a Postgres binary, it's a `debian:buster-slim` operating system with the necessary Debian packages needed to run Postgres without any installation from the user. 

## Running Docker
- There are 3 common ways to run docker.
	- Docker through CLI
	- Docker through Dockerfile
	- Docker through docker-compose

### Docker through CLI
You can easily start up a docker container and run a single script all through a single command like the following.
```bash
docker run -it --rm --name my-running-script -p 80:80 -v "$PWD":/usr/src/app -w /usr/src/app node:8 node your-daemon-or-script.js
```
The line above will pull a node image if it's not already available and start a container with that image and run `your-daemon-or-script.js`. When it is done it will die, but if it's a daemon you'll need to kill it with `docker stop my-running-script`

There are even more switches that you can add to fine tune the container. This can lead to a gurthy command line. To avoid this you use Docker files to try to consolidate 

### Docker through Dockerfile
A Dockerfile defines how an image is built, not how it is used. So you won't be able to port over all the CLI commands here.

Dockerfile is a textfile containing all the configurations needed to build an image. Unlike using the CLI, you can also add more configurations to it like using the `RUN` which runs OS level commands such as downloading additional packages for the OS.

The following is a Dockerfile the replaces the build portions of the CLI and adds extra build commands to showcase the power of it.
```Dockerfile
FROM node:8
WORKDIR /usr/src/app
EXPOSE 80/tcp
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.1/zsh-in-docker.sh)"
CMD ["node", "your-daemon-or-script.js"]
```



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
#### Dockerfile style
```Dockerfile
FROM python:3 # Installs the latest should be debian image at this time also don't include this comment
WORKDIR /code
RUN echo 'alias ll="ls -lart --color=auto"' >> ~/.bashrc

RUN python -m pip install ipython
RUN pip install --upgrade pip

ENTRYPOINT ["tail", "-f", "/dev/null"]
```




---
## Metadata
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