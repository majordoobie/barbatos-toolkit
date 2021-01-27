# docker-notes
## About Docker


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