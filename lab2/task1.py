import random  

regular_price = 100
advance_ticket = 0.6 
student_ticket = 0.5 
late_ticket = 0.9 
class Tickets():
    def __init__(self, price):
        self.price = price
    def __str__(self):
        return str(self.price)


class Order():
    def __init__(self):
        self.id = (random.randint(0,100))
        self.event = None
        self.ticket = None
        self.ticket_price = None

   

        print("Here are the tickets available for sale:\n\t[1] - Regular ticket")
        print("\t[2] - Advance ticket (purchased 60 or more days before the event)")
        print("\t[3] - Late ticket (purchased fewer than 10 days before the event)")
        print("\t[4] - Student ticket (50% of Regular ticket.")
    
        while self.ticket not in ["1", "2", "3", "4"]:
            self.ticket = input("Enter type of the ticket:")
            if self.ticket == "1":
                self.ticket_price = Tickets(regular_price)
            elif self.ticket == "2":
                self.ticket_price =  AdvanceTicket(regular_price)
            elif self.ticket == "3":
                self.ticket_price = LateTicket(regular_price)
            elif self.ticket == "4":
                self.ticket_price = StudentTicket(regular_price)
            elif self.ticket == "exit":
                break
            else:
                print("Error! ", end="")

    def __str__(self):
        return f"""\n
        --------------------------------------
        |////////////////////////////////////|
        |/////////Your Ticket: {self.ticket_price:}//////////|
        |/////////Ticket Number:{self.id:/<3}//////////|
        |////////////////////////////////////|
        --------------------------------------"""
     

class AdvanceTicket(Tickets):
    def __init__(self, price):
        super().__init__(price)
        self.price = price * advance_ticket
    def __str__(self):
        return str(round(self.price))
        

class StudentTicket(Tickets):
    def __init__(self, price):
        super().__init__(price)
        self.price = price * student_ticket
    def __str__(self):
        return str((round(self.price)))

class LateTicket(Tickets):
    def __init__(self, price):
        super().__init__(price)
        self.price = price * late_ticket
    def __str__(self):
        return str((round(self.price)))
       

    
example1 = Order()
print(example1)


