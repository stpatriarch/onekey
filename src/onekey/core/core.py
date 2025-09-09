#!/usr/bin/env python3

# Այստեղ իրականացված են գործիքի բոլոր բազզային ֆունկցիոնալ հնարավորությունները։

import hashlib
import base64
from getpass import getpass
import pyperclip as clip


class OneKeyCore:
     
    def __init__(self, unikey=None, domain=None):

        self.domain_for_show = domain if domain else None
        self.req_len  = 64
        self.ukey = unikey if unikey else self.get_key()
        self.domain = domain if domain else self.get_domain()
        self.hash = clip.copy(self.final_hash_sum)
        
    def get_hash_sum(func):
        def wrapper(self):     
            return hashlib.sha256(str.encode(func(self))).hexdigest() 
        return wrapper   
    
    @get_hash_sum
    def get_key(self):
         
        secret_phrase = getpass('Please enter your unical secret key: ')

        while not len(secret_phrase) == self.req_len:
              secret_phrase = getpass('Please enter valid, 64 character unical secret key: ')

        return secret_phrase

    @get_hash_sum 
    def get_domain(self):
        
        domain = input('please enter account domain: ') or None
        
        while not domain:
            domain = input('Domain lebel can\'t be empty: ') or None
        self.domain_for_show = domain
        return domain     
    
    def __del__(self):
        print(f'Your password for {self.domain_for_show.upper()} copied to clipboard')
        return 
    
    @property
    def final_hash_sum(self):
     hash_sum = hashlib.sha256(str.encode(self.ukey + self.domain)).digest()
     return base64.b64encode(hash_sum).decode('ascii')

    
   




if __name__ == '__main__':
    OneKeyCore()
    

