from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)  # size of the window


# Button
def button_clicked():
    print("I have been clicked")
    word = Input.get()
    my_label.config(text=word)


# label
my_label = Label(text="I am label", font=("Arial", 24, "bold"))
# changing a component in the label
# my_label["text"] = "New Text"
# or
my_label.config(text="New Text")
# we use pack to display the label to the screen otherwise the label won't be visible
# my_label.pack()
# 0r another layout is
# my_label.place(x=0, y=0)
# or the best layout out of the two is grid since it divides the layout as any number of columns and rows.
my_label.grid(column=0, row=0)

# button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=10, pady=10) # adding space to the widget
button1 = Button(text="New button", command=button_clicked)
button1.grid(column=2, row=0)
# button.pack()


# Entry
Input = Entry(width=15)
# Input.pack()
Input.grid(column=3, row=2)


window.mainloop()
