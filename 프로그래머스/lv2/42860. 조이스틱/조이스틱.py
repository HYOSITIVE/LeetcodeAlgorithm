def solution(name):
    answer = 0
    cursor_gap = len(name) - 1 # A가 없을 경우 좌우 조이스탁 조작 횟수
    
    
    for index, letter in enumerate(name):
        # 알파벳 이동을 위한 상하 조이스틱 조작    
        alphabet_gap = min(ord(letter) - 65, 90 - ord(letter) + 1)
        answer += alphabet_gap
        
        # 커서 이동을 위한 좌우 조이스틱 조작
        next = index + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        cursor_gap = min([cursor_gap, 2 * index + len(name) - next, index + 2 * (len(name) - next)])
    answer += cursor_gap
    return answer
