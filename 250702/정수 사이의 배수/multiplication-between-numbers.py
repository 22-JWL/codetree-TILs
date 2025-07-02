inp = input()
arr = inp.split()

A = int(arr[0])
B = int(arr[1])
count = 0
sum_val=0

for i in range(A, B+1):
    
    if i%35==0:
        sum_val +=i
        count += 1

    elif i%5==0 or i%7==0:
        sum_val +=i
        count += 1
    

avg = sum_val / count
print(f"{sum_val} {avg:.1f}")

