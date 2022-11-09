all_pizzas = {}

additonal_ingridients = {
    "tomato": 1,
    "bacon": 3,
    "mushrooms": 2,
    "olives": 2,
    "meat": 3,
    "corn": 1,
    "blue cheese":2
}

pizza_of_day = {
    0:"Green Pizza",
    1:"Pepperoni Pizza",
    2:"Margherita Pizza",
    3:"Hawaiian Pizza",
    4:"Buffalo Pizza",
    5:"Cheese Pizza",
    6:"Meat Pizza"    
}

def fetch_pizza(cls):
    pizza = cls()
    all_pizzas[pizza.title] = cls

def get_pizza(day_of_week):
    if 0 <= day_of_week <= 6:
        pizza = pizza_of_day[day_of_week]
        return all_pizzas[pizza]
    else:
        raise ValueError("Number of day is incorrect")
    
class Pizza:
    def __init__(self, title:str, price:int|float, ingridients:list[str]):
        self.title = title
        self.price = price
        self.ingridients = ingridients
        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title: str):
        if isinstance(title, str):
            self.__title = title
        else:
            raise TypeError("Name of the pizza is incorrect")
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price: int|float):
        if not isinstance(price, int) and not isinstance(price, float):
            raise TypeError("Price of the pizza is incorrect!")
        self.__price = price
   
    @property  
    def ingridients(self):
       return self.__ingridients.copy()
   
    @ingridients.setter
    def ingridients(self, ingridients):
         for ingridient in ingridients:
             if not isinstance(ingridient, str):
                 raise TypeError(f"Ingridient {ingridient} is incorrect")
         self.__ingridients = ingridients
         
    def add_additional_ingridients(self, *ingridients):
        for ingridient in ingridients:
            if not ingridient in additonal_ingridients:
                raise ValueError(f"Addintional ingridients don't include {ingridient}")
            self.__ingridients.append(ingridient)
            self.price += additonal_ingridients[ingridient]

        
    def __str__(self):
        return f"Title: {self.title}\nPrice: {self.price}\nIngridients: {self.ingridients}"

@fetch_pizza
class GreenPizza(Pizza):
    def __init__(self):
        super().__init__("Green Pizza", 8, ["tomato", "lettuce", "broccoli", "corn", "cheese"])

@fetch_pizza
class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__("Pepperoni Pizza", 15, ["pepperoni", "cheese"])

@fetch_pizza
class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita Pizza", 10, ["tomato", "cheese"])

@fetch_pizza
class HawaiianPizza(Pizza):
    def __init__(self):
        super().__init__("Hawaiian Pizza", 12, ["chicken", "cheese", "pineaple"])

@fetch_pizza
class BuffaloPizza(Pizza):
    def __init__(self):
        super().__init__("Buffalo Pizza", 11, ["chicken", "blue cheese", "red onion"])

@fetch_pizza    
class CheesePizza(Pizza):
    def __init__(self):
        super().__init__("Cheese Pizza", 14, ["parmesan", "cheder", "danish blue"])

@fetch_pizza    
class MeatPizza(Pizza):
    def __init__(self):
        super().__init__("Meat Pizza", 17, ["chicken", "bacon", "hunting sausages"])