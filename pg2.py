'''Write a Python program that uses a dictionary to store product prices. 
The program should allow adding new products and updating prices. 
Use “if” statements to check if a product already exists.'''


class StoreProductPrices:
    def __init__(self):
        self.productprices={}

    def add_product(self,product_name,price):
        if product_name in self.productprices:
            print(f"Updating price of {product_name} from {self.productprices[product_name]} to {price}.")

        else:
            print(f"Adding New Product:{product_name} with price  {price}.")

        self.productprices[product_name]=price


    def show_product_prices(self):
        if self.productprices:
            print("\n Product Prices are:")
            for product,price in self.productprices.items():
                print(f"{product}:{price}")
        else:
            print("No Products available")


P1=StoreProductPrices()
P1.add_product("Laptop",56000)
P1.add_product("Mobile",25000)

P1.show_product_prices()
P1.add_product("Laptop",50000)
P1.show_product_prices()


        