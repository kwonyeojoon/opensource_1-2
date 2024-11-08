#!/bin/sh

read file_name

if [ ! -d "$file_name" ]; then
    mkdir "$file_name"
fi

cd "$file_name"

for i in 0 1 2 3 4
do
    touch "file$i.txt"
done

for i in 0 1 2 3 4
do
    mkdir -p "file$i"
    ln -s "../file$i.txt" "file$i/file$i.txt"
done

exit 0
