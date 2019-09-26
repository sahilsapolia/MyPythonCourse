def print_stars(count):
    print("*"*count)

#print_stars()
print_stars(20)

def slice_list(list_to_slice,*upper_bounds):
    """Returns slice of list if upper bound is valid"""
    list_to_return = []
    for upper_bound in upper_bounds:
        if (len(list_to_slice) > upper_bound):
            print('slicing...')
            list_to_return.append(list_to_slice[:upper_bound])
        else:
            list_to_return.append(None)
    return list_to_return

some_nums = [2,5,4,2,22,54,12,8,-1]

print('Valus returned', slice_list(some_nums, 4))
print('Valus returned', slice_list(some_nums, 12))
print(slice_list(some_nums,4,12,2,3))

