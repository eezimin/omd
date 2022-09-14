def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    def step2_umbrella():
        print("Утка-маляр взяла зонтик, но на подходе к бару на нее неожиданно свалился камень. "
              "У утки-маляра был раскрыт зонт?"
              )
        option = ''
        while option not in options:
            print('Выберите: {}/{}'.format(*options))
            option = input()
        if options[option]:
            print('Поздравляем!!! Зонт выдержал камень!\n...У утки произошел шок. '
                  'Утка-маляр скончалась.')
        else:
            print('Ничего страшного! Камень упал мимо утки, она даже и не заметила.\n'
                  'Утка успешно вошла в бар и напилась. Доза оказалась несопоставимой '
                  'с жизнью. Утка-маляр скончалась.')

    def step2_no_umbrella():
        print("На утку свалился камень, повреждения оказались несопоставимы с жизнью. "
              "Утка-маляр скончалась.")

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

if __name__ == '__main__':
    step1()
