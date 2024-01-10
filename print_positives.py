n = int(input("Enter the number of elements: "))
list1 = []
listp = []
for i in range(n):
    ele = int(input("Enter element: "))
    list1.append(ele)
for i in list1:
    if i>0:
        listp.append(i)
print(listp)
