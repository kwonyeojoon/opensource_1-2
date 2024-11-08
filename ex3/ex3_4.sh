#!/bin/sh

echo "리눅스가 재미있나요? (yes / no)"
read answer

case $answer in
    [Yy]* | [Yy][Ee][Ss]*)
        echo "yes" ;;
    [Nn]* | [Nn][Oo]*)
        echo "no" ;;
    *)
        echo "yes or no 로 입력해주세요." ;;
esac

exit 0
