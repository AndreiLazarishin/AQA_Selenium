import random
import string


def rand_pass(password):
    generate_pass = ''.join([random.choice(string.ascii_lowercase + string.digits) for _ in range(password)])
    return generate_pass


def random_email(email):
    generate_email = ''.join([random.choice(string.ascii_lowercase) for _ in range(email)]) + '@john.com'
    return generate_email


def rand_username(name):
    generate_name = ''.join([random.choice(string.ascii_lowercase) for _ in range(name)])
    return generate_name
