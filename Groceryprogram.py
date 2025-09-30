groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}

cart = {}

while True:
    user_input = input("What do you want to buy? ").strip().lower()

    if user_input == "done":
        break

    parts = user_input.split()
    item = parts[0]

    if len(parts) > 1 and parts[1].isdigit():
        quantity = int(parts[1])
    else:
        quantity = 1

    if item in groceries:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
    else:
        print("Sorry, we don’t have that item.")

total = 0

for item, quantity in cart.items():
    price = groceries[item]

    if item == "milk" and quantity > 2:
        price -= 1  

    total += price * quantity

print("\nYou bought:", cart)
print("Total = $", total)

if total > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")


    