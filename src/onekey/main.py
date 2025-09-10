#!/usr/bin/env python3

import sys
import signal
import argparse
from onekey.core import OneKeyCore


def close_handler(sig, frame):
    messages = ['\n', '\U00002757Something went wrong...', '\U00002757Onekey is closed with an emergancy exit', '\n']
    for message in messages:
        print(message)
    sys.exit(0)
    
signal.signal(signal.SIGINT, close_handler)
signal.signal(signal.SIGTSTP, close_handler)

def call(args):
    if args.key and len(args.key) > 64:
        args.key = None
    one = OneKeyCore(unikey=args.key, domain=args.domain)
    one.close()
    


def main():
    parser = argparse.ArgumentParser(description="Գաղտանաբռերի մենեջեր հիմնաված հեշ sha256 վրա։" \
    "\n You do not need to remember your Passwords")

    parser.add_argument('--key', '-k', default=None, help='Քո բանալին ասյտեղ | Your key here')
    parser.add_argument('--domain', '-d', default=None, help='հոսթի կամ հաշվի անունը | Host or accaunt name')

    args = parser.parse_args()
    call(args=args)


if __name__ == '__main__':
    main()