# test : 행렬 테두리 회전하기
# link : https://programmers.co.kr/learn/courses/30/lessons/77485


def solution(rows: int, columns: int, queries: list[list[int]]) -> list[int]:
    matrix = [[0] * (columns + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[i][j] = (i - 1) * columns + j

    return [rotation(matrix, *i) for i in queries]


def rotation(matrix: list[list[int]], fx: int, fy: int, tx: int, ty: int) -> int:
    this_range = get_range(fx, fy, tx, ty)
    copied = [matrix[i][j] for i, j in this_range]

    for i in range(len(this_range)):
        try:
            matrix[this_range[i + 1][0]][this_range[i + 1][1]] = copied[i]
        except IndexError:
            matrix[this_range[0][0]][this_range[0][1]] = copied[i]

    return min(copied)


def get_range(fx: int, fy: int, tx: int, ty: int) -> list[tuple[int, int]]:
    coordinates: list[tuple[int, int]] = []
    # (fx,fy) ~ (fx,ty)
    for i in range(fy, ty + 1):
        coordinates.append((fx, i))
    # (fx,ty) ~ (tx,ty)
    for i in range(fx + 1, tx + 1):
        coordinates.append((i, ty))
    # (tx,ty) ~ (tx,fy)
    for i in range(ty - 1, fy - 1, -1):
        coordinates.append((tx, i))
    # (tx,ty) ~ (ft-1,fy)
    for i in range(tx - 1, fx, -1):
        coordinates.append((i, fy))

    return coordinates