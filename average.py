n = input("Enter Number to calculate average")
n = int (n)
average = 0
sum = 0
for num in range(0,n+1,1):
    sum = sum+num
print("SUM of first ", n, "number is: ", sum )
