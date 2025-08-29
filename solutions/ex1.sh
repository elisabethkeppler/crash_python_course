#!/bin/bash

# storing current working directory

orig_dir=$(pwd)

# naming the new working directory

newdir="bandpass_EKeppler"

mkdir "$newdir"
cp bandpasses/* "$newdir"

echo "copied all bandpass files into new '$newdir' directory"

# finding and counting file extensions

echo "list of bandpass extensions and the number of occurencies of each:"

for file in *; do
	ext="${file##*.}"
	echo "$ext"
done | sort | uniq -c

echo "-----------------"

# renaming all files

for file in *; do
	if grep -qi "photons" "$file"; then
		type="photons"
	elif grep -qi "energy" "$file"; then
		type="energy"
	else
		echo "no filter type in file $file"
		continue
	fi

	filtername="${file%.*}"	# file name without extension
	newname="${filtername}.${type}.filt"	# builds the new name
	
	# renaming the file
	mv "$file" "$newname"
	echo "Renamed '$file' -> '$newname'"
done

echo "Finished renaming all files"

# returning to the original working directory

cd "$orig_dir" || exit
