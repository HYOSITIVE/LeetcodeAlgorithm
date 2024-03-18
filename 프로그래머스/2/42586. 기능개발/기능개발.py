import math

def solution(progresses, speeds):
    answer = []

    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    index = 0

    for i in range(len(days)) :
        if days[index] < days[i] :      # 현재 인덱스의 작업일보다 큰 작업일이 나오면
            answer.append(i - index)    # 둘의 차이(배포 개수)를 추가 
            index = i
    answer.append(len(days) - index)    # 갱신된 인덱스부터 마지막 인덱스까지의 개수
    return answer