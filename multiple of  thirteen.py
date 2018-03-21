def isMultipleof13(n):
      
    while ( n > 0 ):
        n = n - 13
  
    if ( n == 0 ):
        return 1
  
    return 0
     

i = 26
if ( isMultipleof13(i) == 1 ):
    print (i, "is multiple of 13")
else:
    print (i, "is not a multiple of 13")
  
