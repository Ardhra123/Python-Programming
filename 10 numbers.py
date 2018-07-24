a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("10,11,12,14,16,18,19,20,13,21:"))
    a.append(b)
a.sort()
print("Largest element is:",a[n-1])
