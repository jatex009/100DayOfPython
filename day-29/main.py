from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ----------------------------------------* Password Generator ---------------------------------------------------------


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '+']

print("Welcome to the PyPassword generator!")

# new_item = [new_item for item in list]
# using list comprehension
password_letter = [choice(letters) for _ in range(randint(8, 10)) ]
password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
password_number = [choice(numbers) for _ in range(randint(2, 4))]

password_list = password_letter + password_symbol + password_number
shuffle(password_list)

password = "".join(password_list)

pyperclip.copy(password) # imported pyperclip to copy the password to the clipboard and can be pasted anywhere.
# password = " "
# for char in password_list:
#   password += char

# print(f" Your password is: {password}")


# ----------------------------------------* UI ---------------------------------------------------------
window = Tk()
window.title("Password Manager")
# window.minsize(width=600, height=500)
window.config(pady=70, padx=70)

# adding an image to GUI using Canvas() and PhotoImage classes
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


def generate():
    password_entry.insert(0, password)


def save():
    data = website_entry.get()
    data1 = email_entry.get()
    data2 = password_entry.get()


    if len(data) == 0 or data2 == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!!")
    else:
        # adding a pop-up before moving to store the data using messagebox
        # messagebox.showinfo(title="Title", message="Message")
        Is_ok = messagebox.askokcancel(title=data,
                                       message=f"These are the details entered:\nEmail: {data1}, \nPassword: {data2}\n"
                                               f"Is it ok to save?")

        if Is_ok:
            with open("data.txt", "a") as file:
                file.write(f"\n{data} | {data1} | {data2}")
                website_entry.delete(0, END)
                # email_entry.delete(0, END)
                password_entry.delete(0, END)



# second step we create a label
label_website = Label(text="Website:", font=("Arial", 10))
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:", font=("Arial", 10))
label_email.grid(column=0, row=2)

label_Password = Label(text="Password:", font=("Arial", 10))
label_Password.grid(column=0, row=3)

# third we add a text entry for specific labels
# used column span to span the entry to the next column
website_entry = Entry(width=60)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

email_entry = Entry(width=60)
email_entry.insert(END, string="example@gmail.com")
email_entry.grid(columnspan=2, row=2, column=1)

# fourth step we add buttons
generate_button = Button(text="Generate Password", font=("Arial", 10), width=20, command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", font=("Arial", 10), width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

# we create a function that stores the inputs of the website, email and password into a data.txt file(that will be
# created)


window.mainloop()
