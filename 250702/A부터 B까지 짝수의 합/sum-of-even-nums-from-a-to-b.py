inp = input()
arr = list(map(int, inp.split()))
# sorted_arr = sorted(arr)  # 새로운 정렬된 배열 생성
A = arr[0]
B = arr[1]

sum_val=0



for i in range(A, B+1):
    if i%2==0:
        sum_val+=i
print(sum_val)