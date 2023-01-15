def solution(n, lost, reserve):
    realReserve = list(set(reserve) - set(lost))
    realLost = list(set(lost) - set(reserve))
    answer = n - len(realLost)
    realReserve.sort()
    realLost.sort()
    for goodStudent in realReserve:
        if (goodStudent - 1) in realLost or (goodStudent + 1)  in realLost:
            answer += 1
            if (goodStudent - 1) in realLost:
                realLost.remove(goodStudent - 1)
            else:
                realLost.remove(goodStudent + 1)
    return answer