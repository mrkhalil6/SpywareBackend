import random
import string


def random_key_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_device_key():

    return random_key_generator(size=12)
