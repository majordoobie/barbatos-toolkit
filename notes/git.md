[Heading ID](#1)
[Heading 2](#2)

### Git basic {#1}
---
```
git init
git status
git remote add -t <branch> <url>
git add <files>
git commit -m <msg>
```
### Branches {#2}
---
| Command | Description |
| ----------- | ----------- |
| `git branch` | List branches |
| `git branch <branch>` | Create a new branch |  


### Force git pull
----
[Source](https://stackoverflow.com/questions/1125968/how-do-i-force-git-pull-to-overwrite-local-files)
```
git fetch --all
git reset --hard <remote>/<branch>
```

