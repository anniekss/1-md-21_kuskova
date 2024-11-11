from tkinter import *
def task_3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type,rate):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rate = rate
        def describe_restaurant(self):
            print(f"\nНазвание ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
            print(f"Рейтинг: {self.rating}")
        def open_restaurant(self):
            print(self.restaurant_name, " открыт")
        def update_rating(self,new_rate):
            self.rate = new_rate
            print("новое значение: ", self.new_rate)

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors, rate, location, hours, type):
            self.rate = rate
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.flavors = flavors
            self.location = location
            self.hours = hours
            self.type = type
        def add_flavor(self, flavor):
            self.flavors.append(flavor)
        def del_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
        def prov_flavor(self, flavor):
            if flavor in self.flavors:
                print(f" Мороженое {self.flavors}  вкуса есть")
        def saw_flavors(self):
            print("Сорта мороженого: ")
            for flavor in self.flavors:
                print(flavor)
        def saw_type(self):
            print("Вид мороженого: ")
            for types in self.type:
                print(types)

    IceCreamStand = IceCreamStand("Морожка","Ice_Creams",["шоколад","ваниль","клубника"], 4, "ул. вознесенский проспект, д. 20", "10:00 - 21:00", ["With stick","In horn"])

    root = Tk()
    root.title(f"Приложение от {IceCreamStand.restaurant_name}")
    root.geometry("300x200")

    label = Label(text=IceCreamStand.restaurant_name,font=("Arial", 24))
    label.pack()

    flavors = Label(text=IceCreamStand.flavors,font=("Arial", 20),background=("#434242"),foreground=("#FFFFFF"))
    flavors.pack(anchor=N,fill=BOTH)

    def Buy_Ice_Cream():
        window = Canvas(bg="Blue",width=100,height=100)
        window.pack(anchor=CENTER,expand=1)
        window.create_text(50,50,text='Спасибо за покупку',fill="#FFFFFF")

    add_flavor = Button(text="Купить морожку", command=Buy_Ice_Cream)
    add_flavor.place(x=30,y=100)


    root.mainloop()

task_3()