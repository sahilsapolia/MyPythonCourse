import sys
import math
product1_price = input("What is the price of product1? ")
print('ther type is', type(product1_price))
price1 = float(product1_price)
print('product1_price is:', price1)
print('print 1 is an integer:',price1.is_integer())
weight1 = float(input("How many ounces is product 1? "))
price2 = float(input("What is the price of product 2? "))
weight2 = float(input("How many ounces is product 2? "))
print('product2_price:', price2)

price_per_ounce1 = price1 / weight1
price_per_ounce2 = price2 / weight2
print("Price per ounce of product 1:")
print(price_per_ounce1)
print("Price per ounce of product 2:")
print(price_per_ounce2)

print("Product1 costs same as Product2", (price_per_ounce1 == price_per_ounce2))
print("Product2 is cheaper :" , (price_per_ounce1 > price_per_ounce2)) 

total_price = price1 + price2
print("total price of both products: ",total_price)
discount = 10
print("Discount applied :",discount)
discount_sum = total_price*discount/100

total_price -= discount_sum
print("Total Price after discount:",total_price)

print("the truncated value of product1 is ", math.trunc(price1))
print("The rounded value of product1 is ", round(price1))
print("The floor value is ", math.floor(price1))
print("The ceil value is", math.ceil(price1))