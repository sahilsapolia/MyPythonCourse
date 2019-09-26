some_nums = [2,6,4,2,22,54,12,8,-1]
print(len(some_nums))
print("The sun of the list is :", sum(some_nums))
print("Third item in list: ", some_nums[2])

highest_num = some_nums[0]

for x in some_nums:
    if x > highest_num:
        highest_num = x

print("The hightes number is ", highest_num)

for x in range(len(some_nums) - 1):
    print(x)
    if (x%2==0):
        some_nums[x] = 11

print(some_nums)


