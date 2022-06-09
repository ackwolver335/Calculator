# Here is another Module in Calculator Library created using Python which will provide the outcomes of Discount
# Following is the class of this one 

class Discount:
    original_price = 0
    discount_percent = 0

    def __init__(self,orgprice,discount):
        self.original_price = orgprice
        self.discount_percent = discount

    def final_price(self):
        discount_price = (self.discount_percent / 100) * self.original_price
        final_price = self.original_price - discount_price
        return final_price