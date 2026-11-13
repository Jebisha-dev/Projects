
class FoodItem:
    def __init__(self, food_id, food_name, price, quantity):
        self.food_id = food_id
        self.food_name = food_name
        self.price = price
        self.quantity = quantity

    def display_food(self):
        print("Food ID:", self.food_id)
        print("Food Name:", self.food_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)


class Restaurant:
    def __init__(self):
        self.menu = []

    def add_food(self):
        food_id = input("Enter food ID: ")
        food_name = input("Enter food name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        obj = FoodItem(food_id, food_name, price, quantity)

        self.menu.append(obj)
        print("Food added successfully!")

    def view_menu(self):
        for item in self.menu:
            item.display_food()
    def search_item(self):
        a=input("Enter the Food ID or food name:")
        
        for item in self.menu:
            if a==item.food_id or a==item.food_name:
                print("The food is available")
                item.display_food()
                return
        print("Not Found")

    def delete_food(self):
        b=input("Enter the Food ID or food name that want to delete :")
        for item in self.menu:
            if b==item.food_id or b==item.food_name:
                item.display_food()
                self.menu.remove(item)
                print("The food is deleted")
                return
        print("Not found")

    def update_food(self):
        c=input("Enter the food id or food name that want to update:")
        for item in self.menu:
            if c==item.food_id or c==item.food_name:
                d=input("Tell what to update(Price/Quantity):")
                if d.lower()=="price":
                    new_price=float(input("Enter the new price:"))
                    item.price=new_price
                    print("price updated sucessfully")
                elif d.lower()=="quantity":
                    new_quantity=int(input("Enter the new quantity:"))
                    item.quantity=new_quantity
                    print("Quantity updated sucessfully")

                else:
                    print("invalid")

                item.display_food()
                return
        print("Food not found")

            


# Main program
restaurant = Restaurant()

while True:
    print("Restaurant Project")
    print("1. Add food")
    print("2. View food")
    print("3. Delete food")
    print("4. Update food")
    print("5. search food")
    print("6. EXIT")

    choice=input("Enter your choice:")

    if choice =="1":
        restaurant.add_food()
    elif choice == "2":
        restaurant.view_menu()
    elif choice == "3":
        restaurant.delete_food()
    elif choice =="4":
        restaurant.update_food()
    elif choice =="5":
        restaurant.search_item()
    elif choice =="6":
        print("Thank You!")
        break
    else:
        print("Invalid choice")
