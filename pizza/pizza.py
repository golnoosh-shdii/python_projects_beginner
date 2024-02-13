import tkinter


def order_pizza():
    size = size_pizza_entry.get().lower()
    peperuni = peperuni_entry.get().lower()
    cheese = cheese_entry.get().lower()
    phone_entry.get()
    p = 0
    if size == "s":
        p += 50
    elif size == "m":
        p += 70
    elif size == "l":
        p += 100

    if size == "s" and peperuni == "yes":
        p += 20
    elif size == "m" and peperuni == "yes":
        p += 30
    elif size == "s" and peperuni == "yes":
        p += 40

    if size == "s" and peperuni == "yes" and cheese == "yes":
        p += 30
    elif size == "m" and peperuni == "yes" and cheese == "yes":
        p += 30
    elif size == "l" and peperuni == "yes" and cheese == "yes":
        p += 30

    ans_lable.config(text=f"{p}")


window = tkinter.Tk()
window.title("pizza GA")

size_pizza_lable = tkinter.Label(text="pizza size [s, m, l]: ")
size_pizza_lable.grid(row=0, column=0, padx=(20, 10), pady=10)

size_pizza_entry = tkinter.Entry(width=30)
size_pizza_entry.grid(row=0, column=1, padx=(20, 10), pady=10)

peperuni_lable = tkinter.Label(text="Now , Do you like pepperoni in your pizza? ")
peperuni_lable.grid(row=1, column=0, padx=(20, 10), pady=10)

peperuni_entry = tkinter.Entry(width=30)
peperuni_entry.grid(row=1, column=1, padx=(20, 10), pady=10)

cheese_label = tkinter.Label(text="Do you want extra cheese ? ")
cheese_label.grid(row=2, column=0, padx=(20, 10), pady=10)

cheese_entry = tkinter.Entry(width=30)
cheese_entry.grid(row=2, column=1, padx=(20, 10), pady=10)

phone_label = tkinter.Label(text="please enter your number: ")
phone_label.grid(row=3, column=0, padx=(20, 10), pady=10)

phone_entry = tkinter.Entry(width=30)
phone_entry.grid(row=3, column=1, padx=(20, 10), pady=10)

ans_lable = tkinter.Label(text="pice")
ans_lable.grid(row=4, column=1, padx=(20, 10), pady=10)

submit_button = tkinter.Button(text="submit!", bg="blue", command=order_pizza)
submit_button.grid(row=4, column=11)

window.mainloop()
