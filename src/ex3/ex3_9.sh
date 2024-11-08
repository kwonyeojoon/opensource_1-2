#!/bin/sh

name=$1

if [ -f "DB.txt" ]; then
    grep -i "$name" DB.txt
else
    echo "DB.txt 파일이 존재하지 않습니다."
fi

exit 0
