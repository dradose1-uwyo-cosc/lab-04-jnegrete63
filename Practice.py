items = ["Milk", "Bread", "Eggs", "Pizza", "Shirt"]
prices = [2.56, 1.50, 3.75, 5.99, 15.99]
#I bought Eggs for 3.4
#I bought Bread for 1.50
#...

for index in range(len(items)):
    print(f" I bought {items[index]} for ${prices[index]}")

#print out the items and there corresponding prices 

#print out the total of the prices. i payed ___ total
total = 0
for price in prices:
    total = price + total
print(f"I payed ${total} for the everything")

#print out the most expensive item you have and remove the item and price


mostexpensive_item = max(prices)
print(f"largest price, ${mostexpensive_item,[index]}")

del prices[4]
del items[4]


for index in range(len(items)):
    print(f" I bought {items[index]} for ${prices[index]}")

    


