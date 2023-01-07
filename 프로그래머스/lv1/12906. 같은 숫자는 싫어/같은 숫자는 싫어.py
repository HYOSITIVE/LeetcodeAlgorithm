def solution(arr):
    previous = -1;
    answer = []
    for elem in arr:
        if elem != previous:
            answer.append(elem)
        previous = elem
   
    print('Hello Python')
    return answer