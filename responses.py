import random


def handleResponse(message) -> str:
    msg = message.lower()

    if msg == 'hi' or msg == 'hello' or msg == 'hey':
        return 'Hey there!'

    if msg == 'roll':
        return str(random.randint(1, 6))

    if msg == 'flip':
        return str(random.choice(['heads', 'tails']))

    if msg == '!help':
        return 'Available commands: `!help`, `hi`, `hello`, `hey`, `roll`, `flip`'

    if msg == 'bye' or msg == 'goodbye':
        return 'Bye!'
