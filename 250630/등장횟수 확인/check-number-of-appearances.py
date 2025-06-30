cnt = 0
arr = []
for _ in range(5):
    N = int(input())
    arr.append(N)
    
    if N%2==0:
        cnt += 1
print(cnt)

