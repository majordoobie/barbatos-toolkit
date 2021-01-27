# VIM-Notes
- Originated in 1976, VIM is designed to be a `modal`editor since it has "modes" that you enter and leave
- vim supports the following modes:

## Usage
### Modal Editing
- Normal `ESC`
- Insert `i`
- Replace `R`
- Visual : [ `v`, `V`, `<c-v>` ]

### Buffers
- Every "file"open in vim is called a buffer and you can also have tabs that can have their own windows.
- Vim maintains a set of open files, called “buffers”. A Vim session has a number of tabs, each of which has a number of windows (split panes). Each window shows a single buffer. Unlike other programs you are familiar with, like web browsers, there is not a 1-to-1 correspondence between buffers and windows; windows are merely views. A given buffer may be open in multiple windows, even within the same tab. This can be quite handy, for example, to view two different parts of a file at the same time.

### Basic Commands
Commands are given with the `:` key
![](attachments/Pasted%20image%2020210122115023.png)

### Help menu
- You can get to the help menu with `:help` you can also get help on topics with `:help <topic>` keep in mind that if you want help on a command such as `:w` you need to give that colon to it `:help :w`
- There is quickref in the help menu with `:help quickref` then you can jump from the table of contents to the topic with `<ctrl> + ]` you need to be at the beginning of the word for this to work


### Jumps
#### Basic Jumps
    `<ctrl> + d`       : Scroll down
    `<ctrl> + u`       : Scroll up
    `H M L`            : Highest, Middle, Lowest
    `gg`               : Move to the top of the file
    `G`                : Move to the bottom of the file
#### Advance Jumps
##### Scroll by braces
    `{ || }`          : Jump to next blank line
    `[{ || }]`        : Jumps between blocks
    `( || )`          : Jumps between sentences in most cases it will jump between parent braces                       it is unreliable 
    `[[ || ]]`        : Jumps between parent braces i.e. java classes within the same file
    `%`               : Jump between the brace in the current scope

##### Scroll by Char
    `f + char`        : Move to the char; Best used with brackets
    `t + char`        : Move before the char

##### Word Jumps
    `w`               : Jump forward by a word
    `b`               : Jump backwards by a word
    `e`               : Jump to the end of a word
##### Insert Jumps
    `o`               : Insert below position with respect to syntax formatting
    `O`               : Insert above position with respect to syntax formatting
    `I`               : Insert at the beginning of the line regardless of position within the line
    `A`               : Insert at the end of the line regardless of position; Best used for                           multi-line editing
##### Marker Jumps
    `m + char`        : Creates a jump marker at the cursor location using the char provided
    `' + char`        : Jumps to the beginning of the line of the marker set at char
    `btick + char`    : Jumps to the cursor position of the marker
    `''`              : Jumps to the previous location before jump

### Deleting and Editing Text
 #### Basic Delete and Change
    `dw`              : Deletes a word
    `cw`              : Changes the word (Delete + Insert)
    `c2w`             : Change the next two words
    `d2w`             : Delete the next two words
#### Advance delete and change
>    Small examples below but you can use them interchangeable be creative and think about what each char is doing with each other

    `%`               : Swap between brackets
    `ci[`             : Change Inside Open and Close Bracket
    `dt]`             : Delete all up to Close Bracket

### Advance Search
    # Select between ()
    v + i + (

    # Include ()
    v + a + (

    # Select by word
    v + w

    # Selecting with F
    v + f + char

### Forward slash search with regex
```
/ 			: Search for text
n			: Next find
N			: Previous find
```
> You can also apply regex
```
/appl.
/.pple
/$apple
```

- Moving between windows

    # between windows
    `<ctrl> ww`  — Keep toggling around in sequence
    `<ctrl> wj`  — Change down can also use the rest hjkl

- New Tabs

    ```bash
    # Create new tabs
    :tabnew 
    :tabnew filename

    # Save file when open
    :w filename

    # Move between tabs
    <ctrl> + PgDown/PgUp

    # Close tab
    :tabclose

    # Split window
    :split filename
    :vsplit filename

    # Cycle between windows
    <ctrl> + w + w
    ```

## Combos

### Multi-line edit

- Multi-line where you reside

    ```
    # Enter visual block mode
    <c-v>

    # Move selection up or down
    j or k

    # Enter multi edit mode
    <shift> + i

    # Escape to make changes
    <esc>
    ```

- Multi-line at then end of all lines

    ```
    # Enter visual block mode
    <c-v>

    # Move selection up or down
    j or k

    # Move to the end of the line
    $

    # Enter append mode
    <shift> + a

    # Escape to make changes
    <esc>
    ```

- Whole function delete

    ```bash
    # line highlight
    <SHIFT> + v
    # Move down if you have betore your brace
    j
    # Jump to bracket
    f {
    # Jump to end of matching brackey
    %
    ```

# Settings

- Indentation

    ```
    set tabstop=4
    set expandtab
    set softtabstop=4
    set shiftwidth=4
    filetype indent on
    ```

- Recommended settings by Cambridge University



---
## Metadata
- `tags`: #cybernetic
- `Title`: VIM-Notes
- `Created`: [[2021-01-22]] 11:46

==References==
- [Cambridge Notes](https://missing.csail.mit.edu/2020/editors/)
- [Cheat Sheet](http://paulrougieux.github.io/vim.html)
- [Advance Vim](https://advancedweb.hu/tips-on-window-management-in-vim/)