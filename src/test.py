import random

print("안내면 진다 가위바위보")
data=input("가위 바위 보 셋 중 하나를 입력하시오. >> ")

rcp=['가위','바위','보']
user=random.choice(rcp)

print(user)

if data=='가위' and user=='가위':
    print('비겼습니다. ')
elif data=='가위' and user=="보":
    print('이겼습니다. ')
elif data=='가위' and user=='바위':
    print("졌습니다. ")
elif data=='보' and user=='보':
    print("비겼습니다.")
elif data=='보' and user=="바위":
    print('이겼습니다. ')
elif data=='보' and user=='가위':
    print("졌습니다. ")
elif data=='바위' and user=='바위':
    print("비겼습니다.")
elif data=='바위' and user=='보':
    print("졌습니다.")
elif data=='바위' and user=='가위':
    print("이겼습니다.") 
else:
    print("다시 시도하시오.")   