from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json


def search():

    website = website_entry.get()
    print(website)
    with open("data.json", "r") as data_file:
        website_dict = json.load(data_file)[website]
        email, password = website_dict.values()
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": user,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Fields not allowed", message="Fields are Empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=("Consolas", 10), bg="white")
website_label.grid(row=1, column=0)
user_label = Label(text="Email/Username:", font=("Consolas", 10), bg="white")
user_label.grid(row=2, column=0)
pass_label = Label(text="Password:", font=("Consolas", 10), bg="white")
pass_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
user_entry = Entry(width=45)
user_entry.insert(0, "dexter@gmail.com")
user_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=24)
pass_entry.grid(row=3, column=1)

# Buttons
generate_pass_button = Button(text="Generate Password", font=("Consolas", 10), command=generate_password)
generate_pass_button.grid(row=3, column=2)
add_button = Button(text="Add", font=("Consolas", 10), width=40, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", font=("Consolas", 10), command=search)
search_button.grid(row=1, column=2)

window.mainloop()
