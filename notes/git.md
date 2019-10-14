[Git Basics](#1)  
[Git Branches](#2)  
[Merge with master](#3)

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
| `git status` | Tells you what branch you are in and status of files | 
| `git checkout <branch>` | Checks out a branch you have already created | 

### Merge with master {#3}
---
| Command | Description |
| ----------- | ----------- |
| `git checkout master` | Check out the branch you want to merge into |
| `git merge <branch>` | Merges branch specified with the branch you are currently on |



### Force git pull
----
[Source](https://stackoverflow.com/questions/1125968/how-do-i-force-git-pull-to-overwrite-local-files)
```
git fetch --all
git reset --hard <remote>/<branch>
```

