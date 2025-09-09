#!/usr/bin/env python3

import argparse
from onekey.core import OneKeyCore

def call(args):
    OneKeyCore(unikey=args.key, domain=args.domain)


def main():
    parser = argparse.ArgumentParser(description="Գաղտանաբռերի մենեջեր հիմնաված հեշ sha256 վրա։" \
    "\n You do not need to remember your Passwords")

    parser.add_argument('--key', '-k', default=None, help='Քո բանալին ասյտեղ | Your key here')
    parser.add_argument('--domain', '-d', default=None, help='հոսթի կամ հաշվի անունը | Host or accaunt name')

    args = parser.parse_args()
    call(args=args)


if __name__ == '__main__':
    main()