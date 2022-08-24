import telebot

# Создаем экземпляр бота
bot = telebot.TeleBot('5516639636:AAEUTCmuRKYxl25I9muyFHADWIHegKyyq-s')

pole = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
move = 0
players = ['Человек', "Бот"]
signs = ['x', '0']
flag = 0

def ShowBoard(message):
    string = ""
    for i in pole:
        string += "".join(i) + '\n'
    bot.send_message(message.chat.id, string)
    bot.send_message(message.chat.id, "Ходит " + players[move] + ' (' + signs[move] + ').')


def Finish():
    global flag
    if pole[0][0] == pole[0][1] == pole[0][2] == 'x' or pole[0][0] == pole[1][1] == pole[2][2] == 'x' or pole[0][
        0] == \
            pole[1][0] == pole[2][0] == 'x' or pole[0][0] == pole[1][0] == pole[2][0] == 'x' or pole[0][2] == \
            pole[1][
                2] == pole[2][2] == 'x' or pole[0][0] == pole[1][1] == pole[2][2] == 'x' or pole[0][2] == pole[1][
        1] == pole[2][
        0] == 'x' or pole[2][0] == pole[2][1] == pole[2][2] == 'x':
        return True
    elif pole[0][0] == pole[0][1] == pole[0][2] == '0' or pole[0][0] == pole[1][1] == pole[2][2] == '0' or pole[0][
        0] == \
            pole[1][0] == pole[2][0] == '0' or pole[0][0] == pole[1][0] == pole[2][0] == '0' or pole[0][2] == \
            pole[1][
                2] == pole[2][2] == '0' or pole[0][0] == pole[1][1] == pole[2][2] == '0' or pole[0][2] == pole[1][
        1] == pole[2][
        0] == '0' or pole[2][0] == pole[2][1] == pole[2][2] == '0':
        return True
    return False


def check_move(message):
    x, y = map(int, message.split())
    if pole[x - 1][y - 1] == "*":
        return True


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


@bot.message_handler(commands=['play'])
def play(message):
    global flag
    flag = 1
    while not Finish():
        global move
        ShowBoard(message)
        if move % 2 == 0:
            bot.send_message(message.chat.id, 'Введите координаты')
        if check_move(a - 1, b - 1):
            pole[a - 1][b - 1] = signs[move]
            move = (move + 1) % 2
    print('Победил ' + players[(move + 1) % 2] + '!')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if flag == 1:
        bot.register_next_step_handler(bot.send_message(message.chat.id, 'Введите координаты'), play)


# Запускаем бота
bot.polling(none_stop=True, interval=0)