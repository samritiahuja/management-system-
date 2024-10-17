#Define the menu of hotel
menu ={
    'Falafel Farmer Salad': 390,
    'basil pesto pasta ': 290,
    'italian affair': 260,
    'avocado sandwich': 400,
    'cold coffee': 280,
    'orange pulpy juice': 110,
    'oreo shake': 150,  
    }

#Greet
print("WELCOME TO HEALTHY DAY")
# print("Falafel Farmer Salad: 390\nbasil pesto pasta: 290\nitalian affair: 260\navocado sandwich :400\ncold coffee :280\norange pulpy juice :110\noreo shake :150\n")

order_total = 0
#390 + 150 = 340

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total +=menu[item_1] #0 + 390
    print(f"Your item {item_1} has been added to yoyr order")

else:
    print(f"order item {item-1} is not available yet")

    