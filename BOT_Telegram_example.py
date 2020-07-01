"""
Created on Sun Nov 24 14:36:04 2019

@author: Agnese Portera
"""


import telepot
import time
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

global query_reminder
query_reminder = 0


def on_chat_message(msg): #create a personalized keyboard
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="BUTTON 1", callback_data='/button1'), InlineKeyboardButton(text="BUTTON 2", callback_data='/button2')],
                                     [InlineKeyboardButton(text="BUTTON 3", callback_data='/button3'), InlineKeyboardButton(text="SET TIME", callback_data='/button4')]])
    
    global query_reminder
    print('the reminder variable is: ', query_reminder)
    if content_type == 'text' and query_reminder == 1:
        query_reminder = 0
        try:
            time_object = time.strptime(msg['text'], '%H:%M')
            bot.sendMessage(chat_id, f"Please set a time: {msg['text']}")
        except ValueError as e:
            print('ValueError:', e)
            bot.sendMessage(chat_id,f"Uncorrect time value: time data {msg['text']} does not match format '%H:%M'")
        
        print(f"String received: {msg['text']}")
        
    bot.sendMessage(chat_id, 'Hello! Your menu:', reply_markup=keyboard)
            

def on_callback_query(msg): #query management
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    
    if query_data == '/button1':
        bot.answerCallbackQuery(query_id, text='Button 1 clicked')
    elif query_data == '/button2':
        bot.answerCallbackQuery(query_id, text='Button 2 clicked')               
    elif query_data == '/button3':
        bot.sendMessage(from_id, 'Button 3 clicked')
    elif query_data == '/button4':
        bot.sendMessage(from_id, 'Set time example')
        global query_reminder
        query_reminder = 1
        

bot=telepot.Bot('123456xxxxxxx') #BOT token from BOT Father
print('bot collegato')
bot.message_loop({'chat': on_chat_message,
                  'callback_query': on_callback_query})
print ('Listening ...')


while 1:
    time.sleep(10)
