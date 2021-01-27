# Get path to a binary
```
get-command <binary>
(get-command <binary>).Path
get-command <binary> | get-member
```
# Execution Policy
- You can retrieve the policy with 
```
get-executionpolicy
```
- Be default it will be set to restricted
- To change it you can set it
```
set-executionpolicy remotesigned -scope currentuser
```
# GCI foo
```
gci <path> | select-string -pattern <search>
```
# Archives
```
Expand-Archive
Compress-Archive
```