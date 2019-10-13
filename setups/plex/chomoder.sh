#!/bin/bash


MOVIES="/media/plex_ntfs_drive/MOVIES"
MARVEL="/media/plex_ntfs_drive/MARVEL"
DISNEY="/media/plex_ntfs_drive/DISNEY"
BUBS="/media/plex_ntfs_drive/BUBS"

for file in $BUBS/* $MOVIES/* $MARVEL/* $DISNEY/*
do
	[ -e "$file" ] 
	if [ ! $(stat -c %A "$file") = "drwxrwxrwx" ]
	then
		chmod 777 "$file"
		#echo "$file"
	fi
done
