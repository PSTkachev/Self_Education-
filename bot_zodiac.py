#!/usr/bin/python3.3
import random
import telebot;
from telebot import types # Импортируем типы из модуля, чтобы создавать кнопки

bot = telebot.TeleBot('1212661447:AAHve1sQc_dRvjo_CLMjkqp4mMbCWvlWEsc');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")

        keyboard = types.InlineKeyboardMarkup()  # Готовим кнопки

        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(key_lev)
        key_mar = types.InlineKeyboardButton(text='Маргарита', callback_data='zodiac')
        keyboard.add(key_mar)

        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

first = ["Сегодня — идеальный день для новых начинаний.",
         "Оптимальный день для того, чтобы решиться на смелый поступок!",
         "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
         "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
         "Плодотворный день для того, чтобы разобраться с накопившимися делами."]

second = ["Но помните, что даже в этом случае нужно не забывать про", "Если поедете за город, заранее подумайте про",
          "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
          "Если у вас упадок сил, обратите внимание на",
          "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]

second_add = ["отношения с друзьями и близкими.",
              "работу и деловые вопросы, которые могут так некстати помешать планам.",
              "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
              "бытовые вопросы — особенно те, которые вы не доделали вчера.",
              "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]

third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
         "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
         "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
         "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
         "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]

@bot.callback_query_handler(func=lambda call: True) # Обработчик нажатий на кнопки

def callback_worker(call):
    if call.data == "zodiac": # Если нажали на одну из 12 кнопок — выводим гороскоп
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third) # Формируем гороскоп
        bot.send_message(call.message.chat.id, msg) # Отправляем текст в Телеграм

bot.polling(none_stop=True, interval=0)


"""
#кусок кода для работы в консоли
# выводим знаки зодиака
zodiac_signs = ["Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"]
i = 0
for n in zodiac_signs:
    i += 1
    print(i, '—', n)

# Спрашиваем у пользователя про его знак
zodiac = int(input("{blue}Введите число с номером знака зодиака: {endcolor}".format(blue="\033[96m", endcolor="\033[0m")))

# Если число введено верно — выдаём гороскоп
if 0 < zodiac < 13:
    print(random.choice(first), random.choice(second), random.choice(second_add), random.choice(third))
else:
    print("Вы ошиблись с числом, запустите программу ещё раз")
"""
