n=9
k=1
if n%2!=0:
    for i in range(1,n+1):
        if i<=round(n/2):
            for j in range(1,i+1):
                print(i*j,end=" ")
        else:
            for j in range(1,n-i+2):
                print(i*j,end=" ")
            k=i-k
        print()
else:
    print("invalid ")
