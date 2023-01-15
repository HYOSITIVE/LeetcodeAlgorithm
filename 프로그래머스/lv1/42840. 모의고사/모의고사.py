def solution(answers):
    answer = []
    routine1 = [1, 2, 3, 4, 5]
    routine2 = [2, 1, 2, 3, 2, 4, 2, 5]
    routine3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = {1 : 0, 2 : 0, 3 : 0}
    
    for i in range(len(answers)):
        if answers[i] == routine1[i % len(routine1)]:
            scores[1] += 1
        if answers[i] == routine2[i % len(routine2)]:
            scores[2] += 1
        if answers[i] == routine3[i % len(routine3)]:
            scores[3] += 1
    sortedScores = (sorted(scores.items(), reverse=True, key=lambda x: x[1]))
    answer.append(sortedScores[0][0])
    if sortedScores[1][1] == sortedScores[0][1]:
        answer.append(sortedScores[1][0])
    if sortedScores[2][1] == sortedScores[0][1]:
        answer.append(sortedScores[2][0])
    
    return answer