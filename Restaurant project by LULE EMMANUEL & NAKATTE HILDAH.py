
# restaurant management system using concepts of OOPs like inheritance, polymorphism, encapsulation, abstraction

class Dish:  # dish class for storing dish details as base class
    def __init__(self, name, price):
        self.name = name    # name of dish
        self.price = price  # price of dish

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def __str__(self):  # string representation of dish
        return self.name + " " + str(self.price)

class drink(Dish):  # drink class inherited from dish class
    def __init__(self, name, price, size):
        super().__init__(name, price)   # calling constructor of base class
        self.size = size    # size of drink

    def get_size(self):
        return self.size    # returning size of drink

    def set_size(self, size):
        self.size = size    # setting size of drink

    def __str__(self):
        return self.name + " " + str(self.price) + " " + self.size  # string representation of drink

class food(Dish):
    def __init__(self, name, price, type):
        super().__init__(name, price)   # calling constructor of base class
        self.type = type    # type of food

    def get_type(self):
        return self.type    # returning type of food

    def set_type(self, type):   # setting type of food
        self.type = type

    def __str__(self):
        return self.name + " " + str(self.price) + " " + self.type  # string representation of food

class order:
    # takes list of dishes as input
    def __init__(self, dishes, status):
        self.dishes = dishes    # list of dishes
        self.status = status    # status of order
        self.tax = 0.18     # tax rate
        self.service_charge = 0.05  # service charge rate

    def get_dishes(self):
        return self.dishes  # returning list of dishes

    def get_status(self):
        return self.status  # returning status of order

    def set_dishes(self, dishes):   # setting list of dishes
        self.dishes = dishes

    def set_status(self, status):   # setting status of order
        self.status = status

    def add_dish(self, dish):   # adding dish to order
        self.dishes.append(dish)

    def remove_dish(self, dish):    # removing dish from order
        self.dishes.remove(dish)

    def get_total(self):    # calculating total bill
        total = 0
        for dish in self.dishes:    # iterating over list of dishes
            total += dish.get_price()
        return total

    def get_tax(self):  # returning tax rate
        return self.tax

    def get_service_charge(self):   # returning service charge rate
        return self.service_charge

    def calculate_bill(self):   # calculating bill
        total = self.get_total()    # getting total bill
        tax = total * self.get_tax()    # calculating tax
        service_charge = total * self.get_service_charge()  # calculating service charge
        return total + tax + service_charge # returning total bill


    def __str__(self):
        return str(self.dishes) + " " + self.status # string representation of order

class dine_in_order(order):
    def __init__(self, dishes, table_no):
        super().__init__(dishes, 'Not Paid')    # calling constructor of base class
        self.table_no = table_no    # table number

    def get_table_no(self):
        return self.table_no    # returning table number

    def set_table_no(self, table_no):   # setting table number
        self.table_no = table_no    # setting table number

    def __str__(self):
        return str(self.dishes) + " " + str(self.table_no)  # string representation of dine in order

class take_away_order(order):
    def __init__(self, dishes, customer_name,address):  # constructor of take away order
        super().__init__(dishes, 'Not Paid')    # calling constructor of base class
        self.customer_name = customer_name  # customer name
        self.address = address  # address
        self.delivery_charge = 0.05 # delivery charge rate

    def get_customer_name(self):    # returning customer name
        return self.customer_name

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name  # setting customer name

    def get_address(self):
        return self.address # returning address

    def set_address(self, address):
        self.address = address  # setting address
    def calculate_bill(self):
        return super().calculate_bill() +  (self.get_total() * self.delivery_charge)    # calculating bill
    def __str__(self):
        return str(self.dishes) + " " + self.customer_name + " " + self.address # string representation of take away order

class table:
    def __init__(self, table_no, status, order):    # constructor of table
        self.table_no = table_no
        self.status = status
        self.order = order

    def get_table_no(self): # returning table number
        return self.table_no

    def set_table_no(self, table_no):   # setting table number
        self.table_no = table_no

    def get_status(self):   # returning status of table
        return self.status

    def set_status(self, status):   # setting status of table
        self.status = status

    def get_order(self):    # returning order
        return self.order

    def set_order(self, order):
        self.order = order  # setting order

    def __str__(self):
        return str(self.table_no) + " " + self.status + " " + str(self.order)   # string representation of table

