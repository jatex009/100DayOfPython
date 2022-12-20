from tkinter import *

window = Tk()
window.title("Final Day project")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)


# creating a miles to kilometer converter GUI
def converter():
    print("I have been clicked")
    number = float(value.get("1.0", END))
    conversion = number * 1.609344

    # result.set("1.0", conversion)
    result.config(text=f"{conversion}")


# first we create a text entry
value = Text(width=10, height=1)
value.focus  # puts cursor in the text box
# text.insert(END, "Text Entry")
# print(value.get("1.0", END))  # GETS current value of the text box
value.grid(column=1, row=0)

button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)

result = Label(text="0")
result.grid(column=1, row=1)

text = Label(text="Miles", font=("Arial", 10, "bold"))
text.grid(column=2, row=0)

text1 = Label(text="is equal to", font=("Arial", 10, "bold"))
text1.grid(column=0, row=1)

text2 = Label(text="Km", font=("Arial", 10, "bold"))
text2.grid(column=2, row=1)

window.mainloop()
