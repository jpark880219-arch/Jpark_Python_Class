#퀴즈 프로그램
quiz={
    1:{
        "question": "순서가 없고 중복 불가능한 컬렉션은?",
        "choice":["1.리스트","2.튜플","3.세트","4.딕셔너리"]
    },
    2:{
        "question": "다음중 파이썬의 반복문은",
        "choice":["1.break","2.repeat","3.cycle","4.while"]
    },
    3:{
        "question": "다음중 기타제어문은?",
        "choice": ["1.brake","2.break","3.break dance","4.break time"]
    },
}

answer = {
    1: 3,
    2: 4,
    3: 2
}

score=0
# for key, value in 딕셔너리.items():
for no, content in quiz.items():
    #1. 문제
    print("{}.{}".format(no,content["question"]))
    
    #보기
    for choice in content["choice"] :
        print(""+choice)
        
    #답안입력
    user=input("답:")
    
    #정답확인
    if int(user)==answer[no]:
        print("정답입니다!")
        score=score+10
    else:
        print("틀렸습니다. 정답은{}번 입니다".format(answer[no]))
        
print("점수는{} 점 입니다".format(score))