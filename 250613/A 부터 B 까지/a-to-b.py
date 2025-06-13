inp = input()
arr = inp.split()
A = int(arr[0])
B = int(arr[1])

while A<=B:
    print(A, end=' ')

    if A%2==0:
        A+=3
    else:
        A *=2