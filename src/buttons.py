from t_bot.bot import bot
from telebot import types


### Buttons for interaction

add     = types.InlineKeyboardButton('Add',    callback_data= '/add')
view    = types.InlineKeyboardButton('View',   callback_data= '/view')
remove  = types.InlineKeyboardButton('Remove', callback_data= '/remove')
change  = types.InlineKeyboardButton('Change', callback_data= '/change')
help    = types.InlineKeyboardButton('Help',   callback_data= '/help')

btn = {'/add': add,'/view': view,'/remove': remove,'/change': change,'/help': help}


def make_btns(*args) -> types.InlineKeyboardMarkup:
    """
        given an arbitrary of args\n
        Makes button in a container with row width of 1\n
        with the given args
    """
    btns = []
    container = types.InlineKeyboardMarkup(row_width=1)
    
    for command in args:
        name: str = command[1:]
        btn = types.InlineKeyboardButton(name.capitalize(), callback_data= command)
        btns.append(btn)
    tuple(btns)
    return container.add(*btns)

if __name__ == '__main__':
    btns= ['/add', '/view', '/remove','/change', '/help']
    make_btns(*btns)
   
    pass



