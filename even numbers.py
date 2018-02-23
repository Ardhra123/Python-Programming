lower =800 
upper = 900
print("even numbers between two interval")
for num in range(lower,upper+1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
