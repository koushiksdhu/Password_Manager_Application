from random import choice, randint, shuffle

def create_password():
        
    letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
            ]

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '<', '>', '?', '|', '}', '{', '[', ']', ';', ':']

    no_of_letters = randint(5, 8)    # 5 to 8 letters. 
    no_of_numbers = randint(2, 3)    # 2 to 3 numbers.
    no_of_symbols = randint(1, 2)    # 1 to 2 symbols.

    # password_list = []      # To store the password in a list fomat.

    # for each in range(no_of_letters):
    #     password_list.append(random.choice(letters))
    
    # for each in range(no_of_numbers):
    #     password_list.append(random.choice(numbers))
        
    # for each in range(no_of_symbols):
    #     password_list.append(random.choice(symbols))
     
    # The above code from line 18 to line 27 is been replaced by using LIST COMPREHESION below:
    password_letters = [choice(letters) for _ in range(no_of_letters)]
    password_numbers = [choice(numbers) for _ in range(no_of_numbers)]
    password_symbols = [choice(symbols) for _ in range(no_of_symbols)]
    
    password_list = password_letters + password_numbers + password_symbols  # Concatenating the above 3 list in a single list.
    
    shuffle(password_list)       # Shuffling each element in a list.
        
    # password = ""   # To store password in a string.
    # for p in password_list:
    #     password += p
    
    # The above 3 lines code from line 38 to line 40 is being replaced by the below 1 line of code using join() function:
    password = "".join(password_list)        # joined all the element available inside the python_list into a single string.

    return password
    