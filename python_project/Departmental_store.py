class Departmental_store:
    def __init__(self,list_of_items):
        self.items=list_of_items
    def store_available(self):
        print("Items present in the store are:  ")
        for items in self.items:
            print("\t "+items)
            
    def purchase_item(self,item_name):
        if item_name in items:
            print(f"You purchased a {items} from the store...Hope You Liked It...")
            return True
        else:
            print(f"Item you entered is not available in the store")
            return False
    
class Consumer:
    def request_item(self):
        self.item=input("Enter a item that uou want to purchase..")
        return self.item
    def return_item(self):
        self.item=input("Enter a item that you want to return..")
        return self.item
if __name__ == '__main__':
    list=["clothing","skincare","groceries","appliances"]
    Departmental_Store=Departmental_Store([list])
Consumer=Consumer()
while True:
    welcomemsg='''\n*************WELCOME TO MY DEPARTMENTAL STORE*************
    PLEASE CHOOSE AN OPTION :
    1.List of stores available here
    2.Request of items
    3.Return of items
    4.EXIT FROM THE DEPARTMENTAL STORE''' 
    print(welcomemsg)
    a=int(input("Enter your choice :"))
    if a==1:
        Departmental_Store.store_available()
    elif a==2:
        Departmental_Store.purchase_item(Consumer.request_item()
    elif a==3:
        Departmental_store.return_item(Consumer.return_item())
    elif a==4:
        exit()
    else:
        print("invalid")