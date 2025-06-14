N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
for i in range(N):

    temp = arr[i]
    if temp%2==1 and temp%3==0:
        print(temp)

