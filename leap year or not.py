year = 2016
if (year % 16) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year")
       else:
           print("{0} is not a leap year")
   else:
       print("{0} is a leap year")
else:
   print("{0} is not a leap year")
