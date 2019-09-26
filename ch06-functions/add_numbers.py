def add_numbers(*numbers):
    count=0
    for number in numbers:
        count += number

    return count

print('total_sum = ', add_numbers(1,2,3,4,5,6,7,8,23,45,67,45,67))