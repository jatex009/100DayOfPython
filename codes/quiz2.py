from tkinter import *

window = Tk()
window.title("MY GUI")
window.minsize(width=400, height=400)

my_label = Label(text="This is a new text", font=("Arial", 24, "bold"))
my_label.pack()


# function for a button once its clicked
def action():
    print("Do something")


# add a button
button = Button(text="Click Me", command=action)
button.pack()

# add an entry
entry = Entry(width=25)
entry.insert(END, string="Type something")
print(entry.get())
entry.pack()

# add a text bar
text = Text(width=20, height=4)
text.focus  # puts cursor in the text box
text.insert(END, "Text Entry")
print(text.get("1.0", END))  # GETS current value of the text box
text.pack()


# add a spinbox
# create a function for the spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# add a scale
def scaling(value):
    print(value)


scale = Scale(from_=0, to=100, command=scaling)
scale.pack()

# add a checkbutton
def checkbox_used():
    print(checked_state.get())


checked_state = IntVar() # variable to hold on to checked state, 0 for off, 1 for on.
checkbox = Checkbutton(text="Is ON?", variable=checked_state, command=checkbox_used)
checkbox.pack()

# add a radio
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radio1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radio2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radio1.pack()
radio2.pack()


# adding a list box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Mango", "Guava", "Watermelon"]
for items in fruits:
    listbox.insert(fruits.index(items), items)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



window.mainloop()
