import hashlib
import requests
import colorama
import argparse

colorama.init()
parser = argparse.ArgumentParser(description='Antipublic.One Tool by Armanta#6184')
parser.add_argument("-g", "--generate", help="Generates a 16 bytes hexadecimal key", action='store_true')
parser.add_argument("-d", "--count", help="Get database size", action='store_true')
parser.add_argument("-c", "--check", help="Check an email address or a key", action='store_true')
parser.add_argument("-k", "--key", help="Check a key", type=str)
parser.add_argument("-e", "--email", help="Check an email", type=str)
args = parser.parse_args()


def key_check(key):
    req = requests.get(f'http://antipublic.one/api/check.php?key={key}')
    data = req.json()
    print(data)

def mail_check(email, key):
    req = requests.get(f'https://antipublic.one/api/email_search.php?key={key}&email={email}')
    data = req.json()
    if data["success"]:
        for combo in data["results"]:
            print(f"{colorama.Fore.LIGHTMAGENTA_EX}[+]{combo['line']}")
    else:
        print(f"{colorama.Fore.LIGHTRED_EX}[-]No matching email address")

def count():
    req = requests.get('https://antipublic.one/api/count_lines.php')
    db_size = req.text
    print(f"{colorama.Fore.LIGHTCYAN_EX}[#]{db_size} lines")


if args.generate:
    pass
elif args.check:
    if args.email and args.key:
        mail_check(args.email, args.key)
    else:
        print(f"{colorama.Fore.LIGHTRED_EX}Missing arguments (key, email)")
else:
    count()