class Restaurant:
    def __init__(self, name, no_of_tables,lunch_menu, breakfast_menu, dinner_menu, drinks_menu):    # constructor of restaurant
        self.name = name
        self.no_of_tables = no_of_tables
        self.free_tables = no_of_tables
        self.lunch_menu = lunch_menu
        self.breakfast_menu = breakfast_menu
        self.dinner_menu = dinner_menu
        self.drinks_menu = drinks_menu
        self.tables = []
        for i in range(no_of_tables):
            self.tables.append(table(i, "Available", dine_in_order([],i)))  # creating list of tables
        self.take_away_orders = []
    def get_name(self):
        return self.name    # returning name of restaurant

    def set_name(self, name):
        self.name = name    # setting name of restaurant

    def get_no_of_tables(self):
        return self.no_of_tables    # returning number of tables

    def set_no_of_tables(self, no_of_tables):
        self.no_of_tables = no_of_tables    # setting number of tables

    def get_tables(self):
        return self.tables  # returning list of tables

    def set_tables(self, tables):
        self.tables = tables    # setting list of tables

    def add_table(self, table):
        self.tables.append(table)   # adding table to list of tables

    def remove_table(self, table):
        self.tables.remove(table)   # removing table from list of tables

    def get_free_tables(self):
        return self.free_tables   # returning number of free tables

    def set_free_tables(self, free_tables):
        self.free_tables = free_tables  # setting number of free tables

    def get_lunch_menu(self):
        return self.lunch_menu  # returning lunch menu

    def set_lunch_menu(self, lunch_menu):
        self.lunch_menu = lunch_menu    # setting lunch menu

    def get_breakfast_menu(self):
        return self.breakfast_menu  # returning breakfast menu

    def set_breakfast_menu(self, breakfast_menu):
        self.breakfast_menu = breakfast_menu    # setting breakfast menu

    def get_dinner_menu(self):
        return self.dinner_menu # returning dinner menu

    def set_dinner_menu(self, dinner_menu):
        self.dinner_menu = dinner_menu  # setting dinner menu

    def get_drinks_menu(self):
        return self.drinks_menu # returning drinks menu

    def set_drinks_menu(self, drinks_menu):
        self.drinks_menu = drinks_menu  # setting drinks menu

    def add_dish_to_lunch_menu(self, dish):
        self.lunch_menu.add_dish(dish)  # adding dish to lunch menu

    def remove_dish_from_lunch_menu(self, dish):
        self.lunch_menu.remove_dish(dish)   # removing dish from lunch menu

    def add_dish_to_breakfast_menu(self, dish):
        self.breakfast_menu.add_dish(dish)  # adding dish to breakfast menu

    def remove_dish_from_breakfast_menu(self, dish):
        self.breakfast_menu.remove_dish(dish)   # removing dish from breakfast menu

    def add_dish_to_dinner_menu(self, dish):
        self.dinner_menu.add_dish(dish) # adding dish to dinner menu

    def remove_dish_from_dinner_menu(self, dish):
        self.dinner_menu.remove_dish(dish)   # removing dish from dinner menu

    def add_dish_to_drinks_menu(self, dish):
        self.drinks_menu.add_dish(dish) # adding dish to drinks menu

    def remove_dish_from_drinks_menu(self, dish):
        self.drinks_menu.remove_dish(dish)  # removing dish from drinks menu

    def add_table_to_restaurant(self, table):
        self.tables.append(table)   # adding table to list of tables

    def remove_table_from_restaurant(self, table):
        self.tables.remove(table)       # removing table from list of tables

    def check_table_details(self, table_no):
        for table in self.tables:   # checking table details
            if table.get_table_no() == table_no:    # checking table details
                return table

    def check_table_status(self, table_no):
        for table in self.tables:   # checking table status
            if table.get_table_no() == table_no:    # checking table status
                return table.get_status()

    def check_table_order(self, table_no):
        for table in self.tables:   # checking table order
            if table.get_table_no() == table_no:
                return table.get_order()

    def check_table_order_status(self, table_no):
        for table in self.tables:   # checking table order status
            if table.get_table_no() == table_no:
                return table.get_order().get_status()

    def check_table_order_items(self, table_no):
        for table in self.tables:   # checking table order items
            if table.get_table_no() == table_no:
                return table.get_order().get_items()

    def check_table_order_total(self, table_no):
        for table in self.tables:   # checking table order total
            if table.get_table_no() == table_no:
                return table.get_order().get_total()
    def cancel_table_order(self, table_no):
        for table in self.tables:   # cancelling table order
            if table.get_table_no() == table_no:
                table.set_order(None)   # setting order to None
                table.set_status("Available")
                self.free_tables += 1   # incrementing number of free tables
    def add_take_away_order(self, order):
        self.take_away_orders.append(order)

    def remove_take_away_order(self, order):
        self.take_away_orders.remove(order)



    def __str__(self):
        return self.name + " " + str(self.no_of_tables) + " " + str(self.free_tables)

