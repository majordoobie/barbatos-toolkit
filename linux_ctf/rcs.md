# ~/.bashrc
```
# Color variables
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

# Functions
# Determine git branch.
parse_git_branch() {
 git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

# added by Anaconda3 5.0.1 installer
# export PATH="/Users/anker/anaconda3/bin:$PATH"  # commented out by conda initialize

# make ls use colors
export CLICOLOR=1
alias ls='ls -Fa'
alias ll='ls -laht'
alias cp='cp -iv'
alias mv='mv -iv'
alias mkdir='mkdir -pv'

# Check biggest hog
alias cpu_hogs='ps wwaxr -o pid,stat,%cpu,time,command | head -10'

#export PS1="________________________________________________________________________________\n| \w @ \h (\u) \n| => "
#export PS2="| => "


#set your prompt
#export PS1="\n$C_LIGHTGREEN\u$C_DARKGRAY@$C_BLUEDRAGON $C_DARKGRAY: $C_LIGHTYELLOW\w\n$C_DARKGRAY\$$C_DEFAULT "
export PS1="\n$C_BLUE\u$C_DARKGRAY$C_DARKGRAY: $C_LIGHTYELLOW\w\n$C_DARKGRAY\$$C_DEFAULT "

export PATH="/usr/local/opt/jpeg-turbo/bin:$PATH"
export PATH="/usr/local/opt/gettext/bin:$PATH"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/anker/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/anker/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/anker/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/anker/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```