#break
#:현재 속한 반복문을 벗어나는 키워드

# 무한반복
# : 무조건 계속 반복하는 반복문
# *반드시, 종료조건을 넣어주어야 한다.

while True:
    shop=input("내가 좋아하는 가게는?")
    #종료조건
    if shop=="맥도날드":
        print("정답입니다")
        break
    else:
        print("틀렸습니다")
        