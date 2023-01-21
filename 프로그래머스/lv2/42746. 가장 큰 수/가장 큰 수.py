def solution(numbers):
    numbers = list(map(str, numbers)) # map을 돌면서 각 number들을 string으로 변경
    numbers.sort(key = lambda x: x * 3, reverse = True) # x: x * 3은 x를 3번씩 반복한다는 뜻. 자릿수 맞추기 위함
    return str(int(''.join(numbers))) # 구분자 없는 배열들을 join. number가 모두 0인 경우를 대비해 재변환
    
    return answer