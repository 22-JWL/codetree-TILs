inp = input()
arr = inp.split()
arr.sort()
A = int(arr[0])
B = int(arr[1])
sum_val=0


for i in range(A, B+1):
    if i%5==0:
        sum_val+=i
print(sum_val)