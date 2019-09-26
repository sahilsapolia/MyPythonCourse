counter=0
dynamic_counter=input('Enter the upper limit for counter')
if dynamic_counter == "":
    dynamic_counter = 4
else:
    dynamic_counter = int(dynamic_counter)

while True:
    if counter == dynamic_counter :
        break;
    if (counter%2 != 0):
        print (counter, end=" ")
    counter +=1