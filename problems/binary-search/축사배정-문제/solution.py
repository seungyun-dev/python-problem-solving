```
def f(lst, d): # 배치 알고리즘
    cnt = 1
    p = 0
    mini = max(x)-min(x)
    #print(lst[p])
    while cnt<c:
        for i in range(1, d+1):
            if p+i < n:
                if lst[p+i] - lst[p] >= d:
                    cnt += 1
                    mini = min(lst[p+i] - lst[p], mini)
                    p += i
                    #print(lst[p])
                    break
            elif cnt < c:
                return 0
        
    return mini


n, c = map(int, input().split())

x = []
for i in range(n):
    x.append(int(input()))


x.sort()

# print(f(x, 3))
start, end = 1, max(x)-min(x)

while start <= end: # D에 대한 이진 탐색
    mid = (start+end)//2
    
    if f(x, mid):
        start = mid+1
        s = mid
    else:
        end = mid-1

print(s)
```
