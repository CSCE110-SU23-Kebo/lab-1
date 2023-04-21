# Cashier program
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
for name in sorted(basket, reverse=True):
    print(f"{name}: ${round(basket[name], 2)}")
print(f"Your total is ${round(sum(basket.values()), 2)}")