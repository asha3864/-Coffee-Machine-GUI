import tkinter as tk
from tkinter import messagebox

class CoffeeMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Machine")
        self.root.geometry("400x400")

        self.resources = {"water": 500, "milk": 200, "coffee": 100}
        self.menu = {
            "Latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 150},
            "Espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 100},
            "Cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 200},
        }
        self.balance = 0

        tk.Label(root, text="Select Your Coffee:", font=("Arial", 14)).pack(pady=10)
        for coffee in self.menu.keys():
            tk.Button(root, text=coffee, command=lambda c=coffee: self.order_coffee(c)).pack(pady=5)
        
        tk.Button(root, text="Show Report", command=self.show_report).pack(pady=10)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=5)
    
    def order_coffee(self, coffee_name):
        coffee = self.menu[coffee_name]
        if self.check_resources(coffee):
            self.process_payment(coffee, coffee_name)
    
    def check_resources(self, coffee):
        for ingredient, amount in coffee.items():
            if ingredient in self.resources and self.resources[ingredient] < amount:
                messagebox.showerror("Error", f"Not enough {ingredient}!")
                return False
        return True

    def process_payment(self, coffee, coffee_name):
        cost = coffee["cost"]
        self.balance = simpledialog.askinteger("Payment", f"Enter amount (Cost: Rs{cost}):", minvalue=0)
        
        if self.balance is None or self.balance < cost:
            messagebox.showerror("Error", "Insufficient funds! Payment refunded.")
        else:
            change = self.balance - cost
            self.make_coffee(coffee, coffee_name)
            messagebox.showinfo("Success", f"Enjoy your {coffee_name}! Change: Rs{change}")

    def make_coffee(self, coffee, coffee_name):
        for ingredient in self.resources:
            if ingredient in coffee:
                self.resources[ingredient] -= coffee[ingredient]

    def show_report(self):
        report = f"Water: {self.resources['water']}ml\nMilk: {self.resources['milk']}ml\nCoffee: {self.resources['coffee']}g"
        messagebox.showinfo("Machine Report", report)

if __name__ == "__main__":
    from tkinter import simpledialog
    root = tk.Tk()
    app = CoffeeMachineGUI(root)
    root.mainloop()
