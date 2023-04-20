up::[[Root]]
Tags:: #code #guides #env 
# Setting up MacOS

## Setting Space Shortcut
For spaces to automatically be created you have to enable the keyboard shortcut for the space to be moved `ctrl + #`

First, create all the spaces you want to be persistent. Pick 10

Then to enable, go to Settings -> Keyboard Shortcuts -> Mission Control [^1]
![[Pasted image 20230413170827.png]]

## Setting Sticky App
You can assign an app to a space by opening the app, and clicking on "assign to desktop"
![[Pasted image 20230413173240.png]]

## Tiling Window Manager Yabai
Yabai ^[https://github.com/koekeishiya/yabai] is a window manager for macOS. It uses its own daemon to monitor for keyboard shortcuts to activate yabai functions. A neat thing about it is that yabai can use Brew Services ^[https://github.com/Homebrew/homebrew-services] to manage the two daemons for you. 

### Yabai Tutorial
The following tutorial is from a YouTuber named [Josean Martinez](https://youtu.be/k94qImbFKWE) ^[https://youtu.be/k94qImbFKWE] ^[https://github.com/josean-dev/dev-environment-files] ^[https://www.josean.com/posts/yabai-setup]


## Setting up zsh
### Install oh-my-zsh on macOS
```bash
xcode-select —-install

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
With oh-my-zsh installed, you can now install the best theme
```bash
git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k 

vim ~/.zshrc 

ZSH_THEME="powerlevel10k/powerlevel10k" 

source ~/.zshrc #this will promot p10k configure
```


### Plugins to install
Plugins must be installed into the `oh-my-zsh` custom folder for them to be seen by the framework. To activate them, you just modify the `~/.zshrc` 

#### Built-in Plugins
##### sudo ^[https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/sudo]
The sudo plugin allows you to run the previous failed command with sudo kinda like how bash allows you to do `$$` In this case, once you fail the command, you just type `sudo` and the previous command is populated automatically
```bash
netstat -pantu
sudo
```

##### Copyfile ^[https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/copyfile]
The `copyfile` plugin allows you to copy the contents of a file to your clipboard. This can be use in place of something like cat
```bash
copyfile ~/.zshrc
```

##### jsontools ^[https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/jsontools]
This plugin allows you to pipe json payloads to make them look prety
```bash
curl endpoint.com | pp_json
```
##### macos ^[https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/macos]
This plugin provides a few utilities to interact between the terminal and finder app
![[Pasted image 20230420124153.png]]
![[Pasted image 20230420124208.png]]

##### docker
Plugin provides auto completion but it does not working with "stacking"

```bash
# zsh-autocomplete
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions



git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions 

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting 

git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/plugins/zsh-completions 

git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git \
  ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting

plugins=( 
	# Build in
	sudo
	copyfile
	docker
	macos
	jsontools

	# Third party
	zsh-autosuggestions
 
	git 
	vi-mode

)
```

        zsh-autosuggestions zsh-syntax-highlighting fast-syntax-highlighting zsh-autocomplete




---
# Resources

[^1]: https://appleinsider.com/articles/18/10/12/how-to-use-spaces-apples-mostly-ignored-macos-mojave-productivity-feature
