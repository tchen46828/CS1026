# My name is Terry Chen and this is my program for Assignment #1
# This program begins with the definition of menu items and their corresponding price within a dictionary, listing food item names as the key and their prices as the values
# The initial total of the table begins at $0
# The program then asks the table for their orders. It firsts ask the use which item they want.
# If the user inputs anything that is not a food item in the list, or if the name is incorrectly spelled, then the program asks the user for another input
# If the user inputs a proper food item name, then the program asks for a quantity of the food item
# This process continues until the user finishes the order by inputting 'q'
# The program then outputs the total before tax, the tax expense and the total after tax.
status_of_food_item = False
# This definition is the "switch" to continue the while loop if there is an incorrect input for the input of food item names
# If a proper food item name is inputted, then the status_of_food_item variable becomes True
menu = {"egg": 0.99, "bacon": 0.49, "sausage": 1.49, "hash brown": 1.19, "toast": 0.79, "coffee": 1.49,
        "tea": 1.09, "small breakfast": 0.99 + 1.19 + (2 * 0.79) + (2 * 0.49) + 1.49,
        "regular breakfast": (2 * 0.99) + 1.19 + (2 * 0.79) + (4 * 0.49) + (2 * 1.49),
        "big breakfast": (3 * 0.99) + (2 * 1.19) + (4 * 0.79) + (6 * 0.49) + (3 * 1.49)}
# Placed on separate lines to enhance readability
# This dictionary contains all the food items and their prices, with the small, regular and big breakfast prices as the individual costs of each item added together
table_order = 0
# This defines the initial dollar total of the table before their order, which should always be $0
def formatInput(textLine):
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return textLine
# This function helps keep user inputs consistent with the key variable names, deletes all spaces, lower-cases every letter and adds a single space between each word
while not status_of_food_item:
    food_item = input("Enter item (q to terminate) :  small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea:")
    food_item = formatInput(food_item)
# This while loop ensures that while the status of food items is False, that the input continues until the status is True, which only occurs if they input a proper food item name
# The function formatInput(textLine) was used to ensure the input "food_item" was permanently reformatted to match the variable names in the dictionary
    if food_item == 'q':
        status_of_food_item = True
# This if-statement is to first check if the input is 'q', which should automatically terminate the while loop (done by changing status of food item to True)
# This is placed at the very beginning to ensure no other code is run before it
    elif food_item != 'q' and food_item not in menu:
        print('Sorry, please enter a valid food item name')
# This if-statement checks if the food item input is invalid, whether it not be 'q' or not a valid food item name
    elif food_item in menu:
# If the foot item input is valid, then the program starts to ask what quantity of the item the customer wants
        status_of_quantity = False
# This status of quality makes sure the while loop for quantity input continues if the customer does not enter a valid input
        while not status_of_quantity:
            quantity = input('Enter quantity')
# Continuously asks the user for a quantity until a valid integer greater than 0 is input (then the status of quantity is changes to True)
            formatInput(quantity)
            quantity = formatInput(quantity)
# Ensures any spaces to not hinder int() or isnumeric()
            if not quantity.isnumeric() or int(quantity) <= 0:
# Checks to see if the quantity input is a number and if it is greater than 0
                print('Please enter a valid quantity (in integer form)')
            elif quantity.isnumeric() and int(quantity) > 0:
                food_item_total = int(quantity) * menu[food_item]
# If the quantity input is correct, then the price of the item is multiplied by the quantity and is added to the total
                table_order = table_order + food_item_total
                status_of_quantity = True
# The while loop for quantity is ended and continues back to the initial while loop for food items until 'q' is inputted
print('\n{:<10}{:>10}'.format('Cost :', '{:.2f}'.format(table_order)))
# When 'q' is input, the program outputs the total cost incurred before taxes for the table, rounding the decimal places to 2 spots
tax = round(0.13 * table_order, 2)
print('{:<10}{:>10}'.format('Tax :', tax))
# Tax is calculated by multiplying the total by 13%, and rounding to 2 decimal places and the tax expense is output
total = round(tax+table_order, 2)
print('{:<10}{:>10}'.format('Total :', total))
# The total including taxes is calculated by adding total before taxes to tax expense and is printed
