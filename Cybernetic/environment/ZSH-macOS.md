
# ZSH-macOS
- The [Kevin-Smets Repo](https://gist.github.com/kevin-smets/8568070) repo has all you need to install oh-my-zsh which is the package manager for zsh that we are using.

## Plugin format
The format for adding plugins is to not have any commas in the array
```bash
plugins=(
    git
    zsh-autosuggestions
    docker
    osx
)
```

## Fixing paths
```
vim ~/.p10k.zsh
typeset -g POWERLEVEL9K_DIR_MAX_LENGTH=0
source ~/.p10k.zsh
```

## Plugins
- [auto suggestion](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#oh-my-zsh)
- [syntax highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)
- osx (Already available)
- docker (already available)

## Installing fonts on windows
```
# Install fonts
## For windows
https://github.com/ryanoasis/nerd-fonts#patched-fonts
### Pick font download both windows comptaible ones i.e:
https://github.com/ryanoasis/nerd-fonts/blob/master/patched-fonts/Go-Mono/Regular/complete/Go%20Mono%20Nerd%20Font%20Complete%20Mono%20Windows%20Compatible.ttf
### Set windows terminal with the same family
{
	"fontFace": "GoMono NF"
}
```

## Install fonts on nix
```
mkdir -p ~/.local/share/fonts
cd ~/.local/share/fonts && curl -fLo "Droid Sans Mono for Powerline Nerd Font Complete.otf" https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/DroidSansMono/complete/Droid%20Sans%20Mono%20Nerd%20Font%20Complete.otf
```




---
## Metadata
- `tags`: #cybernetic #env
- `Title`: ZSH-macOS
- `Created`: [[2021-01-22]] 09:42

==References==
- [Kevin-Smets Repo](https://gist.github.com/kevin-smets/8568070)
- [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#oh-my-zsh)