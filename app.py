import telebot
from telebot import types

import csv
#TOKEN = '5489671847:AAHiKOJZOHcLMF1zhaV_w7ZxbUniJOe5Fj0'
#TOKEN = '5576007213:AAF_6bhIYghrDiIIc7fAOuH6mMvvjhwjt4o' # мой тест
#TOKEN = '5485790364:AAFYy221sHSiJiDlRVWiZTumHjsEQNRJPNs' # мой тестовый
TO_CHAT_ID = '290065001'
bot = telebot.TeleBot(TOKEN)





def after_text_2(message):
    print(message.content_type)
    #bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    #https://qna.habr.com/q/926275

    if message.content_type == "document" or message.content_type == "photo":
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id,
                               'Документ отправлен, напишите коментарий',
                               reply_markup=markup)
        bot.register_next_step_handler(msg, after_text_2)


    elif message.content_type == "text" and message.text == "Вариант1":
        print("tutu1")
        bot_message(message)
    elif message.content_type == "text" and message.text == "Вариант2":
        print("tutu2")
        bot_message(message)
    elif message.content_type == "text" and message.text == "Вариант3":
        print("tutu3")
        bot_message(message)
    elif message.content_type == "text" and message.text == "Вариант4":
        print("tutu4")
        bot_message(message)


    elif message.content_type == "text":

        print(message)

        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('<- Назад', callback_data='est_vopros'))
        msg = bot.send_message(message.chat.id
                                       ,'Спасибо за обращение, информация передана нашему менеджеру.',
                                       reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id,
                         'В течении 10 часов он Вам ответит и решит Вашу проблему.',
                         reply_markup=markup1)
        #bot.register_next_step_handler(msg, after_text_2)



def after_text_1(message):
    print(message.content_type)
    #bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    #https://qna.habr.com/q/926275

    if message.content_type == "document" or message.content_type == "photo":
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('<- Назад', callback_data='nazad_glavnoe_menu'))
        msg = bot.send_message(message.chat.id,
                               'Отзыв отправлен!',
                               reply_markup=markup1)
        #bot.register_next_step_handler(msg, after_text_1)

    elif message.content_type == "text" and message.text == "Вариант1":
        print("tutu1")
        bot_message(message)
    elif message.content_type == "text" and message.text == "Вариант2":
        print("tutu2")
        bot_message(message)
    elif message.content_type == "text" and message.text == "Вариант3":
        print("tutu3")
        bot_message(message)
    elif message.content_type == "text" and message.text == "Вариант4":
        print("tutu4")
        bot_message(message)
    elif message.content_type == "text":
        message.text = ''
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('<- Назад', callback_data='nazad_glavnoe_menu'))
        msg = bot.send_message(message.chat.id,
                                   'Прикрепите пожалуйста фото',
                                   reply_markup=markup1)
        bot.register_next_step_handler(msg, after_text_1)



@bot.message_handler(commands=['start']) # главное начало
def start(message):


    markup1 = types.InlineKeyboardMarkup()
    markup1.add(types.InlineKeyboardButton('Забрать бонус', callback_data='zabrat_bonus'))
    markup1.add(types.InlineKeyboardButton('Есть вопрос?', callback_data='est_vopros'))
    bot.send_message(message.chat.id,
                     'привет,{0.first_name}! \n Благодарим Вас за покупку и желаем Вам отличного настроения! Желаете забрать свой бонус 💰или у Вас есть проблемы по товару?🤔'.format(
                         message.from_user), reply_markup=markup1)


