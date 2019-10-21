# Personal shortcuts for using TMUX
## Combo: CTRL + b - Calling combo super

### Misc
| Binding | Description |
| ---- | ---- | 
| `super + [` | Allows you to scroll through the terminal output. Press q to exit the mode |

### Window Management
| Binding | Description |
| ---- | ---- | 
| `super + "` | Split windows horizontally | 
| `super + %` | Split windows vertically |
| `super + <arrow>` | Switch between panes |
| `super<hold> + <arrow>` | Resize the pane |
| `super + n` | Cycle through the windows |
| `super + p` | Cycle in reverse through the windows |

# Tmux Configurations
## Source tmix
```
tmux source-file ~/.tmux.conf
```
### Change binding
```
unbind C-b
set -g prefix C-a
```
