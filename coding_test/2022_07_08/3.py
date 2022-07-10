# https://golangexample.com/abag-go-task/


def is_aesthetically_pleasing(A):
    if A[0] == A[1]:
        return 0

    cur = A[1]
    checker = A[0] > A[1]
    for i in range(2, len(A)):
        this = cur >= A[i]
        if this != checker:
            checker = this
        else:
            return 0
        cur = A[i]
    return 1


# cut only one tree
def get_list(A, x):
    lst = []
    for i in range(len(A)):
        if i != x:
            lst.append(A[i])
    return lst


def solution(A):
    res = is_aesthetically_pleasing(A)
    if res == 1:
        return 0

    for i in range(len(A)):
        lst = get_list(A, i)
        res += is_aesthetically_pleasing(lst)

    return res if res != 0 else -1
