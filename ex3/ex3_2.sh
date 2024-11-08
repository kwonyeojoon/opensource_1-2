#!/bin/sh

read num1 oper num2

if [ "$oper" = "+" ]; then
    result=`expr $num1 + $num2`
elif [ "$oper" = "-" ]; then
    result=`expr $num1 - $num2`
elif [ "$oper" = "*" ]; then
    result=`expr $num1 \* $num2`
elif [ "$oper" = "/" ]; then
    result=`expr $num1 / $num2`
else
    echo "지원하지 않는 연산자입니다."
    exit 1
fi

echo "$result"
exit 0
