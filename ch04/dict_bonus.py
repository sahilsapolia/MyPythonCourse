
multiples_three = {}
for i in range(1,11):
    multiples_three[i] = i*3

message = "3 times multiple of {} is {}"

for key,value in multiples_three.items():
    print(message.format(key,value))
