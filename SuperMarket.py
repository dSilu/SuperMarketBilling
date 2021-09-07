# store data
store = {
    'Bread': 35,
    'Peanut Butter': 250.59,
    'Choco Chips': 199,
    'Amul Cheese': 89,
    'Blue Tokai': 428.56,
    'Taj Mahal Tea': 350,
    'Orange Juice':123,
    'Apple Cidar': 259
}


# Welcome statement
print(".............WELCOME TO NAVRIN..............\n")
print("Have a look at our store: ")
print("Product: Amount ₹")
print(47 * '-')
for key,value in store.items():
    print(key,':\t\t', value)
print("-"* 47)
print("Take your order!")

# Cart 
cart = []
amt = []
f_cart = {cart[i]: amt[i] for i in range(len(cart))}


# First order
product_input = input("Product: ")
product_input = product_input.title()
qn_input = int(input("Quantity: "))
product = store.get(product_input)
price = qn_input * store[product_input]
cart.append(product_input)
amt.append(price)
print("Your current order is:\t", product_input, price, "₹")


# Subsiquent orders
while True:
    next_product = input("Would you like to add another product: ")
    next_product = next_product.title()
    if next_product in store:
        qn_input = int(input("Quantity: "))
        nxt_product = store.get(next_product)
        n_price = float(qn_input) * float(nxt_product)
        price += n_price
        price = round(price, 2)
        cart.append(next_product)
        amt.append(price)

        f_cart = {cart[i]: amt[i] for i in range(len(cart))}

        print("Your current order is:\t", f_cart)
        
    elif next_product == 'No':
        break

# Discount
total_amt = float(sum(amt))
if total_amt >= 1000:
    disc = total_amt * 0.05 # 5% discount
elif total_amt >= 500:
    disc = total_amt * 0.02 # 2% discount
elif total_amt < 500:
    disc = 0


# Final receipt
print('------------------------------------------------\n')
print("Your Bill:")
for k,v in f_cart.items():
    print(k,":\t\t",v)
print('Total amount:\t\t',str(total_amt), "\t₹")
print("Discount:\t\t", str(disc), "\t₹")
print("Net Amount:\t\t", str(total_amt - disc), "\t₹\n")
print('Thank You for choosing NAVRIN!')
