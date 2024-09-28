import csv
import os
import locale
from collections import Counter



class Product:
    def __init__ (self):
        self.products = [
                    {
                    "name", "blueraydspelare",
                    "desc", "blueraydspelare",
                    "price", 1000,
                    "quantity", 3
                    },
                    {
                    "name", "laptop",
                    "desc", "crazy gaming laptop",
                    "price", 15000,
                    "quantity", 2
                    }
                    ]
                    
                    
    def check_inventory(self):

            return self.products
        
get_products = Product()

products = get_products.check_inventory()

    
           
    
       
products = Product()
os.system("cls")   
print(products.check_inventory())
           
            
def display_inventory():
    for i in range (len(products.check_inventory)):
        os.system("cls")
        print(products[i]["name"])
        print(products[i]["desc"])
        print(products[i]["price"])
        print(products[i]["quantity"])
        
    os.system("cls")   
    display_inventory()

        



