import os 

class Car:     #en klass har alltid stor bokstav
    def __init__(self, make, model, colour):
        self.make = make
        self.model = model
        self.colour= colour
    

    def view_cars(self):
        return f"{self.make} - {self.model} ({self.colour})"
     
     

cars = [] #lista
            
os.system("cls")


while True:
    make = input("Enter brand: ")
    os.system("cls")
    model = input("Enter model: ")
    os.system("cls")


    colour = input("Enter colour (type nothing and hit enter to quit): ")
    os.system("cls")


    if colour == "":
        break
            

    cars.append(Car(make, model, colour))

def display_cars():
        os.system("cls")
        print("\nAdd Car")
        for car in cars:
            print(car.view_cars)
    
display_cars()


os.system("cls")


