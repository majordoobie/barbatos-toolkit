#!/bin/bash
  
DIR="/Users/anker/OneDrive/root/Documents/test_dir"

for file in $DIR/*; do
    # Check if the file is a file
    [ -e "$file" ] || continue
        # Grab the last section of the string split by /
        file=${file##*/}
        # Split the underscore
        file=`echo $file | cut -d _ -f 1`
        # Regex for grabbing the characters we want; you would use C
        file=`expr "$file" : '^\([J][0-9]*\)'`
        # Make sure the string is not empty
        if [ -n "$file" ]; then
            case $file in
                J0)
                    echo "${file} matches 192.168.2.1"
                    if [ ! -d "$DIR/192.168.1.1" ]; then
                        mkdir $DIR/192.168.1.1
                    fi
                    ;;
                J11)
                    echo "${file} matches 192.168.4.1"
                    if [ ! -d "$DIR/192.168.4.1" ]; then
                        mkdir $DIR/192.168.4.1
                    fi
                    ;;
                *)
                    echo "${file} did not match any IP"
                    ;;
            esac
        fi
done
