#!/usr/bin/env python3

from .core import Hasher
import json
import random
import requests


HEADERS = {
    'Content-Type': 'application/json'
}

class KeyGenerator(Hasher):

    def __init__(self, command: str):
        super().__init__()

        self.command = command
        self.randoms = self.api_connection

    def __str__(self) -> str:

        if self.command in ('new',):
            return f'Randomly generated key -> {self.hexhash(self.hexhash(self.randoms[random.randint(0, 7)]))}'
        else:
            return f'Key generated from your inputs -> {self.hexhash(self.command)}' 


    @property
    def api_connection(self) -> list:

        with open('src/onekey/core/randomorg_api.json', encoding='utf-8') as file:
            request_form = json.load(file)

        response = requests.post(
            'https://api.random.org/json-rpc/2/invoke', 
            data=json.dumps(request_form),
            headers=HEADERS)
        
        return response.json()['result']['random']['data']
            