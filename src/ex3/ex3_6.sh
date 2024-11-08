#!/bin/sh

read folder_name

if [ ! -d "$folder_name" ]; then
    mkdir "$folder_name"
fi

cd "$folder_name"

for i in 0 1 2 3 4
do
    touch "file$i.txt"
done

tar -cf files.tar file0.txt file1.txt file2.txt file3.txt file4.txt

mkdir -p extracted_files
mv files.tar extracted_files/
ls extracted_files

cd extracted_files
tar -xvf files.tar

exit 0
