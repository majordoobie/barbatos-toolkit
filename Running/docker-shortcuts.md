Commands needed:
| switch          | Description                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------------- |
| -d              | Detached Mode                                                                                               |
| -p              | If you need ports exposed `-p 80:80`                                                                        |
| --name          | Better way to view your container instead of getting the ID of the container in `docker ps`                 |
| `image`         | Image you want always goes last on the command line i.e `docker run -it --name my-container image:version`  |
| -rm             | Clean up container and files as if it never ran                                                             |
| --entrypoint="" | Here we can change the entry point to something that will stall the container `["tail", "-f", "/dev/null"]` |
| --mount         | Set a bind of the current directory                                                                         |
| -w              | Set a working directory                                                                                     |

```bash
docker run -it -d --rm --name temp-container --mount type=bind,source="$(pwd)",target=/code -w /code --entrypoint "tail -f /dev/null" python
```