class menu:
    def __init__(self, dishes):
        self.dishes = dishes

    def get_dishes(self):
        return self.dishes

    def set_dishes(self, dishes):
        self.dishes = dishes

    def add_dish(self, dish):
        self.dishes.append(dish)

    def remove_dish(self, dish):
        self.dishes.remove(dish)

    def __str__(self):
        return str(self.dishes)

def main():
    # Create breakfast menu
    breakfast_menu = menu([drink("Milk", 10000,'250ml'), drink("Coffee", 20000,'250ml'), drink("Tea", 100,'250ml'), drink("Juice", 1000,'250ml'), food("Bread", 100, 'Baked Item'), food("Egg", 100, 'Baked Item'), food("Bacon", 100, 'Baked Item'), food("Sausage", 100, 'Baked Item'), food("Hash Brown", 100, 'Baked Item')])  # creating breakfast menu

    lunch_menu = menu([food("Pilao Rice", 10000, 'Rice'), food("Matooke",10000,'Vegitable'),food('Chips/French Fries',1000,'Fast Food'), food('Grilled Irish',1000,'Meat'), food('Steam Irish',1000,'Meat'), food('Sauce – Chicken soup',1000,'Soup'), food('Mushroom soup',1000,'Soup'), food('Fried Pork',1000,'Meat'), food('Lamb',1000,'Meat'), food('Roasted Goat',1000,'Meat'), food('Beef',1000,'Meat'), food('Fried rabbit',1000,'Meat')]) # creating lunch menu

    dinner_menu = menu([food("Pilao Rice", 10000,'Rice'), food("Matooke",10000,'Vegitable'),food('Chips/French Fries',1000,'Fast Food'), food('Grilled Irish',1000,'Meat'), food('Steam Irish',1000,'Meat'), food('Sauce – Chicken soup',1000,'Soup'), food('Mushroom soup',1000,'Soup'), food('Fried Pork',1000,'Meat'), food('Lamb',1000,'Meat'), food('Roasted Goat',1000,'Meat'), food('Beef',1000,'Meat'), food('Fried rabbit',1000,'Meat')]) # creating dinner menu
    # Create drinks menu
    drinks_menu = menu([drink("Sodas", 10000,'250ml'), drink("Water", 1000,'250ml'), drink("Fresh Juice", 1000,'250ml'), drink("Beers", 100,'250ml')])
    # Create restaurant
    restaurant = Restaurant("Serena Resort Restaurant",  10, breakfast_menu, lunch_menu, dinner_menu, drinks_menu)  # creating restaurant

    # Create main menu
    while True: # main menu
        print("Welcome to Serena Resort Restaurant")
        print("1. Dine in")
        print("2. Take away")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice: "))  # getting choice from user
        except:
            print("Invalid input")
            continue
        if choice == 1:
            if restaurant.get_free_tables() == 0:
                print("Sorry, no free tables")  # checking if there are free tables
                continue
            else:
                print("Available tables: ")
                for table in restaurant.get_tables():   # printing available tables
                    if table.get_status() == "Available":
                        print(table.get_table_no(), 'Free')
                try:
                    table_no = int(input("Enter table number: "))
                except:
                    print("Invalid input")
                    continue
                if restaurant.check_table_status(table_no) == "Available":  # checking if table is available
                    restaurant.check_table_details(table_no).set_status("Occupied") # setting table status to occupied
                    restaurant.set_free_tables(restaurant.get_free_tables() - 1)    # decrementing number of free tables
                    restaurant.check_table_details(table_no).set_order(dine_in_order([],table_no))  # creating order for table
                else:
                    print("Sorry, table is occupied")   # if table is not available
                    continue
                while True:
                    print("1. Breakfast")
                    print("2. Lunch")
                    print("3. Dinner")
                    print("4. Drinks")
                    print("5. Check order")
                    print("6. Cancel order")
                    print("7. Pay bill")
                    print("8. Exit")
                    try:
                        choice = int(input("Enter your choice: "))  # getting choice from user
                    except:
                        print("Invalid input")
                        continue
                    if choice == 1:
                        print("Breakfast menu: ")
                        for i in range(len(restaurant.get_breakfast_menu().get_dishes())):  # printing breakfast menu
                            print(str(i + 1) + ". " + str(restaurant.get_breakfast_menu().get_dishes()[i]))
                        try:
                            dish_name = input("Enter dish number: ")    # getting dish name from user
                            while dish_name not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                                dish_name = input("Enter dish number: ")
                        except:
                            print("Invalid input")
                            continue

                        dish_name = int(dish_name)  # converting dish name to integer

                        dish = restaurant.get_breakfast_menu().get_dishes()[dish_name - 1]
                        restaurant.check_table_order(table_no).add_dish(dish)   # adding dish to order

                    elif choice == 2:
                        print("Lunch menu: ")   # printing lunch menu
                        for i in range(len(restaurant.get_lunch_menu().get_dishes())):  # printing lunch menu
                            print(i+1, restaurant.get_lunch_menu().get_dishes()[i].get_name(), restaurant.get_lunch_menu().get_dishes()[i].get_price())
                        try:
                            dish_name = input("Enter dish number: ")    # getting dish name from user
                            while dish_name not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']:
                                dish_name = input("Enter dish number: ")
                        except:
                            print("Invalid input")
                            continue

                        dish_name = int(dish_name)

                        dish = restaurant.get_lunch_menu().get_dishes()[dish_name - 1]  # getting dish from lunch menu
                        restaurant.check_table_order(table_no).add_dish(dish)   # adding dish to order

                    elif choice == 3:
                        print("Dinner menu: ")
                        for i in range(len(restaurant.get_dinner_menu().get_dishes())): # printing dinner menu
                            print(i+1, restaurant.get_dinner_menu().get_dishes()[i].get_name(), restaurant.get_dinner_menu().get_dishes()[i].get_price())
                        try:    # getting dish name from user
                            dish_name = input("Enter dish number: ")    # getting dish name from user
                            while dish_name not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']:
                                dish_name = input("Enter dish number: ")
                            dish_name = int(dish_name)  # converting dish name to integer
                        except:
                            print("Invalid input")
                            continue


                        dish = restaurant.get_dinner_menu().get_dishes()[dish_name - 1] # getting dish from dinner menu
                        restaurant.check_table_order(table_no).add_dish(dish)

                    elif choice == 4:   # printing drinks menu
                        print("Drinks menu: ")
                        for i in range(len(restaurant.get_drinks_menu().get_drinks())):
                            print(str(i + 1) + ". " + str(restaurant.get_drinks_menu().get_drinks()[i]))
                        try:
                            dish_name = input("Enter dish number: ")
                            while dish_name not in ['1', '2', '3', '4']:
                                dish_name = input("Enter dish number: ")

                            dish_name = int(dish_name)
                        except:
                            print("Invalid input")
                            continue

                        dish = restaurant.get_drinks_menu().get_dishes()[dish_name - 1]
                        restaurant.check_table_order(table_no).add_dish(dish)

                    elif choice == 5:   # printing order
                        print('Your order is: ')
                        for dish in restaurant.check_table_order(table_no).get_dishes():    # printing dishes in order
                            print(dish.get_name(), dish.get_price())

                    elif choice == 6:
                        dishes=restaurant.check_table_order(table_no).get_dishes()
                        try:
                            print('Your order is: ')    # printing dishes in order
                            for i in range(len(dishes)):
                                print(i+1,dishes[i].get_name(), dishes[i].get_price())  
                            dish_name = input("Enter dish number: ")
                                
                            while dish_name not in [str(i+1) for i in range(len(dishes))]:
                                dish_name = input("Enter dish number: ")
                            dish_name = int(dish_name)
                        except:
                            print("Invalid input")
                            continue

                        restaurant.check_table_order(table_no).dishes.pop(dish_name-1)  # removing dish from order

                    elif choice == 7:
                        if restaurant.check_table_order(table_no).get_total() == 0:
                            print("Order is empty")
                            continue
                        print("Total bill: ", restaurant.check_table_order(table_no).calculate_bill())
                        restaurant.check_table_order(table_no).set_status("Paid")   # setting order status to paid
                        restaurant.check_table_details(table_no).set_status("Available")
                        restaurant.set_free_tables(restaurant.get_free_tables() + 1)
                        print("Thank you for dining with us")
                        break

                    elif choice == 8:
                        if restaurant.check_table_order(table_no).dishes != [] and restaurant.check_table_order(table_no).get_status() != "Paid":
                            print("Please pay bill")    # if order is not empty and order status is not paid then print the message to pay bill

                            continue
                        else:
                            break
                    else:
                        print("Invalid choice")
                        continue

        elif choice == 2:
            customer_name = input("Enter customer name: ")  # getting customer name from user
            address = input("Enter address: ")  # getting customer name and address from user
            order=take_away_order([],customer_name,address) # creating take away order

            while True:
                print("1. Breakfast")   
                print("2. Lunch")
                print("3. Dinner")
                print("4. Drinks")
                print("5. Check order")
                print("6. Cancel order")
                print("7. Pay bill")
                print("8. Exit")
                choice = int(input("Enter your choice: "))  # getting choice from user
                if choice == 1:
                    print("Breakfast menu: ")
                    for i in range(len(restaurant.get_breakfast_menu().get_dishes())):  # printing breakfast menu
                        print(str(i + 1) + ". " + str(restaurant.get_breakfast_menu().get_dishes()[i]))
                    try:
                        dish_name = input("Enter dish number: ")
                        while dish_name not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                            dish_name = input("Enter dish number: ")

                        dish_name = int(dish_name)
                    except:
                        print("Invalid input")
                        continue

                    dish = restaurant.get_breakfast_menu().get_dishes()[dish_name - 1]
                    order.add_dish(dish)

                elif choice == 2:
                    print("Lunch menu: ")       
                    for i in range(len(restaurant.get_lunch_menu().get_dishes())):  # printing lunch menu
                        print(str(i + 1) + ". " + str(restaurant.get_lunch_menu().get_dishes()[i]))
                    try:
                        dish_name = input("Enter dish number: ")
                        while dish_name not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']:
                            dish_name = input("Enter dish number: ")

                        dish_name = int(dish_name)
                    except:
                        print("Invalid input")
                        continue

                    dish = restaurant.get_lunch_menu().get_dishes()[dish_name - 1]
                    order.add_dish(dish)

                elif choice == 3:
                    print("Dinner menu: ")
                    try:
                        for i in range(len(restaurant.get_dinner_menu().get_dishes())): # printing dinner menu
                            print(str(i + 1) + ". " + str(restaurant.get_dinner_menu().get_dishes()[i]))
                        dish_name = input("Enter dish number: ")
                        while dish_name not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']:
                            dish_name = input("Enter dish number: ")

                        dish_name = int(dish_name)
                    except:
                        print("Invalid input")
                        continue

                    dish = restaurant.get_dinner_menu().get_dishes()[dish_name - 1]
                    order.add_dish(dish)


                elif choice == 4:
                    print("Drinks menu: ")
                    try:    
                        for i in range(len(restaurant.get_drinks_menu().get_drinks())): # printing drinks menu
                            print(str(i + 1) + ". " + str(restaurant.get_drinks_menu().get_drinks()[i]))
                        dish_name = input("Enter dish number: ")
                        while dish_name not in ['1', '2', '3', '4']:
                            dish_name = input("Enter dish number: ")

                        dish_name = int(dish_name)
                    except:
                        print("Invalid input")
                        continue

                    dish = restaurant.get_drinks_menu().get_dishes()[dish_name - 1]
                    order.add_dish(dish)    # adding dish to order

                elif choice == 5:
                    print('Order: ')    # printing dishes in order
                    for dish in order.get_dishes():
                        print(dish.get_name(), dish.get_price())

                elif choice == 6:   # removing dish from order
                    dishes=order.get_dishes()
                    try:
                        print('Your order is: ')    # printing dishes in order
                        for i in range(len(dishes)):
                            print(i+1,dishes[i].get_name(), dishes[i].get_price())
                        dish_name = input("Enter dish number: ")
                            
                        while dish_name not in [str(i+1) for i in range(len(dishes))]:
                            dish_name = input("Enter dish number: ")
                        dish_name = int(dish_name)
                    except:
                        print("Invalid input")
                        continue

                    dish_name = int(dish_name)

                    order.dishes.pop(dish_name - 1)

                elif choice == 7:   # paying bill
                    if order.get_total() == 0:
                        print("Order is empty")
                        continue
                    print("Total bill: ",order.calculate_bill())
                    order.set_status("Paid")
                    restaurant.add_take_away_order(order)
                    print("Thank you for ordering")
                    break

                elif choice == 8:   # exiting
                    if order.dishes != [] and order.get_status() != "Paid":
                        print("Please pay bill")

                        continue
                    else:
                        break

                else:
                    print("Invalid choice")
                    continue

        elif choice == 3:
            print('Thank you for using our system')
            break

        else:
            print("Invalid choice")
            continue

if __name__ == '__main__':
    main()