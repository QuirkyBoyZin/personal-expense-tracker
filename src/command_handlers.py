import reply
from t_bot.bot import bot
from validate import(
    validate_add,
    validate_remove,
    validate_view,
    validate_change_id,
    validate_change_btns
    
)
from buttons import (
    make_btns
)
from state   import user_state
from g_sheets import sheets
from helper   import (
    view_expense,   
)
from datetime import datetime


date     = datetime.now().strftime("%Y-%m-%d")
commands = ('/add', '/view', '/remove','/change', '/help')


def handle_quit(message):
    chat_id = message.chat.id
   
    if message.text == "/quit":
        user_state.pop(chat_id, None)
        bot.send_message(chat_id, f"What do you want to do next?", reply_markup= make_btns(*commands))
        return True
    return False

def handle_start(message):
    bot.send_message(message.chat.id, f'Here are a list of commands you can use', reply_markup= make_btns(*commands)) 
    return

def handle_add(message):
    chat_id = message.chat.id
    expense = message.text.split()
   
    if handle_quit(message):
        return
   
    valid = validate_add(expense, message, handle_add)
   
    
    if valid:
        bot.send_message(message.chat.id, f'What do you want to do next?', reply_markup= make_btns(*commands))
        user_state.pop(chat_id, None)
        sheets.add_row(expense[0], expense[1], expense[2])

    return

def handle_view(message,date):
    commands = ('/add', '/remove','/change')
    valid = validate_view(date)
    
    if not valid:
        bot.send_message(message.chat.id, f"You haven't note down anything yet!")   
        bot.send_message(message.chat.id, view_expense(), parse_mode= "Markdown" )
        return
        
    bot.send_message(message.chat.id, f"Here is your list of expense for today")
    bot.send_message(message.chat.id, view_expense(), parse_mode= "Markdown" )
    bot.send_message(message.chat.id, f'What do you want to do next?', reply_markup= make_btns(*commands))
    
    return
    

def handle_remove(message):
    chat_id = message.chat.id
    
    if handle_quit(message):
        return

    (valid,id) = validate_remove(message, handle_remove)
    
    if valid:
        bot.send_message(message.chat.id, f'What do you want to do next?', reply_markup= make_btns(*commands))
        user_state.pop(chat_id, None)
        sheets.remove_row(id)
        return

def handle_change(message):
    chat_id = message.chat.id
    global id

    if handle_quit(message):
        return

    
    (valid,id) = validate_change_id(message, handle_change) 

    # if validating pass, Sends buttons to user category name price
    if valid:
        user_state.pop(chat_id, None)
        change_btns = ('/category', '/name', '/price', '/quit')
        bot.send_message(message.chat.id, reply.to_change(message.text), reply_markup= make_btns(*change_btns))
    
    return
    
def handle_change_btns(message, btn):
    """
        This function will only be called when hand handle_change is valid
    """
    
    chat_id = message.chat.id
    
    if handle_quit(message):
        return
    
    (change_valid, new) = validate_change_btns(message, btn, handle_change_btns)
    
  
    
    if change_valid and btn == "/category":
        
        user_state.pop(chat_id, None)
        change_more = ('/name','/price', '/quit')
        bot.send_message(message.chat.id, f'Sucessfully changed Category to --- {new.capitalize()} ---')
        bot.send_message(message.chat.id, f'Wanna change anything else?', reply_markup= make_btns(*change_more))
        sheets.change_row(id, new_type= new )
    
    elif change_valid and btn == "/name":
        
        user_state.pop(chat_id, None)
        change_more = ('/category','/price', '/quit')
        bot.send_message(message.chat.id, f'Sucessfully changed Name to --- {new.capitalize()} ---')
        bot.send_message(message.chat.id, f'Wanna change anything else?', reply_markup= make_btns(*change_more))
        sheets.change_row(id, new_name= new )
        
    elif change_valid and btn == "/price":
        
        user_state.pop(chat_id, None)
        change_more = ('/category','/name', '/quit')
        bot.send_message(message.chat.id, f'Sucessfully changed Price to --- {new} ---')
        bot.send_message(message.chat.id, f'Wanna change anything else?', reply_markup= make_btns(*change_more))
        sheets.change_row(id, new_price= new )

    return

if __name__ == '__main__':
    
    pass