# @bot.message_handler(content_types=['text'])
# def bot_message(message):
#     global answer
#     if message.chat.type == 'private':
#         if message.text == 'Забрать бонус':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             item1 = types.KeyboardButton('Wildberries')
#             back = types.KeyboardButton('<- Назад')
#             markup.add(item1,back)
#             bot.send_message(message.chat.id, 'На какой площадке Вы сделали покупку?',reply_markup=markup)
#
#         elif message.text == 'Wildberries':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             back = types.KeyboardButton('<- Назад')
#             markup.add( back)
#             bot.send_message(message.chat.id, 'Для получения бонуса 🤑 Вам нужно: \n⭕️Написать отзыв о купленном товаре⭐️⭐️⭐️⭐️⭐️ и получить 150р. на телефон или СБП 📲. \n⭕️Написать отзыв о купленном товаре, прикрепить фотографию к отзыву и получить 200р. на телефон или СБП 📲. \n🔜 📌Сделать скриншот оставленного вами отзыва и прикрепить в наш чат-бот следующим сообщением!!!', reply_markup=markup)
#             msg = bot.send_message(message.chat.id, 'Прикрепите, пожалуйста, скриншот отзыва для получения бонуса!', reply_markup=markup)
#             bot.register_next_step_handler(msg, after_text_1)
#             #bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
#
#         elif message.text =='<- Назад':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             item1 = types.KeyboardButton('Забрать бонус')
#             item2 = types.KeyboardButton('Есть вопрос?')
#             markup.add(item1, item2)
#             bot.send_message(message.chat.id, '{0.first_name}!Благодарим Вас за покупку и желаем Вам отличного настроения! Желаете забрать свой бонус 💰или у Вас есть проблемы по товару?🤔'.format(message.from_user), reply_markup=markup)
#
#         elif message.text == 'Есть вопрос?':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             item1 = types.KeyboardButton('Вариант1')
#             item2 = types.KeyboardButton('Вариант2')
#             item3 = types.KeyboardButton('Вариант3')
#             item4 = types.KeyboardButton('Вариант4')
#             back = types.KeyboardButton('<- Назад')
#             markup.add(item1,item2,item3,item4,back)
#             bot.send_message(message.chat.id, 'Выберите подходящую тему для Вас👇🏻\n1️⃣Качество, состав изделия\n2️⃣Параметры и замеры изделия\n3️⃣Наличие товара4️\n4️⃣Возник другой вопрос или проблема.', reply_markup=markup)
#
#
#         elif message.text == 'Вариант1':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             back = types.KeyboardButton('<- Назад')
#             markup.add(back)
#             msg = bot.send_message(message.chat.id,
#                              'Опишите, пожалуйста, проблему с которой Вы столкнулись. Мы ответим на все Ваши вопросы и с радостью решим любую Вашу проблему.',
#                              reply_markup=markup)
#             bot.send_message(message.chat.id,'❗️Для более качественного и подробного ответа, Вы можете прикреплять фотографии и артикул товара, по которому есть вопрос.',reply_markup=markup)
#
#             bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
#             bot.register_next_step_handler(msg, after_text_2)
#         elif message.text == 'Вариант2':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             back = types.KeyboardButton('<- Назад')
#             markup.add(back)
#             msg = bot.send_message(message.chat.id,
#                                    'Опишите, пожалуйста, проблему с которой Вы столкнулись. Мы ответим на все Ваши вопросы и с радостью решим любую Вашу проблему. \n❗️Для более качественного и подробного ответа, Вы можете прикреплять фотографии и артикул товара, по которому есть вопрос.',
#                                    reply_markup=markup)
#
#             bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
#             bot.register_next_step_handler(msg, after_text_2)
#         elif message.text == 'Вариант3':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             back = types.KeyboardButton('<- Назад')
#             markup.add(back)
#             msg = bot.send_message(message.chat.id,
#                                    'Опишите, пожалуйста, проблему с которой Вы столкнулись. Мы ответим на все Ваши вопросы и с радостью решим любую Вашу проблему. \n❗️Для более качественного и подробного ответа, Вы можете прикреплять фотографии и артикул товара, по которому есть вопрос.',
#                                    reply_markup=markup)
#             bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
#             bot.register_next_step_handler(msg, after_text_2)
#         elif message.text == 'Вариант4':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             back = types.KeyboardButton('<- Назад')
#             markup.add(back)
#             msg = bot.send_message(message.chat.id,
#                                    'Опишите, пожалуйста, проблему с которой Вы столкнулись. Мы ответим на все Ваши вопросы и с радостью решим любую Вашу проблему. \n❗️Для более качественного и подробного ответа, Вы можете прикреплять фотографии и артикул товара, по которому есть вопрос.',
#                                    reply_markup=markup)
#             bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
#             bot.register_next_step_handler(msg, after_text_2)
#
#             #https://ru.stackoverflow.com/questions/1254633/%D0%BA%D0%B0%D0%BA-%D0%BF%D1%80%D0%B8%D0%BD%D0%B8%D0%BC%D0%B0%D1%82%D1%8C-%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9-%D1%82%D0%B5%D0%BA%D1%81%D1%82-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F-%D1%82%D0%B5%D0%BB%D0%B5%D0%B3%D1%80%D0%B0%D0%BC-%D0%B1%D0%BE%D1%82-python-telebot

