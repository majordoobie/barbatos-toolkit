# dragontoolkit

## Collection of notes and scripts used for configuring servers or participating in CTFs

---
# Quick Ref

## Quick python instance
```Dockerfile
FROM python:3 # Installs the latest should be debian image at this time also don't include this comment
WORKDIR /code
RUN echo 'alias ll="ls -lart --color=auto"' >> ~/.bashrc

RUN python -m pip install ipython
RUN pip install --upgrade pip

ENTRYPOINT ["tail", "-f", "/dev/null"]
```
```bash
docker build -f /path/to/dockefile -t python_tag . 
docker run -it --rm -d --name python_container --mount type=bind,source="$(pwd),target=/code python_tag  
docker exec -it python_container /bin/bash
```
> The `--rm` will make sure the clean up the container when you stop it so it will leave your disk dirty. But the tag will still exits you can see it with `docker images`. So to spin it back up you just need the run line again
