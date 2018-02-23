N=int(input("Enter a number: "))
if((1<=N<=100000)and(N%2==0)):
  print("Even")
elif((N%2)!=0):
   print("Odd")
else:
  print("not valid")
