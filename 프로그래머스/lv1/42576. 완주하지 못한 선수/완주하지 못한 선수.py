import collections

def solution(participant, completion):
    # Counter 객체는 각 요소들과 요소들의 개수를 짝지어서 가지고 있음
    answer = collections.Counter(participant) - collections.Counter(completion) # 뺄셈을 진행하면, answer에는 한 개의 원소만 남음
    return list(answer.keys())[0]
    return answer