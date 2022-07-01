# test : 신고 결과 받기
# link : https://programmers.co.kr/learn/courses/30/lessons/72410


def solution(id_list: list[str], report: list[str], k: int):
    r_distinct = list(map(lambda x: x.split(), set(report)))
    reported = {i: 0 for i in id_list}

    for i in r_distinct:
        reported[i[1]] += 1

    ans = {i: 0 for i in id_list}
    for i, j in r_distinct:
        if reported[j] >= k:
            ans[i] += 1

    return list(ans.values())
