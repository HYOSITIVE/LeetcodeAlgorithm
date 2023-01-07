def solution(array, commands):
    answer = []
    for command in commands:
        slicedArray = array[command[0] - 1:command[1]]
        slicedArray.sort()
        answer.append(slicedArray[command[2] - 1])
    return answer