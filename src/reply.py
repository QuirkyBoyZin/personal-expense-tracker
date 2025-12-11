from helper import(
    view_expense,
    get_item
)

#### Constants or functions for replying message to user ####

### Warning message if user enter anything other than the list of commands that can be used

WARNING = f"Here is a list of commands you can use"

### Using /start

WELCOME = f"I am your expense tracker. Ready to log in?"

### Using /add

ADD_USAGE = ("Please enter your expense in this format:\n\n"
               "Format:  \t\t\t\t\t\t Type       Name      Price in (USD)\n"
               "Exmaple:       Food      Noodle           2.5" )


def validate_add(condition: str, message: list) -> str:
    """ Validating /add cammand returns a validation message.\n
        condition's arguments:\n 
        success\n
        missing_args\n
        excessive_args\n
        category\n
        name\n
        price\n
    """
    if len(message) == 3:
        category: str = message[0]
        name:     str = message[1]
        price:    str = message[2]

    if condition == "success":
        recently_added = f"{category.capitalize()} {name.capitalize()} {price.capitalize()}"
        return f"Sucessfully added -- {recently_added} -- \n" 
    
    elif condition == "missing_args":
        return (f"Missing arguments for -- {" ".join(message)} --. \n\n"
                    "Usage:  \t\t\t\t\t\t Category       Name      Price in (USD)\n"
                    "Example:       Food      Noodle           2.5" )
    
    elif condition == "excessive_args":
         return (f"Excessive arguments for -- {" ".join(message)} --. \n\n"
                    "Usage:  \t\t\t\t\t Category       Name      Price in (USD)\n"
                    "Example:       Food      Noodle           2.5" ) 

    elif condition == "category":
        return f"Invalid Category: -- {category} --. Please enter text" 

    elif condition == "name":
        return f"Invalid Name: -- {name} --. Please enter text"

    elif condition == "price":
        return f"Invalid Price: -- {price} --. Please enter numbers"
    
    else: 
        return f"Error, Please try again."


### Using /view

VIEW_USAGE  = f"Here is your list of expenses for today\n"

### Using /remove

REMOVE= "Which item do you want to remove?"

REMOVE_USAGE= "Enter an ID from the list to remove\n"

def validate_remove(condition, message):
    if condition == "text":
         return f"Invalid ID: -- {message} --.Please enter an ID"
    
    elif condition == "id":
         return f"-- {message} -- is not on the list. Please try again."
    elif condition == 'empty':
         return f"You don't have anything to remove!"
    
    elif condition == 'success':
         return f"Sucessfully removed -- {get_item(int(message))} --"

### Using /change

CHANGE = "Which item do you want to change?\n"

CHANGE_USAGE= "Enter an ID from the list to change\n"

def validate_change(condition,message):
    if condition == "text":
         return f"Invalid ID: -- {message} --.Please enter an ID"
    
    elif condition == "id":
         return f"-- {message} -- is not on the list. Please try again."
    
    elif condition == 'empty':
         return f"You don't have anything to change!"
    
    elif condition == 'invalid_category':
         return f"Invalid Category: --- {message} --- Category must be a text!"
    
    elif condition == 'invalid_name':
         return f"Invalid Name: --- {message} --- Name must be a text!"
    
    elif condition == 'invalid_price':
         return f"Invalid Price: --- {message} --- Price must be a number!"
    
    elif condition == 'success':
         return f"Sucessfully changed -- {get_item(int(message))} -- "

def to_change(message):
    return f"What to change for -- {get_item(int(message))} -- ?"

### Using /help

HELP = (
            "/add:    \t\t\t\t\t\t Add an item to your expense\n\n"
            "/view:   \t\t\t\t\t\t View your expense list\n\n"
            "/remove: \t\t Remove an item in your expense list\n\n"
            "/change: \t\t Changing an item in your expense\n\n"
            "/help:   \t\t\t\t\t\t Show a list of commands\n\n"
            "/quit:   \t\t\t\t\t\t Leave a command")




if __name__ == "__main__":
    # print(add_successful(['food', 'noodle', '2.5']))
    pass