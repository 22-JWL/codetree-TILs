N = int(input())

for i in range (1, N+1):
    if i%3==0 or (i%10)==3 or (i%10)==6 or (i%10)==9:
        print(0, end=' ')
    elif i>30 and i<40:
        print(0, end=' ')

    elif i>60 and i<70:
        print(0, end=' ')
    elif i>90 and i<100:
        print(0, end=' ')
    else:
        print(i, end =' ')
    