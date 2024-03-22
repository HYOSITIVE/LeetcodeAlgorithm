from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque() # 큐 선언
    q.append([begin, 0]) # 시작 노드 큐에 삽입
    V = [0] * (len(words)) # Visited 배열
    
    while q:
        word, count = q.popleft()
        if word == target: # 단어 찾으면 거리 리턴
            answer = count
            break
        for i in range (len(words)): # 모든 단어 순회
            temp_count = 0
            if not V[i]: # visited가 아니면
                for j in range(len(word)):
                    if word[j] != words[i][j]: # 단어 비교
                        temp_count += 1
                if temp_count == 1: # 하나만 다르면, 인접이면
                    q.append([words[i], count + 1])
                    V[i] = 1 # 특정 단어(노드) visited 
    return answer