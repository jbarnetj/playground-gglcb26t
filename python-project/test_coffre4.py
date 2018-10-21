import random
import builtins
import time
import os

anc_input = builtins.input
échec = True


entrées = [random.randrange(0, 999) for i in range(10)]


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")


def nouv_input(*params):
    global échec

    if len(params) > 1:
        échec = True

    elif len(params) > 0:
        print(params[0], end="")

    entrée = str(entrées.pop())
    print(entrée)

    échec = False
    return entrée


builtins.input = nouv_input

try:
    import coffre4

    if échec:
        fail()
        send_msg("Quelque chose cloche", "Avez-vous bien utilisé «input»?")
    else:
        try:
            int(coffre4.entrée)
            success()
            send_msg(
                "Bravo!", "L'entrée de l'utilisateur (" + coffre4.entrée + ") est maintenant stockée sous le nom «entrée».")
        except AttributeError as e:
            fail()
            send_msg("Encore un peu!", "input() sert à saisir une entrée au clavier. Pour pouvoir l'utiliser plus tard, il faut la stocker sous le nom «entrée» en faisant «entrée = input()».")

except Exception as e:
    fail()
    échec = True
    send_msg("Pas tout à fait",
             'Quelque chose ne va pas. Utilisez «entrée = input()» après le message de bienvenue.')
    send_msg("Erreur", e)