@bot.message_handler(content_types=['text'])
def bot_message(message):
    global answer
    if message.chat.type == 'private':
        if message.text =='<- Назад':
            markup1 = types.InlineKeyboardMarkup()
            markup1.add(types.InlineKeyboardButton('Забрать бонус', callback_data='zabrat_bonus'))
            markup1.add(types.InlineKeyboardButton('Есть вопрос?', callback_data='est_vopros'))
            bot.send_message(message.chat.id,
                             'привет,{0.first_name}!'.format(
                                 message.from_user), reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id,
                             'Благодарим Вас за покупку и желаем Вам отличного настроения! Желаете забрать свой бонус 💰или у Вас есть проблемы по товару?🤔'.format(
                                 message.from_user), reply_markup=markup1)

        elif message.text == 'Вариант1':

            markup1 = types.InlineKeyboardMarkup()
            markup1.add(types.InlineKeyboardButton("<- Назад", callback_data='back_to_vopros'))
            msg = bot.send_message(message.chat.id,
                             'Опишите, пожалуйста, проблему с которой Вы столкнулись. Мы ответим на все Ваши вопросы и с радостью решим любую Вашу проблему.',
                             reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id,'❗️Для более качественного и подробного ответа, '
                                             'Вы можете прикреплять фотографии и артикул товара, по которому есть вопрос.',reply_markup=markup1)

            bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
            bot.register_next_step_handler(msg, after_text_2)

        elif message.text == 'Вариант2':

            markup1 = types.InlineKeyboardMarkup()
            markup1.add(types.InlineKeyboardButton("<- Назад", callback_data='back_to_vopros'))
            msg = bot.send_message(message.chat.id,
                             'Опишите, пожалуйста, проблему с которой Вы столкнулись. Мы ответим на все Ваши вопросы и с радостью решим любую Вашу проблему.',
                             reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id,'❗️Для более качественного и подробного ответа, '
                                             'Вы можете прикреплять фотографии и артикул товара, по которому есть вопрос.',reply_markup=markup1)

            bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
            bot.register_next_step_handler(msg, after_text_2)

        elif message.text == 'Вариант3':

            markup1 = types.InlineKeyboardMarkup()
            markup1.add(types.InlineKeyboardButton("<- Назад", callback_data='back_to_vopros'))
            msg = bot.send_message(message.chat.id,
                             'Опишите, пожалуйста, проблему с которой Вы столкнулись. Мы ответим на все Ваши вопросы и с радостью решим любую Вашу проблему.',
                             reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id,'❗️Для более качественного и подробного ответа, '
                                             'Вы можете прикреплять фотографии и артикул товара, по которому есть вопрос.',reply_markup=markup1)

            bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
            bot.register_next_step_handler(msg, after_text_2)

        elif message.text == 'Вариант4':

            markup1 = types.InlineKeyboardMarkup()
            markup1.add(types.InlineKeyboardButton("<- Назад", callback_data='back_to_vopros'))
            msg = bot.send_message(message.chat.id,
                             'Опишите, пожалуйста, проблему с которой Вы столкнулись. Мы ответим на все Ваши вопросы и с радостью решим любую Вашу проблему.',
                             reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id,'❗️Для более качественного и подробного ответа, '
                                             'Вы можете прикреплять фотографии и артикул товара, по которому есть вопрос.',reply_markup=markup1)

            bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
            bot.register_next_step_handler(msg, after_text_2)



