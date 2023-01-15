def solution(s):
    answer = False
    
    parentheses = []
    for parenthesis in s:
        if parenthesis == '(':
            parentheses.append(parenthesis)
        elif parenthesis == ')':
            if (len(parentheses) == 0):
                return False
            else:
                parentheses.pop()
            
    if len(parentheses) == 0:
        answer = True

    return answer