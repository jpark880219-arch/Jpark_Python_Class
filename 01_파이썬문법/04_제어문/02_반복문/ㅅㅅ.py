import random
choices=["가위","바위","보"]
user=""
while user !="그만":
    computer=random.choice(choices)
    user=input("가위바위보 선택")
    print("컴퓨터는:{}".format(computer))
    print("나는 : {}".format(user))
    
