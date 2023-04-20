up:: [[Root]]
Tags:: #code #guides 
# Working With Obsidian

## Setting up Git
- Create your repo, push it to target, then use the git plugin to sync it.
- You will probably see an error like this:
![[Pasted image 20230412210842.png]]

You can use the following git config command to change the CRLF settings ^[ https://github.com/denolehov/obsidian-git/issues/37]


```bash
# Replace all CR+LF with LF (keeping dates unchanged)
find .obsidian/plugins -type f | xargs dos2unix -k

git config --global core.autocrlf inp/ut
```

## Footnotes
Footnotes were a bitch when I started to use them. The biggest takeaway is to make sure that you are viewing the results from `cmd + e`

The format is simple too:
```bash
# Inline
^[Inline footnote]

# Not in line
[^Tag]

[^Tag]: Description of it
```

## Using Annotator
The annotator plugin is awesome, just a bit hard to use at times. The biggest takeaway is that the  metadata syntax has to go on top as specified in the metadata docks ^[https://help.obsidian.md/Editing+and+formatting/Metadata]

```
--- 
annotation-target: assets/pdfs/doc.pdf
---
```

## Syncing with iOS 
We are using OneDrive to sync the notes so that we can see the notes in windows. To ge the notes in iOS you would need to either use the obsidian sync or iCloud. But those two options interfere with OneDrive. The alternative is using git and setting up automations to automatically run the pull/push. ^[https://meganesulli.com/blog/sync-obsidian-vault-iphone-ipad/]


Related:

---
# Resources
- [Obsidian Docs](https://help.obsidian.md/Obsidian/Index)
