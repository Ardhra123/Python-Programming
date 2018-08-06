def calcProduct(n, product):
	if(n <= 0):
		if( len(str(product)) > 1):
		
			calcProduct(product,1)
		else:
			print product
	else:
		rem = 1
		if( n % 10 != 0 ):
			rem = ( n % 10 )
		calcProduct(n/10, ( rem * product))
 
calcProduct(23456,1)
 
