
#* A -> B
def solution(A, B):
    count = 1
    cur = B
    
    while True:
        if cur == A:
            break
        if cur % 2 == 0:
            cur = cur // 2
            count += 1
        elif cur % 10 == 1 and cur > 10:
            cur = (cur - 1) // 10
            count += 1
        else:
            return -1
    return count 

from typing import List, Dict #* annotation -> 3.10 이상 
from typing import Union #* 낮은 버전

def solution(A:List[int], B:Dict[str, int]):
    B.get()
def solution(A:dict):
    A.get()
    
#* 컴백홈
from queue import Queue
#from collections import deque
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def solution(n, m):
    C = len(m[0])
    R = len(m)
    target = (0, C - 1)
    
    q = Queue()
    q.put((R - 1, 0, 1))
    count = 0
    while not q.empty():
        y, x, step = q.get()
        if (y, x) == target and step == n:
            count += 1
            continue
        if step > n:
            continue
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < C and 0 <= ny < R:
                if m[ny][nx] == '.':
                    q.put((ny, nx, step + 1))
            
    return count 

print(solution(6, ['....', '.T..', '....']) == 4)

#* 1, 2, 3 더하기 2
s = [4, 4, 4, 4]
order = [3, 5, 7, 8]
answer = ['1+2+1', '2+1+1', '3+1', -1]

def solution(s, order):
    arr = []
    count = 0
    result = []
    
    def dfs():
        nonlocal count
        sum_value = sum(arr)
        if sum_value == s:
            count += 1
            if count == order:
                result.append('+'.join(map(str, arr)))
                return
        
        if sum_value > s:
            return
        
        for i in range(1, 4):
            arr.append(i)
            dfs()
            arr.pop()
    dfs()
    
    if len(result) != 0:
        return result[0]
    else:
        return -1

for i in range(len(s)):
    print(solution(s[i], order[i]) == answer[i])
    