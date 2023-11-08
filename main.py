import argparse
from string import *
from random import choice


def parse_args():
    global args

    parser = argparse.ArgumentParser()
    parser.add_argument('l', type=int, help='Length of password')

    args = parser.parse_args()


def generate_password(password_length: str):
    password_length = password_length
    characters = ascii_letters + digits + punctuation

    password = ""

    for _ in range(password_length):
        password += choice(characters)

    return f'Your password is ready: {password}'


def main():
    parse_args()
    print(generate_password(args.l))


if __name__ == '__main__':
    main()
