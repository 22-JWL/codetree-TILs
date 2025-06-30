N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
sum_val = 0

for i in range(N):
    temp = int(arr[i])
    if temp%2==1 and temp%3 == 0:
        sum_val += temp
print(sum_val)

