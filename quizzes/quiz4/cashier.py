# Cashier program
# Updated to handle duplicate items

items = int(input("Number of items: "))
basket = {}
for i in range(items):
    name = input("\nItem name: ")
    price = float(input("Item price: "))
    if name in basket:
        # Update the existing item in the basket
        basket[name] += price
    else:
        # Create a new item
        basket[name] = price
        # basket.update({name:price})

print("\nReceipt: ")
for name, price in basket.items():
    print(f"{name}: ${round(price, 2)}")
print(f"Your total is ${round(sum(basket.values()), 2)}")
