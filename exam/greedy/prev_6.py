def solution(food_times, k):  # 시간초과(효율성)
    food_times = [[food_times[i], i + 1] for i in range(len(food_times))]

    cur = 0
    for _ in range(k):
        food_times[cur][0] -= 1

        if food_times[cur][0] == 0:
            food_times.pop(cur)
            if not food_times:
                return -1
        else:
            cur += 1

        if cur >= food_times.__len__():
            cur = 0
    return food_times[cur][1]
