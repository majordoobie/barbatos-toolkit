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
11111010
```
## XOR / ^
Logical XOR operations are great for creating unique masks. For example,you can use it to create a mask that extracts tha last 8 bits of an IP address to convert a stream back into dotted decimal.
```
10110111 10011011
11111111 00000000  # But 0s in places you want to keep
-----------------
01001000 10011011  # Apply your new mask back to the original using &

10110111 10011011
01001000 10011011 # apply mask with &
-----------------
00000000 10011011 # Now you extracted the last 8 bits!
```
## Shift / << >>
Shifts are useful for positioning your bits in the correct positions. For example. IP addresses are displayed in dotted decimal, but in binary they are just a single stream of 32 bits.

| Octet1 | Octet2 | Octet3 | Octet4 |
| ------ | ------ | ------ | ------ |
| 192    | 186    | 85     | 42     |
| 11000000 | 10111010 | 01010101 | 00101010 |

As shown above, each section of a IP is 8 bits. But when you put the stream of IPs together you get a 32 bit stream. Remeber that the first octet is 192 in decimal. If we were to extract that out and clear all other other bits we would have:
` 11000000 00000000 00000000 00000000` If we convert this binary stream into decimal we get `3221225472`.   

`192 != 3221225472`

It is important to realize that even though we do have 32 bits that represent a whole IP, we logically section off the stream into four sections each one representing a decimal value of `0 to 255`. So if we wanted to properly extract the first octet we would need to shift our bits to the right which drops those bits.
```
11000000 10111010 01010101 00101010 >> 24
----------------------------------
00000000 00000000 00000000 11000000 
```
Then to put your binary sections back together you would need to shift them to the proper location.
```
11000000 << 24
11000000 00000000 00000000 00000000

10111010 << 16
10111010 00000000 00000000

01010101 << 8
01010101 00000000

00101010

# Now we OR everything together to apply them.
11000000 00000000 00000000 00000000
00000000 10111010 00000000 00000000
00000000 00000000 01010101 00000000
00000000 00000000 00000000 00101010 OR
--------------------------------------
11000000 10111010 01010101 00101010 | 192.168.85.42
```




