while True:
    try:
        budget=float(input("Enter your budget: "))
        print(budget)
        s=budget
    except ValueError:
        print("Print number as a amount ")
        continue
    else:
        break
# Creating dictionary to store product("name"),("quantity"),("price")with empty list as their values
product={"name":[],"quantity":[],"price":[],}
# converting dictionary into list
b=list(product.values())
name=b[0]
quantity=b[1]
price=b[2]
while True:
    try:
        print("Please choose an option :\n")
        choices=int(input("1.ADD AN ITEM \n2.EXIT\n"))
    except ValueError:
        print("Choose only given digits in the options...")
        continue
    else:
        # choice=int(input("Please enter your choice : "))
        if choices==1 and s>0:
            product_name=input("Enter a product name :")
            quan=input("Enter a quantity :")
            Price_=float(input("Enter a price :"))
            if Price_>s:
                print("Can't buy the product .You are out of budget ...")
                continue
            else:
                if product_name in name:
                    index=name.index(product_name)
                    quantity.remove(quantity[index])
                    price.remove(price[index])
                    quantity.insert(index,quan)
                    price.insert(index,Price_)
                    s=budget-sum(price)
                    print("Amount left ",s)
                else:
                    name.append(product_name)
                    quantity.append(quan)
                    price.append(Price_)
                    s=budget-sum(price)
                    print("Amount left\n",s)
        elif s<=0:
            print("### No Budget ###")
        else:
            break
    print("\n Amount left",(s))
if (s) in (price):
    print("Amount left can buy :".name)[price.index(s)]
print("\n\n Grocery List ")
for i in range (len(name)):
    print(name[i],quantity[i],price[i])