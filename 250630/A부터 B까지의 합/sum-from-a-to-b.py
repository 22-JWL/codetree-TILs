sum_val = 0
inp = input()
arr = inp.split()
A = int(arr[0])
B = int(arr[1])

for i in range(A, B+1):
    sum_val += i
print(sum_val)

