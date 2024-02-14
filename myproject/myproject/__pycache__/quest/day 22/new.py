# num= int(input('enter number : '))
# a1=['zero','one','two']
# a2=['ten','eleven','twelve']
# a3=['','','twenty']

# #200,221

# h=num//100
# b=num%100

# if b<10:
#     ones=num%10
#     print(ones)
#     print(a1[h]+' hunderd and '+a1[ones] )
# elif b>=10 and b<20:
#     o=b %10
#     print(a1[h] + 'hunderd and '+a2[o]) 
# else:
#     o=b %10
#     t=b//10
#     if o==0 and  t==0  :      
#         print(a1[h] + 'hunderd ') 
#     elif b>=20  :
#         print(a1[h]+' hunderd '+a3[t] + a1[o])





class ShoppingCart:
    def __init__(self):
        self.items = {}  # A dictionary to store items and their quantities

    def add_item(self, item, price, quantity=1):
        self.price=price
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if quantity >= self.items[item]:
                del self.items[item]
            else:
                self.items[item] -= quantity

    def calculate_total_price(self):
        total_price = 0
        for self.item, quantity in self.items.items():
            # Multiply the price of each item by its quantity and add it to the total price
            total_price += self.price * quantity
            print(total_price)

cos1=ShoppingCart()
cos1.add_item("pants",200)
cos1.add_item("shirt",250)
cos1.calculate_total_price