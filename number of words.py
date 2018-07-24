fname = input("Enter the element: ")
 
num_words = 0
 

for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)
