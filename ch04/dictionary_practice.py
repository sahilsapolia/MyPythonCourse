squares = {1:1, 5:25, 2:4, 3:9, 4:16}
print('squares=', squares)

for key,value in squares.items():
    print(f"The square of {key} is {value}")

#output: 16
print('pop(4)=',squares.pop(4))

# Output:{1: 1, 5: 25, 2: 4, 3: 9}
print('squares', squares)

squares[6] = 36
print('squares added [6]: ',squares)

# Output: square.popitem() returns (6,36)
print('square.popitem() returns ', squares.popitem())

# Output: {1: 1, 2: 4, 3: 9}
print('squares after popitem', squares)

# delete a particular item
del squares[2]
#Outout: {1:1, 5:25, 3:9}
print('squares after del squares[2]',squares)

del squares[7]

# remove all items
squares.clear()

# Output: {}
print('squares after squares.clear()',squares)

# delete the dictionary itself
del squares

# Throws Error
#print(squares)


