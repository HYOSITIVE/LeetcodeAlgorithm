def solution(my_string, target):
    for i in range(0, len(my_string)):
        if (my_string[i:len(my_string)].startswith(target)):
            return 1
    return 0