def print_stars(count):
    print("*"*count)

#print_stars()
print_stars(20)

def slice_list(list_to_slice,upper_bound):
    """Returns slice of list if upper bound is valid"""
    if (len(list_to_slice) > upper_bound):
        print('slicing...')
        return list_to_slice[:upper_bound]
    else:
        print('Value too high...',upper_bound)
        return None

some_nums = [2,5,4,2,22,54,12,8,-1]

print('Valus returned', slice_list(some_nums, 4))
print('Valus returned', slice_list(some_nums, 12))

