class All_Product:
    def __init__(self):
        self.allOrders = []
        self.allproducts = {}
        self.topselling = (0,0)

    class Product:
        def __init__(self,prod_id,quantity,cust_id,price):
            self.prod_id = prod_id
            self.quantity = quantity
            self.cust_id = cust_id
            self.price = prod_id

    def place_order(self,prod_id,quantity,cust_id,price):
        order = self.Product(prod_id,quantity,cust_id,price)
        self.allOrders.append(order)
        if prod_id in self.allproducts.keys():
            self.allproducts[prod_id] += quantity
        else:
            self.allproducts[prod_id] = quantity
        
        if self.topselling[1]<self.allproducts[prod_id]:
            self.topselling = (prod_id,self.allproducts[prod_id])

    def get_top_selling_product(self):
        return self.topselling
    
    def count_unique_products(self):
        return len(self.allproducts.keys())