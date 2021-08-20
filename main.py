def calculator():
    print('Введи запрос, а я его вычислю')
    command = yield
    try:
        print(f'{command}={eval(command)}')
    except SyntaxError:
        print('Не понимаю, о чём вы.')


def bot():
    print('Привет, я бот, мои команды:')
    print('1) Привет')
    print('2) Калькулятор')
    while True:
        command = yield
        if command == 'Привет':
            print('Привет!')
        elif command == 'Калькулятор':
            yield from calculator()
        else:
            print('Не понимаю, о чём вы.')


test_bot = bot()
test_bot.send(None)

while True:
    try:
        test_bot.send(input('>>> '))
    except KeyboardInterrupt:
        break