@bot.callback_query_handler(func=lambda callback: True)
def inline(callback):
    if callback.data == 'zabrat_bonus':
        print('забрать бонус')
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Wildberries', callback_data='wildberries'))
        markup1.add(types.InlineKeyboardButton('<- Назад', callback_data='nazad_glavnoe_menu'))
        bot.send_message(callback.message.chat.id, 'На какой площадке Вы сделали покупку?', reply_markup=markup1)



    elif callback.data == 'est_vopros':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup1 = types.InlineKeyboardMarkup()
        item1 = types.KeyboardButton('Вариант1')
        item2 = types.KeyboardButton('Вариант2')
        item3 = types.KeyboardButton('Вариант3')
        item4 = types.KeyboardButton('Вариант4')
        back = types.KeyboardButton('<- Назад')
        markup1.add(types.InlineKeyboardButton('<- Назад', callback_data='nazad_glavnoe_menu'))
        markup.add(item1, item2, item3, item4)
        bot.send_message(callback.message.chat.id,
                         'Выберите подходящую тему для Вас👇🏻',
                         reply_markup=markup)
        bot.send_message(callback.message.chat.id,
                         '1️⃣Качество, состав изделия\n2️⃣Параметры и замеры изделия\n3️⃣Наличие товара4️\n4️⃣Возник другой вопрос или проблема.',
                         reply_markup=markup1)


    elif callback.data == 'nazad_glavnoe_menu':

        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Забрать бонус', callback_data='zabrat_bonus'))
        markup1.add(types.InlineKeyboardButton('Есть вопрос?', callback_data='est_vopros'))
        bot.send_message(callback.message.chat.id,
                         '{0.first_name}!'.format(
                             callback.message.from_user),reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(callback.message.chat.id,
                         'Благодарим Вас за покупку и желаем Вам отличного настроения! Желаете забрать свой бонус 💰или у Вас есть проблемы по товару?🤔'.format(
                             callback.message.from_user), reply_markup=markup1)




    elif callback.data == 'wildberries':
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('<- Назад', callback_data='nazad_glavnoe_menu'))
        msg = bot.send_message(callback.message.chat.id,
                         'Для получения бонуса 🤑 Вам нужно: \n⭕️Написать отзыв о купленном товаре⭐️⭐️⭐️⭐️⭐️ и получить 150р. на телефон или СБП 📲. \n⭕️Написать отзыв о купленном товаре, прикрепить фотографию к отзыву и получить 200р. на телефон или СБП 📲. \n🔜 📌Сделать скриншот оставленного вами отзыва и прикрепить в наш чат-бот следующим сообщением!!! Прикрепите, пожалуйста, скриншот отзыва для получения бонуса!',
                         reply_markup=markup1)
        bot.register_next_step_handler(msg, after_text_1)


    elif callback.data == 'var1':
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('<- Назад', callback_data='est_vopros'))
        msg = bot.send_message(callback.message.chat.id,
                               'Опишите, пожалуйста, проблему с которой Вы столкнулись. Мы ответим на все Ваши вопросы и с радостью решим любую Вашу проблему. ❗️Для более качественного и подробного ответа, Вы можете прикреплять фотографии и артикул товара, по которому есть вопрос.',
                               reply_markup=markup1)
        bot.forward_message(TO_CHAT_ID, callback.message.chat.id, callback.message.message_id)
        bot.register_next_step_handler(msg, after_text_2)






    elif callback.data == 'var2':

        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('<- Назад', callback_data='est_vopros'))
        msg = bot.send_message(callback.message.chat.id,
                               'Опишите, пожалуйста, проблему с которой Вы столкнулись. Мы ответим на все Ваши вопросы и с радостью решим любую Вашу проблему. ❗️Для более качественного и подробного ответа, Вы можете прикреплять фотографии и артикул товара, по которому есть вопрос.',
                               reply_markup=markup1)
        bot.forward_message(TO_CHAT_ID, callback.message.chat.id, callback.message.message_id)
        bot.register_next_step_handler(msg, after_text_2)
    elif callback.data == 'var3':

        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('<- Назад', callback_data='est_vopros'))
        msg = bot.send_message(callback.message.chat.id,
                               'Опишите, пожалуйста, проблему с которой Вы столкнулись. Мы ответим на все Ваши вопросы и с радостью решим любую Вашу проблему. ❗️Для более качественного и подробного ответа, Вы можете прикреплять фотографии и артикул товара, по которому есть вопрос.',
                               reply_markup=markup1)
        bot.forward_message(TO_CHAT_ID, callback.message.chat.id, callback.message.message_id)
        bot.register_next_step_handler(msg, after_text_2)
    elif callback.data == 'var4':

        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('<- Назад', callback_data='est_vopros'))
        msg = bot.send_message(callback.message.chat.id,
                               'Опишите, пожалуйста, проблему с которой Вы столкнулись. Мы ответим на все Ваши вопросы и с радостью решим любую Вашу проблему. ❗️Для более качественного и подробного ответа, Вы можете прикреплять фотографии и артикул товара, по которому есть вопрос.',
                               reply_markup=markup1)
        bot.forward_message(TO_CHAT_ID, callback.message.chat.id, callback.message.message_id)
        bot.register_next_step_handler(msg, after_text_2)







bot.polling(none_stop=True)
