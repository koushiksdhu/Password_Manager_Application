
from tkinter import *       # It just imports all the classes available inside the tkinter module.
from tkinter import messagebox  # message boc should be imported explicitly. It would not get imported by the above syntax.
from threading import Timer     # for timer function threading module is being imported.
from pass_generate import create_password   # importing create_password function from pass_generate.py
import pyperclip    #  This module contains functions which is helpful for copy and paste of text.
import json     # This module contains functions that is used to perform various operations in JSON file.

# --------------------------------------------- NOTES --------------------------------------------------------

# Using columnspan we use to span the column. Suppose, column = 0, columnspan = 2 then the widget will get accomodate in two columns as number of columnspan is 2.
# for documentation of Tkinter visit: https://tkdocs.com/tutorial/
# Tkinter provides an interface STAMNDARD DIALOGS which can be used for popups or message dialogs.
# The easiest way to use this module is to use one of the convenience function:
# showinfo(), showwarning(), showerror(), askquestion(), askokcancel(), askyesno(), askretrycancel().
# For Example: messagebox.showinfo(title= "This is a title", message = "This is a message")
# Pyperclip is a cross-platform Python module for copy and paste clipboard functions.
# It has two useful functions: pyperclip.copy('text that is to be copied.) and pyperclip.paste().

# --------------------------------------------- CONSTANTS ----------------------------------------------------

FONT = ("Times New Roman", 13, "normal")

# ---------------------------------------- PASSWORD GENERATOR ------------------------------------------------

def generate_password():
    password = create_password()
    password_entry.delete(0, END)       # Delete if there is some previous password in the field.
    password_entry.insert(0, password)  # Insert the new password in the field.
    pyperclip.copy(password)            # To copy the password when it is being generated so that we can paste it where I wanted to be with manually copying it.

def search_details():
    website = website_entry.get().title()       # to fetch the data from the entry field get() function is being used over here.
    try:        # To handle the error if JSON file is not available. 
        with open("data.json", "r") as datafile:    # Opening the file in read mode.
            d = json.load(datafile)                 # Reading the file and storing it in variable d.    
    
    except FileNotFoundError:                   # If exception is thrown by the above try block. In case the JSON file doesn't exist.
        messagebox.showerror(title = "Error", message = "No Data File Found.\n")       # Dialog box prompt.
    
    else:               # If no exception is being thrown by the baove try block.
        if website in d:        # Checking whether the website is available as a key inside the dictionary or not.
            email = d[website]["email"]     # Fetching the email from the nested dictionary and storing it inside a variable.
            password = d[website]["password"]       # Fetching the password from the nested dictionary and storing it inside a variable.
            messagebox.showinfo(title = "Password Manager", message = f"Website Name: {website}\n\nUsername: {email}\nPassword: {password}\n")       # Dialog box prompt.
        else:                   # If dictionary is not contains that website details.
            messagebox.showerror(title = "Error", message = f"No details for {website} exists.\n")       # Dialog box prompt.
    
    
# ---------------------------------------- SAVE PASSWORD ------------------------------------------------------

