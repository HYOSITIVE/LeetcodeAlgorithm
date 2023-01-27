def solution(numbers, target):
    answer = 0
    queue = [[numbers[0], 0], [-1 * numbers[0], 0]] # 첫 원소를 +하는 경우, -하는 경우 모두 존재
    n = len(numbers)
    while queue:
        temp, idx = queue.pop() # temp는 현재 값. idx는 몇 번의 연산이 진행되었는지
        idx += 1
        if idx < n:
            # 원소를 더하는 경우와 빼는 경우가 존재
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer