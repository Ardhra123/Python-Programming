N=int(input())
if(1<=N<=100000):
  if(N>0):
   print("positive")
elif(N<0):
   print("negative")
elif(N==0):
   print("zero")
else:
   print("not valid")
