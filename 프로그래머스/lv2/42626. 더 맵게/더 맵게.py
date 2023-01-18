import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0] >= K:
            break
        elif len(scoville) < 2:
            answer = -1
            break
        else:
            firstFood = heapq.heappop(scoville)
            secondFood = heapq.heappop(scoville)
            mixedFood = firstFood + 2 * secondFood
            heapq.heappush(scoville, mixedFood)
            answer += 1
    return answer