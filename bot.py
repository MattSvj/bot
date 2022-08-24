import telebot, random, time

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
    time.sleep(3)


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
    elif pole[0][0] != "*" and pole[0][1] != "*" and pole[0][2] != "*" and pole[1][0] != "*" and pole[2][0] != "*" and pole[1][1] != "*" and pole[2][2] != "*" and pole[1][2] != "*" and pole[2][1] != "*":
        return False


def check_move(message):
    global move
    x, y = map(int, message.text.split())
    if pole[x - 1][y - 1] == "*":
        pole[x - 1][y - 1] = signs[move]
        move = (move + 1) % 2


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


@bot.message_handler(commands=['play'])
def play(message):
    global flag, move
    flag = 1
    while not Finish():
        ShowBoard(message)
        if move % 2 == 0:
            send = bot.send_message(message.chat.id, 'Введите координаты')
            bot.register_next_step_handler(send, check_move)
            bot.send_message(message.chat.id, 'У вас 10 секунд')
            sec = 0
            while sec < 11:
                if sec > 7:
                    bot.send_message(message.chat.id, 'У вас осталось ' + str(11 - sec))
                time.sleep(1)
                sec += 1
        else:
            x, y = random.choice([0, 1, 2]), random.choice([0, 1, 2])
            if pole[x][y] == "*":
                pole[x][y] = "0"
                move = (move + 1) % 2
    ShowBoard(message)
    bot.send_message(message.chat.id, 'Победил ' + players[(move + 1) % 2] + '!')


# Запускаем бота
bot.polling(none_stop=True, interval=0)