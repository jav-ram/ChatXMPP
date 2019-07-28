import threading
import time
from blessed import Terminal

t = Terminal()

options = [
    ('h ', 'Volver a mostrar este menu'),
    ('mi', 'Mensaje individual'),
    ('mg', 'Mensaje a grupo'),
    ('ul', 'Lista de usuarios'),
    ('ui', 'Información de usuario individual'),
    ('au', 'Agregar usuario a mi lista de contactos'),
    ('q ', 'Desconectarme'),
    ('!q', 'Borrar cuenta'),
    # ('', ''),
]


def get_opt(target):
    for o in options:
        if target == o[0]:
            return target
    return None


def menu():
    print(t.bold('Menu de opciones:'))
    print('--------------------------------------')
    for o in options:
        print(t.bold(t.color(0)(o[0])) + '      ' + o[1])


def get_option(question=':'):
    return input(t.move(t.height - 1, 0) + question)


def switcher(opt, actions):
    if get_opt(opt) == None:
        print(t.color(9)('La opción no existe, pruebe con otra'))
        print('Si no sabe ingrese ' + t.bold(t.color(0)('h')) + ', para mas información')

    for o in options:
        if opt == o[0]:
            actions[opt]()


def OptionsMenu(h, mi, mg):
    args = {
        'h ': h,
        'mi': mi,
        'mg': mg,
    }
    menu()
    print(args)
    while True:
        option = get_option()
        switcher(option, args)
    #     print(self.args)
    #     switcher(option, self.args)

    return
