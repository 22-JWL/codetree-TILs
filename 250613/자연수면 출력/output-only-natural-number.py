inp = input()
arr = inp.split()
A = int(arr[0])
B = int(arr[1])

if A>=0:
    for _ in range(B):
        print(A, end='')
else:
    print(0)