"""
    This project is about restaurent management system that a customer comes to restaurent
    and first this will greet to customer and display his menu and asked for order and 
    display total price of order and also asked for another order or not.
"""
# we will use dictionary and conditional satements i this project.

Menu = {
        "Small Pizza": 900, "Medium Pizza": 1350, "Large Pizza": 1950, "Family Pizza": 2350,
        "Regular Burger": 250, "Cheese Burger": 450, "Petti Burger": 560, "Combo Burger": 850,
        "Regular Shwarma": 150, "Cheese Shwarma": 350, "Zinger Shwarma": 450,
        "Chicken Kddahi_Full": 1650, "Chicken Kddahi_Half": 950, "Beef Kddahi_Full": 2400,
        "Beef Kddahi_Half": 1950, "Mutton Kddahi_Full": 4200, "Mutton Kddahi_Half": 2800,
        "Chicken Tikka_Full": 1200,  "Chicken Tikka_Half": 650, "1kg Kabbab": 1400, "Half_kg Kabbab": 800,
        "Regular_Drink": 80, "1Ltr_Drink": 180, "1.5Ltr_Drink": 250, "Jumbo pack_Drink": 350,
        "Yougart": 250, "Salad": 150
}
# first greet the customer
print("Hello Sir, Welcome to \"Urban Fork Restaurent!\"" )

# after greet it show the menu
print("""
Small Pizza: Rs:900\nMedium Pizza: Rs:1350\nLarge Pizza: Rs:1950\nFamily Pizza: Rs:2350\n
Regular Burger: Rs:250\nCheese Burger: Rs:450\nPetti Burger: Rs:560\nCombo Burger: Rs:850\n
Regular Shwarma: Rs:Rs:150\nCheese Shwarma: Rs:350\nZinger Shwarma: Rs:450\n
Chicken Kddahi_Full: Rs:1650\nChicken Kddahi_Half: Rs:950\n
Beef Kddahi_Full: Rs:2400\nBeef Kddahi_Half: Rs:1950\n
Mutton Kddahi_Full: Rs:4200\nMutton Kddahi_Half: Rs:2800\n
Chicken Tikka_Full: Rs:1200\nChicken Tikka_Half: Rs:650\n
1kg Kabbab: Rs:1400\nHalf_kg Kabbab: Rs:800\n
Regular_Drink: Rs:80\n1Ltr_Drink: Rs:180\n1.5Ltr_Drink: Rs:250\nJumbo pack_Drink: Rs:350\n
Yougart: Rs:250\nSalad: Rs:150
""")

# now ask to customer what would you like to order but first we will create order total variable to store the price of total order whic is orderd by customer
order_total = 0

# now input from user to that waht he want to order
item_1 = input("Enter The Item you want to order = ")
if item_1 in Menu:
    order_total+= Menu[item_1]
    print(f"Your item of {item_1} has been added to your order")

else:
    print(f"orderd item {item_1} is not available at this time")

# now we will create another variable to ask user for another order
another_order = input("Do You Want to order another item?(Yes/No)")
if(another_order=="Yes"):
    item_2 = input("Enter another item you want to order = ")
    if item_2 in Menu:
        order_total+= Menu[item_2]
        print(f"Your item of {item_2} has been added to your order")
    else:
        print(f"orderd item {item_2} is not available at this time")

another_order = input("Do You Want to order another item?(Yes/No)")
if(another_order=="Yes"):
    item_3 = input("Enter another item you want to order = ")
    if item_3 in Menu:
        order_total+= Menu[item_3]
        print(f"Your item of {item_3} has been added to your order")
    else:
        print(f"orderd item {item_3} is not available at this time")

another_order = input("Do You Want to order another item?(Yes/No)")
if(another_order=="Yes"):
    item_4 = input("Enter another item you want to order = ")
    if item_4 in Menu:
        order_total+= Menu[item_4]
        print(f"Your item of {item_4} has been added to your order")
    else:
        print(f"orderd item {item_4} is not available at this time")

print(f"The Total Amount of Your Order to Pay is Rs:{order_total}")

