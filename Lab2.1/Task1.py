import json

AVAIABLE_TICKETS = {}

REGULAR_TICKET_PRICE = 20
ADVANCED_TICKET_DISCOUNT = 0.6
STUDENT_TICKET_DISCOUNT = 0.5
LATE_TICKET_ADDITIONAL = 0.1

DB_NAME = "events.json"

def fetch_ticket(cls):
    AVAIABLE_TICKETS[cls.title] = cls

class Event:
    def __init__(self, event_title:str, tickets:dict()):
        self.event_title = event_title
        self.tickets = tickets
        self.bought_tickets = []
        self.__save()
        
    @property    
    def tickets(self):
        return self.__tickets

    @tickets.setter
    def tickets(self, tickets:dict()):
        if len(tickets.keys()) == len(AVAIABLE_TICKETS.keys()):
            for ticket in tickets:
                if not AVAIABLE_TICKETS.__contains__(ticket):
                    raise ValueError(f"Event policy does not consider {ticket}")
            self.__tickets = tickets
        else:
            raise ValueError("Event ")
    
    
    def __save(self):
        with open(DB_NAME, "r") as f:
            data = json.load(f)
        
        if data["events"].__contains__(self.event_title):
                pass
        else:   
            with open(DB_NAME, "w") as f:
                obj = {
                    "title":self.event_title,
                    "tickets":self.tickets,
                    "bought_tickets":self.bought_tickets
                }
                data["events"][self.event_title] = obj
                json.dump(data, f)    
        
    
    def buy_ticket(self, title:str, payment:int|float):
        if not isinstance(title, str) or not AVAIABLE_TICKETS.keys().__contains__(title):
            raise TypeError("Invalid ticket title")
        
        if self.tickets[title] == 0:
            raise Exception("Tickets of this type are already sold")
        
        ticket = AVAIABLE_TICKETS[title](self.event_title)
        
        if ticket.price != payment:
            raise ValueError(f"You payment must consist of {ticket.price}$")
        
        self.bought_tickets.append(ticket)
        self.tickets[title] -= 1
        
        with open(DB_NAME, "r") as f:
            data = json.load(f)
        
        with open(DB_NAME, "w") as f:
            event = data["events"][self.event_title]
            event["tickets"][title] -= 1
            event["bought_tickets"].append({
                
                        "id":ticket.id,
                        "title":title,
                        "price":ticket.price 
                        
                })
            json.dump(data, f)
        
        return ticket
        

class Ticket:
    def __init__(self, id:int, title:str, price: int|float, event_title:str):
        self.title = title
        self.price = price
        self.event_title = event_title
        self.id = id
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        if not isinstance(id, int):
            raise TypeError("Invalid id")
        
        with open(DB_NAME, "r") as f:
            data = json.load(f)
            bought_tickets = data["events"][self.event_title]["bought_tickets"]
            for ticket in bought_tickets:
                if ticket["id"] == id:
                    raise Exception("Id dublication is forbidden")
        
        if id == 0:
            self.__id = self.generate_id()
        else:
            self.__id = id
    
    @property
    def event_title(self):
        return self.__event_title
    
    @event_title.setter
    def event_title(self, event_title):
        if not isinstance(event_title, str):
            raise TypeError("Invalid event title")
        
        with open(DB_NAME, "r") as f:
            data = json.load(f)
            events = data["events"]
            if not events.keys().__contains__(event_title):
                raise ValueError(f"Event {event_title} doesn't exists!")
        
        self.__event_title = event_title
     
    @property   
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):    
        if not isinstance(price, (int, float)):
            raise TypeError("Price is incorrect")
        self.__price = price
    
    def generate_id(self):
        with open(DB_NAME, "r") as f:
            data = json.load(f)
            event = data["events"][self.event_title]
            id = 1
            for ticket in event["bought_tickets"]:
                if ticket["id"] == id:
                    id += 1
        return id
    
    def __str__(self):
        return str({
            "id": self.id,
            "title": self.title,
             "event_title": self.event_title,
             "price": self.price
        })
        
@fetch_ticket
class RegularTicket(Ticket):
    title = "Regular ticket"
    price = REGULAR_TICKET_PRICE
    def __init__(self, event_title, id=0):
        super().__init__(id, self.title, self.price, event_title)
            
@fetch_ticket
class AdvancedTicket(Ticket):
    title = "Advanced ticket"
    price = REGULAR_TICKET_PRICE * ADVANCED_TICKET_DISCOUNT
    def __init__(self, event_title, id=0):
        super().__init__(id, self.title, self.price, event_title)
      
@fetch_ticket
class LaterTicket(Ticket):
    title = "Later ticket"
    price = REGULAR_TICKET_PRICE + REGULAR_TICKET_PRICE*LATE_TICKET_ADDITIONAL
    def __init__(self, event_title, id=0):
        super().__init__(id, self.title, self.price, event_title)
      
@fetch_ticket
class StudentTicket(Ticket):
    title = "Student ticket"
    price = REGULAR_TICKET_PRICE * STUDENT_TICKET_DISCOUNT
    def __init__(self, event_title, id=0):
        super().__init__(id, self.title, self.price, event_title)                                    
        
if __name__ == "__main__":
    
    tickets = {
        "Regular ticket":2,
        "Advanced ticket":4,
        "Later ticket":1,
        "Student ticket":3
    }  
    
    event = Event("Anime-fest", tickets)
    ticket1 = event.buy_ticket("Student ticket", 10)
    print(ticket1)