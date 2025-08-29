inp = input()
arr = inp.split()
A = int(arr[0])
B = int(arr[1])
prod = 1
for x in range(A, B + 1, A):
    prod *= x
print(prod)
