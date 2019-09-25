import sys
import math

total_sum = int(sys.argv[1])
discount_percent = int(sys.argv[2])

final_amount = total_sum - (total_sum*discount_percent/100)

print(str(total_sum) + " at " + str(discount_percent) + "% " + " discount is $" + str(int(final_amount)))