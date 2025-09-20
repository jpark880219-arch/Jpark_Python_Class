#가위바위보게임
#컴퓨터: 가위바위보를 랜덤으로 선택
#나: 가위바위보를 입력
#내가 질때까지 게임을 계속 진행
import random
choices=["가위","바위","보"]
user=""
win="true" #내가 이겼는지

while win:
    computer=random.choice(choices)
    user=input("가위 바위 보 입력")
    print("컴퓨터 : {}".format(computer))
    
    #이겼을때
    win1=(user=="가위"and computer=="보")
    win2=(user=="바위"and computer=="가위")
    win3=(user=="보"and computer=="바위")
    
    if user==computer:
        print("비겼습니다!")
    elif win1 or win2 or win3:
        print("이겼습니다!")
    else:
        print("졌습니다!")



