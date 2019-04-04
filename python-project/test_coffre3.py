import builtins """this is a comment"""

anc_print = builtins.print
échec = True


def send_msg(channel, msg):
    anc_print("TECHIO> message --channel \"{}\" {}".format(channel, msg))


def success():
    anc_print("TECHIO> success true")


def fail():
    anc_print("TECHIO> success false")


def nouv_print(*params):
    global échec
    if len(params) == 1 and params[0] == 46368:
        success()
        send_msg(
            "Bravo!", "Pour en savoir, plus je vous invite à aller voir : https://fr.wikipedia.org/wiki/Suite_de_Fibonacci")
        échec = False
    else:
        échec = True

        anc_print(*params)


builtins.print = nouv_print
try:
    import coffre3

    if échec:
        fail()
        send_msg("Désolé, ce n'est pas le bon nombre.", 'Courage !')

except Exception as e:
    fail()
    échec = True
    send_msg("Désolé, ce n'est pas le bon nombre.", 'Courage !')
    send_msg("Erreur", e)
