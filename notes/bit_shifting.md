# Basic Bitwise Operations
## AND / & 
Logical AND operations are awesome for extracting the sections of your bit steam. This is why it is used with a mask in order to "zero out" the sections that you do not need.
```
[10011]011   # in brackets is the oportion we want
[11111]000   # Create a mask with 0 in the places you do not want
----------
10011 000   
```

## OR / |
Logical OR operations are great for applying new values to your stream. Say we have a bit in the third position that you would like to set without affecting the rest of your stream. You can create a steam that you can OR to your original stream.
```
11011010   # We want to manipulate the third bit
00100000   # Create a mask that only affects that bit and OR it
--------

```
