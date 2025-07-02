N = int(input())
arr = []
sum_val = 0
cnt = 0
for i in range(N):
    arr.append(int(input()))
    sum_val += arr[i]
    cnt += 1
avg = sum_val/cnt
print(f"{sum_val} {avg:.1f}")