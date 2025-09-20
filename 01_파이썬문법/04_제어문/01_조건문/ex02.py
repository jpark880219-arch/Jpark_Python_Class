# 다중 조건문
# - 위의 나온 조건이 만족하지 않을때,(if)
# 아래의 조건을 확인하고(elif)
# 모두 만족하지 않으면 else문을 실행한다

score=input("성적:")
score=int(score)

if score>=90:
    print("a")
elif score>=80:
    print("b")
elif score>=70:
    print("c")
elif score>=60:
    print("d")
else:
    print("f")
    