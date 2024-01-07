n = int(input("Enter number of fibonacci terms: "))
if(n<=0):
    print("Number should be greater than 0")
elif(n==1):
    print(0)
elif(n==2):
    print(0)
    print(1)
else:
    p=0
    q=1
    print(0)
    print(1)
    for i in range(n-2):
        r=p+q
        print(r)
        p=q
        q=r
print("DONE")
    
