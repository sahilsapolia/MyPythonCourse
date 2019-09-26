
keep
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
step = int(input("Enter the step: "))


keep_looping = True
while keep_looping:
    print("""Do you wish to include : 
    1. All numbers
    2. Evens
    3. Odds"""
    choice = int(input("Enter your choice: "))
    if choice == 1:
        for x in range(start,end,step):
            print(x)
        break;
    elif choice == 2:
        counter = start
        while counter < end:
            if (counter % 2 == 0):
                print(counter)
            counter +=1
        break;
    elif choice == 3:
        counter = Start
        while counter < end:
            if (counter%2 == 1):
                print(counter)
            counter +=1
        break;

