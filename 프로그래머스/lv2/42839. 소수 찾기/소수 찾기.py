from itertools import permutations

def is_prime_number(x) :
    if x < 2 :
        return False
    
    for i in range(2, x) :
        if x % i == 0 :
            return False
            
    return True


def solution(numbers):
    numbers = [n for n in numbers] # numbers를 자릿수 분리
    combinations = []
    candidates = []
    answer = 0
    
    for i in range(1, len(numbers) + 1):
        # 배열의 길이보다 작거나 같은 모든 크기의 수 조합 획득
        combinations.append(list(set(map(''.join, permutations(numbers, i)))))
    candidates = list(set(map(int, set(sum(combinations, [])))))
    
    # 소수 여부 검증
    for candidate in candidates:
        if is_prime_number(candidate) == True:
            answer += 1
    return answer