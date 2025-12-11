import reply
from t_bot.bot import bot
from helper import find_id
from g_sheets import sheets
from datetime import datetime


def validate_view(date):
    expense = sheets.get_expenses_at(date)
    return expense != [] ## Returns false if empty

def validate_add(expense, message, func) -> bool:
    """ Validate expense before adding if passes return true else send 
        a message to user about their mistake"""

    # Missing arguments
    if  len(expense)  < 3:

        bot.send_message(message.chat.id, reply.validate_add("missing_args", expense))
        bot.register_next_step_handler(message, func)
        return
    
    # Excessive arguments
    elif len(expense) > 3: 
        
        bot.send_message(message.chat.id, reply.validate_add("excessive_args", expense))
        bot.register_next_step_handler(message, func)
        return
    
    # Checking if category is string, name is string and price is a float
    invalid_category = True
    invalid_name     = True
    invalid_price    = False
    
    category: str    = expense[0]
    name:     str    = expense[1]
    price:    float  = expense[2]
    
    try:
        float(category)
    except ValueError:
        invalid_category = False
    
    try:
        float(name)
    except ValueError:
        invalid_name = False
    
    try:
        float(price)
    except ValueError:
        invalid_price = True
    
      
    if invalid_category:
        
        bot.send_message(message.chat.id, reply.validate_add('category', expense))
        bot.register_next_step_handler(message, func)  
        return
 
    elif invalid_name:
        
        bot.send_message(message.chat.id, reply.validate_add('name', expense))
        bot.register_next_step_handler(message, func)  
        return
    
    elif invalid_price:
        
        bot.send_message(message.chat.id, reply.validate_add('price', expense))
        bot.register_next_step_handler(message, func)
        return
    
    bot.send_message(message.chat.id, reply.validate_add('success', expense))
    return True

def validate_remove(message, func) -> tuple[bool,int]:
    """ 
        Validate before removing if passes return true else send 
        a message to user about their mistake
    """
    
    # Checking if index is an int
    invalid_index = False
    try:
        index = int(message.text)
    except ValueError:
        invalid_index = True

    if invalid_index:
        bot.send_message(message.chat.id, reply.validate_remove("text", message.text))
        bot.register_next_step_handler(message, func)
        return (False, False)

    # index must be [1, len(list of expense)]
    id = find_id(index)
    if id is False:
        bot.send_message(message.chat.id, reply.validate_remove("id", message.text))
        bot.register_next_step_handler(message, func)
        return (False, False)
    
    bot.send_message(message.chat.id, reply.validate_remove('success', message.text))
    return (True, id)

def validate_change_id(message,func):
    """
        Validate changes before making the change in database 
        and inform user about their mistakes
    """
    # Checking if index is an int
    invalid_index = False
    try:
        index = int(message.text)
    except ValueError:
        invalid_index = True

    if invalid_index:
        bot.send_message(message.chat.id, reply.validate_change("text", message.text))
        bot.register_next_step_handler(message, func)
        return (False, None)

    # index must be [1, len(list of expense)]
    id = find_id(index)
    if id is False:
        bot.send_message(message.chat.id, reply.validate_change("id", message.text))
        bot.register_next_step_handler(message, func)
        return (False, None)
    
    return (True,id)
    
def validate_change_btns(message, btn, func) -> bool:
    """
        Validate the new category name and id entered by the user
        returns true if it's valid, otherwise false
    """
    valid          = True
    invalid_category = True
    invalid_name     = True
    invalid_price  = False
    
    if btn == "/category":
        new_category = message.text
        try:
            float(message.text)
        except ValueError:
            invalid_category = False
        
        if invalid_category is True:
            bot.send_message(message.chat.id, reply.validate_change("invalid_category", message.text))
            bot.register_next_step_handler(message, lambda call: func(call, btn)) 
            return (not valid, None)
        
        else: return (valid, new_category)
    
    elif btn == "/name":
        new_name = message.text
        try:
            float(message.text)
        except ValueError:
            invalid_name = False
        
        if invalid_name is True:
            bot.send_message(message.chat.id, reply.validate_change("invalid_name", message.text))
            bot.register_next_step_handler(message, lambda call: func(call, btn)) 
            return (not valid, None)
        
        else: return (valid, new_name)
    
    elif btn == "/price":
        new_price = message.text
        try:
            float(message.text)
        except ValueError:
            invalid_price = True
        
        if invalid_price is True:
            bot.send_message(message.chat.id, reply.validate_change("invalid_price", message.text))
            bot.register_next_step_handler(message, lambda call: func(call, btn)) 
            return (not valid, None)
        
        else: return (valid, new_price)

    return
        
        

if __name__ == "__main__":
    date = "2025-12-05"
    print(validate_view(date))