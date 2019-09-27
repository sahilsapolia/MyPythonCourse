import sys
import math
try:
    total_sum = int(sys.argv[1])
    discount_percent = int(sys.argv[2])
except IndexError:
    print('Invalid input, please enter two whole number values')
    sys.exit(-1)
except ValueError as message:
    print('Invalid input: ', message)
    sys.exit(-1)

final_amount = total_sum - (total_sum*discount_percent/100)

print(str(total_sum) + " at " + str(discount_percent) + "% " + " discount is $" + str(int(final_amount)))