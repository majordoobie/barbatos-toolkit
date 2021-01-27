# VSC-Setup
## Plugins to install
- Python by Microsoft
- Python Docstrings
- Trailing Spaces
- Better Comments
    - `*` Highlight
    - `!` Alerts
    - `?` Queries
    - `TODO:` todo
- Djanerio
- `python3 -m pip install pyling`
- GitLens
- Remote
- Path Intelligence
- Visual Studio Intellicod
- pylance

## settings.json
```json
{
    "editor.suggestSelection": "first",
    "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
    "window.zoomLevel": 1,
    "terminal.integrated.fontFamily": "'Source Code Pro for Powerline', 'Hack Nerd Font'",
    "files.autoSave": "afterDelay",
    "files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/.hg": true,
        "**/CVS": true,
        "**/.DS_Store": true,
        ".archive2/" : true,
        ".venv*" : true,
        ".vscode" : true,
        ".pylintrc" : true
    }
}
```









---
## Metadata
- `tags`: #cybernetic #env 
- `Title`: VSC-Setup
- `Created`: [[2021-01-22]] 11:38

==References==
- [The Ultimate Visual Studio Code Setup For Django Developers | Django Central](https://djangocentral.com/visual-studio-code-setup-for-django-developers/)
- [Top 20 Best Visual Studio Code Extensions For Programmers](https://www.ubuntupit.com/best-visual-studio-code-extensions-for-programmers/)