def save_password():
    website = website_entry.get()       # to fetch the data from the entry field get() function is being used over here.
    username = username_entry.get()     # to fetch the data from the entry field get() function is being used over here.
    password = password_entry.get()     # to fetch the data from the entry field get() function is being used over here.
    
    password_data = {       # Creating dictionary named, json_data, which will be dumped in JSON file.
        website: {
            "email": username,
            "password": password
        }
    }
    
    # messagebox.showinfo(title = "Password Manager", message = "Data Saved Successfully")     # this will prompt with "Data Saved Successfully" on the screen.
    
    # Validation for empty fields:
    if len(website) == 0:
        messagebox.showerror(title = "Password Manager", message = "Please Enter Website Name.")
    elif len(username) == 0:
        messagebox.showerror(title = "Password Manager", message = "Please Enter Email/Username")
    elif len(password) == 0:
        messagebox.showerror(title = "Password Manager", message = "Please Enter Password.")
    else:
        
        is_ok = messagebox.askokcancel(title = "Password Manager", message = f"These are the details entered:\nWebsite Name: {website}\nUsername: {username}\nPassword: {password}\n\nIs it OK to Save ?")       # Dialog box prompt.
        # In is_ok variable, boolean data is being stored which is being returned by asktocancel() function.
    
        if is_ok:       # Checking whether the user clicked on OK or CANCEL button.
            
            # Creating simple text file and storing the data inside it.
        #     with open("data.txt", "a") as f:          
        #         f.write(f"{website}  |  {username}  |  {password}\n\n")
        #         f.close()
        
            # Creating a JSON file and storing the data inside it:
            try:                                                # If JSON file is not present then this block is used to handle FileNotFoundError.
                with open("data.json", "r") as data_file:       # Opening JSON file in read mode. 
                    data = json.load(data_file)                 # Reading the JSON file and storing it inside data variable.
                    
            except FileNotFoundError:                           # This block is used to catch FileNotFoundError.
                with open("data.json", "w") as data_file:       # Opening JSON file in Write mode so that of that file is not present then it will get created.
                    json.dump(password_data, data_file, indent = 4)             # Dumping the dictionary data into the JSON file.
                    # Indent is used as a parameter in the above line with value 4 means all the data are seprated by 4 spaces bertween them.
            
            else:       # If the try block does not throw any exception then else block will get triggered.
                data.update(password_data)                      # Updating with the new Data.
                
                with open("data.json", "w") as data_file:   # Opening the JSON file in Write mode to dump the updated data.
                    json.dump(data, data_file, indent = 4)      # Dumping the updated data into JSON file.
                    
            finally:
                website_entry.delete(0, END)        # Delete the entire text from the entry field. 0 is the starting range and END is the ending range of the string entered into the entry field.
                password_entry.delete(0, END)       # Same same thing as mentioned above.
                website_entry.focus()               # Move the cursor to the Website Name entry field.
# The below lines are used if we want to show the confirmation as a label on the screen below the ADD button. This is being done using timer method of threading module. 
                saved.configure(text = "Data Saved Successfully.")      # Updating the text, which was empty previously.  
                t = Timer(1, clear_saved)  # Using Timer from Threading module. Here, lear_saved is the function call and 1 is the duration in second.
                t.start()   # Starting of the timer function.
        
def clear_saved():  # This function gets executed after 2 seconds.
    saved.configure(text = "")  # Updating the above text after 2 seconds.

# ---------------------------------------- UI SETUP -----------------------------------------------------------

window = Tk()       # Creating object of the Tkinter class.
window.title("Password Manager Application")
window.config(padx = 50, pady = 50)     # Providing the padding to the window.

canvas = Canvas(height = 200, width = 200)  # Creating object by passing height and width as a paramter and storing it in the variable.
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image = logo_img)     # 100 and 100 is the c and y position which is half of the canvas size.
canvas.grid(row = 0, column = 1)       # packing the canvas on the window suing grid.

label_website = Label(text = "Website Name:", font = FONT)
label_website.grid(row = 1, column = 0, pady = 10)

website_entry = Entry(width = 28, font = FONT)
website_entry.grid(row = 1, column = 1, pady = 10)
website_entry.focus()       # This help to put/focus the cursor on the particular field/entry automatically.

search_button = Button(text = "Search", command = search_details, font = FONT, width = 10)
search_button.grid(row = 1, column = 2, pady = 10)

label_username = Label(text = "Email/Username:", font = FONT)
label_username.grid(row = 2, column = 0, pady = 10)

username_entry = Entry(width = 40, font = FONT)
username_entry.grid(row = 2, column = 1, columnspan = 2, pady = 10)
username_entry.insert(0, "kkoushikssadhu@gmail.com")        # Insert this text at username_entry field at 0th index location. (For default, text insertion)

label_password = Label(text = "Password:", font = FONT)
label_password.grid(row = 3, column = 0, pady = 10)

password_entry = Entry(width = 28, font = FONT)
password_entry.grid(row = 3, column = 1, pady = 10)

generate_password = Button(text = "Generate", command = generate_password, font = FONT, width = 10)
generate_password.grid(row = 3, column = 2, pady = 10)

add = Button(text = "Add", command = save_password, width= 40, font = FONT)
add.grid(row = 4, column = 1, columnspan = 2, pady = 10)

saved = Label(text = "", font = FONT, fg = "red")
saved.grid(row = 5, column = 1, pady = 10)

window.mainloop()