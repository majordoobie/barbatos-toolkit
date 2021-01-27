# barbatos-tookit
Collection of notes and scripts from the internet rabbit holes.


## Quick Ref

### Quick python instance
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
docker run -it --rm -d --name python_container --mount type=bind,source="$(pwd)",target=/code python_tag
docker exec -it python_container /bin/bash
```
> The `--rm` will make sure the clean up the container when you stop it so it will leave your disk dirty. But the tag will still exits you can see it with `docker images`. So to spin it back up you just need the run line again

### Convert exception to string
```python
exc = ''.join(traceback.format_exception(type(error), error, error.__traceback__, chain=True))
```



## Structure
### Systems
> Notes pertaining to a particular system that can come in handy for CTF's
```
OS 
|
--> scripts
--> notes
```
### Class
> Any vendor classes like NET+, SEC+ etc. 

### Cybernetic
> Everything else from how-to's to note to self
#### environment
> Notes pertaining to setting up an environment or service

#### stack
> Notes pertaining to some tool or "how-to"