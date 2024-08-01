from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=60, pady=60)

user_entry = Entry(width=10)
user_entry.insert(END, '0')
user_entry.grid(column=1, row=0)

miles_label = Label(text="Miles").grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to").grid(column=0, row=1)

km_label = Label(text="Km").grid(column=2, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

def converter():
    num_entry=float(user_entry.get()) * 1.6
    result_label.config(text=f"{num_entry}")

calculate_button = Button(text="Calculate", command=converter)
calculate_button.grid(column=1, row=2)




window.mainloop()
