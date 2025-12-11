from t_bot.bot    import bot
import reply
from helper import(
    measure_perf,
    view_expense
)
from command_handlers import(
    handle_start,
    handle_add, 
    handle_view,
    handle_remove,
    handle_change,
    handle_change_btns
)
from buttons import make_btns
from validate import validate_view
from state import user_state
from datetime import datetime

commands= ['/start', '/add', '/view', '/remove','/change', '/help']
date     = datetime.now().strftime("%Y-%m-%d")
  
@bot.message_handler(func= lambda msg: msg.text not in commands)  # Validating Commands & Messages
@measure_perf
def warning(message):
    """ Shows a list of command to use if a user enter non-commands text"""
    handle_start(message)
    return 
    

###--------------------------------------------------------------###

### Handling user's commands

@bot.message_handler(commands=['start','add','view', 'remove', 'change', 'help'])
@measure_perf
def command_handlers(message):
    chat_id = message.chat.id
    if message.text == '/start':
        # Welcomes user and show a list of commands to use
        bot.send_message(message.chat.id, reply.WELCOME)
        handle_start(message)
        
        return
    # Let user add their expense 
    elif message.text == "/add":
        user_state[chat_id] = "add"  
        
        bot.send_message(message.chat.id, reply.ADD_USAGE )
        bot.register_next_step_handler(message, handle_add)
        return
    
    elif message.text == "/view":
        handle_view(message,date)
        
        return
    
    elif message.text == "/remove":
        user_state[chat_id] = "remove"  

        if validate_view(date) is False:
              bot.send_message(message.chat.id, reply.validate_remove('empty',message))
              user_state.pop(chat_id, None)
              return 

        bot.send_message(message.chat.id, reply.REMOVE) 
        bot.send_message(message.chat.id, view_expense(), parse_mode= "Markdown" )
        bot.send_message(message.chat.id, reply.REMOVE_USAGE )
        bot.register_next_step_handler(message, handle_remove)
        
        return
    
    elif message.text == "/change":
        user_state[chat_id] = "change"  

        if validate_view(date) is False:
              bot.send_message(message.chat.id, reply.validate_change('empty',message))
              user_state.pop(chat_id, None)
              return 
    
        bot.send_message(message.chat.id, reply.CHANGE)
        bot.send_message(message.chat.id, view_expense(), parse_mode= "Markdown" )
        bot.send_message(message.chat.id, reply.CHANGE_USAGE )
        bot.register_next_step_handler(message, handle_change)
        
        return

    
    elif message.text == "/help":
        bot.send_message(message.chat.id, reply.HELP)
        
        return

change_callback = ['/category', '/name', '/price', '/quit']
callback = change_callback + commands
### Users clicking on buttons
@bot.callback_query_handler(func= lambda call: call.data in commands)
@measure_perf
def handle_btn(callback):

    chat_id = callback.message.chat.id
    # check if this user is currently in an active flow
    if user_state.get(chat_id) is None:
        # user is free, proceed
        callback.message.text = callback.data
        command_handlers(callback.message)
   
    elif callback.data == '/view':
        bot.send_message(chat_id,  view_expense(), parse_mode= 'Markdown')
    
    else:
        # user is mid-flow, block button
        bot.answer_callback_query(callback.id,  "❗ Please finish this task first.")

@bot.callback_query_handler(func= lambda call: call.data in callback )
@measure_perf
def handle_change_btn(callback):   
    
    chat_id = callback.message.chat.id
   
    if callback.data == '/category':
        # Set user state
        user_state[chat_id] = 'category'
        bot.send_message(chat_id, f"Please enter a new Category")   # Lambda function takes in callback.message assigning it to handle_change_btns then return back a function
        bot.register_next_step_handler(callback.message, lambda call: handle_change_btns(call, callback.data))
    
    elif callback.data == '/name':
        # Set user state
        user_state[chat_id] = 'name'
        bot.send_message(chat_id, f"Please enter a new Name")   # Lambda function takes in callback.message assigning it to handle_change_btns then return back a function
        bot.register_next_step_handler(callback.message, lambda call: handle_change_btns(call, callback.data))
    
    elif callback.data == '/price':
        # Set user state
        user_state[chat_id] = 'price'
        bot.send_message(chat_id, f"Please enter a new Price")   # Lambda function takes in callback.message assigning it to handle_change_btns then return back a function
        bot.register_next_step_handler(callback.message, lambda call: handle_change_btns(call, callback.data))

    elif callback.data == '/quit':
        user_state[chat_id] = None 
        bot.send_message(chat_id, f"Quiting...")   # Lambda function takes in callback.message assigning it to handle_change_btns then return back a function
        bot.send_message(chat_id, f"What do you want to do next?", reply_markup= make_btns(*commands[1:]))
    
    else:
        bot.answer_callback_query(callback.id,  "❗ Please finish this task first.")  
    return 
  
@bot.callback_query_handler(func= lambda call: call.data in callback)
@measure_perf
def handle_btn_task(callback):

    chat_id = callback.message.chat.id
    print(user_state.get(chat_id))
    # check if this user is currently in an active flow
    if user_state.get(chat_id) is None:
        # user is free, proceed
        callback.message.text = callback.data
        handle_change_btn(callback.message)
   
    elif callback.data == '/view':
        bot.send_message(chat_id,  view_expense(), parse_mode= 'Markdown')
    
    else:
        # user is mid-flow, block button
        bot.answer_callback_query(callback.id,  "❗ Please finish this task first.")  


print("Bot is running...")
bot.infinity_polling()
