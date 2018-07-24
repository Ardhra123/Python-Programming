n = input("Input a letter of the alphabet: ")

if n in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % n)
elif n == 'y':
	print(" letter y stand for vowel, letter y stand for consonant.")
else:
	print("%s is a consonant." % n) 
