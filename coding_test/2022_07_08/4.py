# https://www.chegg.com/homework-help/questions-and-answers/today-world-approaching-ecological-crisis-due-global-warming-sea-level-rising-time-amount--q85490467

def solution(S):
    if len(S) == 1:
        return -1
    
    ans = 0
    lst = [['H-H','TTT'],['-H','TT'],['H-','TT']]
    for f,t in lst:
        ans+=S.count(f)
        S = S.replace(f,t)

    return ans if S.find('H')<0 else -1