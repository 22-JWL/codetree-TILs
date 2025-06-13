inp = input()
arr = inp.split()
A = int(arr[0])
B = int(arr[1])

print(f"{A//B}.", end='')

A %= B

for _ in range(20):
    A *= 10
    print(A//B, end='')

    A %= B
