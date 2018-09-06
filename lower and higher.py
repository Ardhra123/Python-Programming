def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list([2, 7, 5, 1]))

def largest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a > min:
            min = a
    return min
print(largest_num_in_list([2, 7, 5, 1]))
