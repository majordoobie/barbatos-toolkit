up:: 
Tags:: #code #howto  
Related::
=======
---
parent file:
  - "[[Published]]"
related: 
creation data: 2020-12-05, 07:11
tags:
  - "#guides"
  - "#os"
---
# MacOS Commands





---
# Resources
 `[Example](Link)`
 `[^Example]: Link    || [^Example]`
 

# System Commands 
### scutil
`scutil` is a binary that is used to configure settings via the terminal. It can also be used to retrieve information about the NIC

| Command        | Description                   |
| -------------- | ----------------------------- |
| `scutil -r`    | Check if network is reachable |
| `scutil --nwi`  | Show network information      |
| `scutil --dns`  | Show DNS information          |
| `scutil --dns` | Show DNS information                              |

### Netstat

| Command                    | Description                                 |
| -------------------------- | ------------------------------------------- |
| `netstat -naf inet`        | Base command is similar to `netstat -pantu` |
| `netstat -naf inet -p tcp` | Can provide a protocol option. Works better than grep       |

### lsof

| Command                     | Description                                                               |
| --------------------------- | ------------------------------------------------------------------------- |
| `lsof -nP`                  | Base command used to show the integer representation of ports and address |
| `lsof -np -i`               | Show networking descriptors only                                          |
| `lsof -nP -i <opts>`        | `[46][protocol][@hostname|hostaddr][:service|port]`                       |
| `lsof -nP -iTCP`            | Only show TCP                                                             |
| `lsof -nP -iTCP:22`         | Only show TCP on port 22                                                  |
| `lsof -nP -i@8.8.8.8`       | Only show output with quad 8 involved                                     |
| `lsof -nP -iTCP@8.8.8.8:80` | Only show output with quad 8 on port 80                                   |

### ps

| Command                              | Description                                                  |
| ------------------------------------ | ------------------------------------------------------------ |
| `ps -ax`                             | This is the base command to show all processes on the system |
| `ps -axc`                            | Remove the full path of the command and only show the binary |
| `ps -axE`                            | Show the environment variables set for the commands ran      |
| `ps -axwwwo user,pid,ppid,%cpu,comm` | Closes I can get to the linux output                         |                                     |                                                              |





---
# Resources
