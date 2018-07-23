A=int(input())
B=int(input())
C=0
while True:
    A=A+1
    if A%2==0:
        H=0
    elif A>=B:
        break
    else:
        C+=1
print(C)
