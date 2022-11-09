import Task2_1 as menu
from datetime import datetime

if __name__ == "__main__":
    pizza = menu.get_pizza(datetime.now().weekday())()
    pizza.add_additional_ingridients("tomato", "blue cheese")
    print(pizza)