n, m = map(int, input().split())

k = []
for i in range(m):
    k.append(int(input()))

start, end = 1, max(k)

r = 0
while start <= end: # 이진 탐색
    mid = (start+end)//2
    
    p = 0 # 
    for i in k:
        p += i//mid 
        if i % mid > 0: # 헷갈렸던 부분
            p += 1
    if p <= n: # 헷갈렸던 부분
        end = mid-1
        r = mid
    else:
        start = mid+1

print(r)
