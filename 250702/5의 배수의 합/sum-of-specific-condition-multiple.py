inp = input()
arr = list(map(int, inp.split()))
sorted_arr = sorted(arr)  # 새로운 정렬된 배열 생성
C = arr[0]
D = arr[1]

A = sorted_arr[0]
B = sorted_arr[1]
sum_val=0

# print(f"{C}, {D}, {A}, {B}")


for i in range(A, B+1):
    if i%5==0:
        sum_val+=i
print(sum_val)