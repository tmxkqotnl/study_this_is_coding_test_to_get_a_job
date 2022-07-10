# https://leetcode.com/problems/largest-magic-square/

def is_square_magic(s,N,M,cur):
    r = 2
    size = 0
    while r+cur[0] <= N and r+cur[1] <= M:
        temp = list(map(lambda x:x[cur[1]:cur[1]+r], s[cur[0]:cur[0]+r])) # fix, refac
        
        h = [sum(x) for x in temp]
        v = [sum(x) for x in zip(*temp)]
        
        d = [[temp[x][x] for x in range(r)]]
        d.append([temp[x][r-x-1] for x in range(r)])
        d = [sum(x) for x in d]
        
        if len(set([*h,*v,*d])) == 1:
            size = r
        r+=1

    return size
        

def solution(A):
    N,M = len(A), len(A[0])

    ans = 1
    for i in range(N-1):
        for j in range(M-1):
            ans = max(is_square_magic(A,N,M,(i,j)),ans)

    return ans


