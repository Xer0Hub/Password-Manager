#--------------------IMPORTS AND RESOURCES------------------------------------#
from tarfile import data_filter
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    pass_entry.delete(0, END)
    #SYMBOL LISTS
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #NEW LISTS MADE FROM LIST + RANDOM ELEMENTS
    new_letters = [choice(letters) for _ in range(randint(8, 10))]
    new_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    new_number = [choice(numbers) for _ in range(randint(2, 4))]

    #ALL LISTS MELDED TO ONE
    mix_combined = new_letters + new_symbols + new_number
    generated_password = [choice(mix_combined) for _ in range(len(mix_combined))]
    generated_password_str = ''.join(generated_password)
    pass_entry.insert(0, generated_password_str)
    pyperclip.copy(generated_password_str)

# ---------------------------- SAVE PASSWORD ------------------------------- #
#COMMITS ELEMENTS FROM THE INPUT BOXES TO CREDS.TXT
def add_to_file():
    web_ent = web_entry.get()
    user_ent = user_box.get()
    pass_ent = pass_entry.get()

    new_data = {
        web_ent: {
            "Email:": user_ent,
            "Password": pass_ent,
        }
    }

    if web_ent and pass_ent:
        # USER CONFIRMATION
        is_ok = messagebox.askokcancel(title=web_ent, message=f"For {web_ent} you've entered: \nEmail/Username: {user_ent} \nPassword: {pass_ent} \nProceed to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    #READS OLD DATA
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                #UPDATES WITH NEW DATA
                data.update(new_data)

                #WRITES TO JSON FORMAT
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                # CLEAR THE FIELDS
                web_entry.delete(0, END)
                pass_entry.delete(0, END)


    else:
        messagebox.showerror(title="FIELDS EMPTY", message="You can not leave any fields empty, please fill all fields to continue to save.")


#Insert those inputs into data.txt file with spacing/formatting "|"
#WHEN THE USER DOES THIS AGAIN MAKE SURE IT'S APPENDED ON A NEW LINE.

# ---------------------------- UI SETUP ------------------------------- #
#WINDOW CONTROL
window = Tk()
window.title("Ultra l337 Password Manager")
window.config(padx=50, pady=50, bg='black')

#CANVAS CONTROL
canvas = Canvas(width=200, height=200, background='black', highlightthickness=0)
canvas.grid(row=0, column=1)

#THE LOGO
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

#-------------------------ON SCREEN ELEMENTS-----------------------------------------#
#WEBSITE
website = Label(text="Website:", bg="black", fg="green")
website.grid(column=0, row=1)
#WEB BOX
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)

#USERNAME / EMAIL
username = Label(text="Email/Username:", bg="black", fg="green")
username.grid(column=0, row=2)
#USER BOX
user_box = Entry(width=35)
user_box.insert(0, "example@email.com")
user_box.grid(column=1, row=2, columnspan=2)

#PASSWORD
password = Label(text="Password:", bg="black", fg="green")
password.grid(column=0, row=3)
#PASS BOX
pass_entry = Entry(width=35)
pass_entry.grid(column=1, row=3)
#GENERATE BUTTON
generate = Button(text="Generate Password", command=password_generator)
generate.grid(column=3, row=3)

#ADD BUTTON
add = Button(text="Add", width=29, command=add_to_file)
add.grid(column=1, row=4, columnspan=2)


canvas.mainloop()

#LESSONS I LEARNED
"""columnspan= allows you to manipulate certain elements better. You can specify how far it can span without
 stretching other elements.
 
 """