#!/bin/sh

read number

if echo "$number" | grep -Eq '^[0-9]+$'; then
    i=1
    while [ "$i" -le "$number" ]; do
        echo "hello world"
        i=`expr $i + 1`
    done
else
    echo "정수를 입력하세요."
fi

exit 0
