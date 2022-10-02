radio.set_group(88)

def on_forever():
    radio.send_value("lighttt", input.light_level())
    basic.pause(1000)
basic.forever(on_forever)
