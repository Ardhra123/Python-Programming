odd_count = 0
user_number = None


while user_number != 0:
    user_number = int(input("Enter and integer (0 to quit): "))

    
    if user_number % 2 != 0:
        odd_count += 1   

print("There were {} odd numbers entered".format(odd_count))
