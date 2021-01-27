# Additional aliases and exports for bashrc
## Modify .bashrc to check for the extention file
```
[ -f "$HOME/.bash_aliases" ] && source "$HOME/.bash_aliases"
```
## Modify VSC to use WSL
```
"terminal.integrated.shell.windows" : "C:\\Windows\\System32\\bash.exe"
```
## Now add your stuff to .bash_aliases
```
# COLORS
C_DEFAULT="\[\033[m\]"
C_WHITE="\[\033[1m\]"
C_BLACK="\[\033[30m\]"
C_RED="\[\033[31m\]"
C_GREEN="\[\033[32m\]"
C_YELLOW="\[\033[33m\]"
C_BLUE="\[\033[34m\]"
C_PURPLE="\[\033[35m\]"
C_CYAN="\[\033[36m\]"
C_LIGHTGRAY="\[\033[37m\]"
C_DARKGRAY="\[\033[1;30m\]"
C_LIGHTRED="\[\033[1;31m\]"
C_LIGHTGREEN="\[\033[1;32m\]"
C_LIGHTYELLOW="\[\033[1;33m\]"
C_LIGHTBLUE="\[\033[1;34m\]"
C_LIGHTPURPLE="\[\033[1;35m\]"
C_LIGHTCYAN="\[\033[1;36m\]"
C_BG_BLACK="\[\033[40m\]"
C_BG_RED="\[\033[41m\]"
C_BG_GREEN="\[\033[42m\]"
C_BG_YELLOW="\[\033[43m\]"
C_BG_BLUE="\[\033[44m\]"
C_BG_PURPLE="\[\033[45m\]"
C_BG_CYAN="\[\033[46m\]"
C_BG_LIGHTGRAY="\[\033[47m\]"

# FUNCTIONS
## Provide the branch name in the terminal
parse_git_branch() {
 git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

# TERMINAL MODS
## Change size of buffer
HISTSIZE=50000
HISTFILESIZE=50000

## PS prompt
PS1="\n$C_BLUE\u$C_DARKGRAY$C_DARKGRAY: $C_LIGHTYELLOW\w\n\$(parse_git_branch)$C_DARKGRAY[\t]\$$C_DEFAULT "

# Set default location
cd /mnt/c/Users/SgtMa/OneDrive/root/Cyberdomains/coding/

## Enable bash completion.
[ -f /etc/bash_completion ] && . /etc/bash_completion

## Improve output of less for binary files.
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# EXPORTS
## Make WSL connect to Docker running on windows
export DOCKER_HOST=tcp://localhost:2375

# ALIASES
alias ls='ls -Fa'
alias ll='ls -laht'
alias cp='cp -iv'
alias mv='mv -iv'
alias mkdir='mkdir -pv'
```