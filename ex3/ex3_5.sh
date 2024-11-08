#!/bin/sh

open_1() {
    echo "함수 안으로 들어왔음."
    ls $option
}

read option
echo "프로그램을 시작합니다."
open_1

exit 0
