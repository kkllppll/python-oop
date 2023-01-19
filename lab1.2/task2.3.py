class Product():
    def __init__(self, price, name, description, dimensions):
        self.price = price 
        self.name = name
        self.description = description
        self.dimensions = dimensions 

    
    
class Customer():
    def __init__(self, surname, name, patronymic, mobilephone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobilephone = mobilephone

        
class Order():
    total_price = 0
    order = {"Customer": None, "products": []}

    def __init__(self, order_number):
        self.order_number = order_number

    def set_customer(self, customer):
        if self.order["Customer"]:
            return "Customer is already in list."
        else:
            self.order["Customer"] = customer
            return "Customer: " + customer.name
       
    def get_customer(self):
        if self.order["Customer"]:
            return self.order["Customer"].name
        else:
            return None

    def set_products(self, products):
        self.order["products"].append({"Product name": products.name, "Product price": products.price,
                                        "Product description": products.description, "Product dimensions": products.dimensions})
                                            
    def get_products(self):
        return self.products["products"]                                       


    def final_price(self):
        self.total_price = 0
        for i in self.order["products"]:
            self.total_price += i["Product price"]
        return self.total_price

customer1 = Customer('Monet', 'Victria','-', "+4567382878")
purchase1_1 = Product(250, 'book','horror, black and white', '20x25cm')
purchase1_2 = Product(30, 'pen','black', '15cm')

 
               
buildorder = Order("000145447")
buildorder.set_customer(customer1)
buildorder.set_products(purchase1_1)
buildorder.set_products(purchase1_2)


print("Final order:", purchase1_1.name, purchase1_1.price,"$,", purchase1_2.name, purchase1_2.price,"$")
print("Order number:", buildorder.order_number, "\nFinal price:", buildorder.final_price()) 
