from tkinter import *
root=Tk()
root.geometry("644x455")
root.configure(bg="peach puff")
root.title("Travel Form")
def getvals():
    print("Submitting form")
    print(f"{name_value.get(),phone_value.get(),gender_value.get(),emergency_value.get(),payment_value.get(),food_service_value.get()}")
    with open("records.txt","a") as f:
        f.write(f"{name_value.get(),phone_value.get(),gender_value.get(),emergency_value.get(),payment_value.get(),food_service_value.get()}")
        f.write("\n")

Label(root,text="******** WELCOME TO DIVYA'S TRAVEL *********",font="comicsansms 13  bold",pady=15,bg="purple",fg="yellow").grid(row=0,column=3)


name=Label(root,text="Name",font="12",bg="purple",fg="yellow")
phone=Label(root,text="Phone",font="12",bg="purple",fg="yellow")
gender=Label(root,text="Gender",font="12",bg="purple",fg="yellow")
emergency=Label(root,text="Emergency Contact",font= "12",bg="purple",fg="yellow")
payment=Label(root,text="Payment Mode",font=" 12",bg="purple",fg="yellow")


name.grid(row=1,column=2,padx=15,pady=15)
phone.grid(row=2,column=2,padx=15,pady=15)
gender.grid(row=3,column=2,padx=15,pady=15)
emergency.grid(row=4,column=2,padx=15,pady=15)
payment.grid(row=5,column=2,padx=15,pady=15)

name_value=StringVar()
phone_value=StringVar()
gender_value=StringVar()
emergency_value=StringVar()
payment_value=StringVar()
food_service_value=IntVar()

name_entry=Entry(root,textvariable=name_value)
phone_entry=Entry(root,textvariable=phone_value)
gender_entry=Entry(root,textvariable=gender_value)
emergency_entry=Entry(root,textvariable=emergency_value)
payment_entry=Entry(root,textvariable=payment_value)


name_entry.grid(row=1,column=3)
phone_entry.grid(row=2,column=3)
gender_entry.grid(row=3,column=3)
emergency_entry.grid(row=4,column=3)
payment_entry.grid(row=5,column=3)

# checkbox

food_service=Checkbutton(text="Want to prebook your meals",variable=food_service_value,fg="yellow",bg="purple")
food_service.grid(row=6,column=3,padx=19,pady=23)


Button(text="Submit To Divya's Travels",command=getvals,bg="purple",fg="yellow").grid(row=7,column=3)
root.mainloop()