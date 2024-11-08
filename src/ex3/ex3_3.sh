#!/bin/sh

read weight length
a=10000

len=$(echo "scale=2; $length * $length / $a" | bc)
bmi=$(echo "scale=2; $weight / $len" | bc)

if echo "$bmi < 18.50" | bc -l | grep -q 1; then
    echo "저체중 입니다."
elif echo "$bmi <= 23.00 && $bmi >= 18.50" | bc -l | grep -q 1; then
    echo "정상체중 입니다."
else
    echo "과체중 입니다."
fi

exit 0
