N = int(input())

for i in range (1, N+1):
    if i%3==0 or (i%10)==3 or (i%10)==6 or (i%10)==9 or i==30 or i == 60 or i==90:
        print(0, end=' ')
    else:
        print(i, end =' ')
    