Commands needed:
| switch  | Description                                                                                                |
| ------- | ---------------------------------------------------------------------------------------------------------- |
| -d      | Detached Mode                                                                                              |
| -p      | If you need ports exposed `-p 80:80`                                                                       |
| --name  | Better way to view your container instead of getting the ID of the container in `docker ps`                |
| `image` | Image you want always goes last on the command line i.e `docker run -it --name my-container image:version` |
| -rm     | Clean up container and files as if it never ran                                                            |
|         |                                                                                                            |