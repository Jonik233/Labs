
class Product:
    
    def __init__(self, price:float, description:str, length:float, width:float, height:float):
        
        if isinstance(price, float):
            if price > 0.0:
                self.price = price
            else:
                raise ValueError("Price must be greater than 0.0!")
        else:
            raise TypeError("TypeValue of price must be float!")
        
        if isinstance(description, str):
            self.description = description
        else:
            raise TypeError("TypeValue of description must be str!")
        
        if isinstance(length,float) and isinstance(width, float) and isinstance(height, float):
            if length > 0.0 and width > 0.0 and height > 0.0:
                self.length = length
                self.width = width
                self.height = height
            else:
                raise ValueError("Values of dimensions can't be negative!")
        else:
            raise TypeError("TypeValues of dimensions must be float")
        
    def __str__(self):
        return (f"Class: {self.__class__.__name__}\n"
              + f"Price: {self.price}\n"
              + f"Description: {self.description}\n"
              + f"Height: {self.height}\n"
              + f"Width: {self.width}\n"
              + f"Length: {self.length}\n")


    def __eq__(self, other):
        return (isinstance(other, Product) and other.price == self.price and other.description == self.description)
    
class Customer:
    
    def __init__(self, name:str, surname:str, patronymic:str, phone_number:str):
        
        if isinstance(name, str) and isinstance(surname, str) and isinstance(patronymic, str) and isinstance(phone_number, str):
            self.name = name
            self.surname = surname
            self.patronymic = patronymic
            self.phone_number = phone_number
        else:
            raise TypeError("TypeValues of name, surname, patronymic and phone_number must be str!")
        
    def __str__(self):
        return (f"Class: {self.__class__.__name__}\n"
              + f"Name: {self.name}\n"
              + f"Surname: {self.surname}\n"
              + f"Patronymic: {self.patronymic}\n"
              + f"Phone number: {self.phone_number}\n")
    

class Order:
    
    
    def __init__(self, customer: Customer, products: list[Product] = list()):
        
        if isinstance(customer, Customer):
            self.customer = customer
        else:
            raise TypeError("TypeValue of customer must be Customer!")
        
        if isinstance(products, list):
            for product in products:
                
                if not isinstance(product, Product):
                    raise TypeError("TypeValues of list[Products] must be Product!")
                   
            self.products = products
            self.quantities = list()
            self.count_quantities()
            
        else:
            raise TypeError("TypeValue of products must be list!")
    
    def count_quantities(self):
        for product in self.products: 
                contains = False
                for p in self.quantities:
                    if p[0].__eq__(product):
                        contains = True
                
                if contains:
                    continue
                
                self.quantities.append((product, self.products.count(product)))
                    
    def total_order_value(self):
        prices = [product.price for product in self.products]
        return sum(prices)
    
    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            self.quantities.clear()
            self.count_quantities()
        else:
            raise TypeError("TypeValue of product must be Product!")
    
    def remove_product(self, product):
        if isinstance(product, Product):
            
            if self.products.__contains__(product):
                self.products.remove(product)
                self.quantities.clear()
                self.count_quantities()     
            else:
                raise Exception("Product can't be found!")
        else:
            raise TypeError("TypeValue of product must be Product!")                
        
    def __str__(self):
        purchases = ""
        for product, quantity in self.quantities:
            purchases += (product.__str__() + f"Quantity: {quantity}\n\n")
        return f"{self.customer.__str__()}\n{purchases}"
