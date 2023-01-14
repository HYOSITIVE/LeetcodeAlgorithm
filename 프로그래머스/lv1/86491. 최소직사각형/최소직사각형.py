def solution(sizes):
    widths = []
    heights = []
    for size in sizes:
        # 1차적으로 모든 명함의 가로, 세로 길이를 배열에 삽입
        widths.append(size[0])
        heights.append(size[1])
    
    for i in range(len(sizes)):
        if (widths[i] < heights[i]):
            # 무조건 가로 길이가 더 길도록 설정
            temp = heights[i]
            heights[i] = widths[i]
            widths[i] = temp
        
    return max(widths) * max(heights)