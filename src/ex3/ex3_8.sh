#!/bin/sh

if [ -f "DB.txt" ]; then
    echo "$1 $2" >> DB.txt
else
    echo "$1 $2" > DB.txt
fi

exit 0
