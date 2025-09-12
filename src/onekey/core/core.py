#!/usr/bin/env python3

# Այստեղ իրականացված են գործիքի բոլոր բազզային ֆունկցիոնալ հնարավորությունները։

import hashlib
import base64
from getpass import getpass

class Hasher:

    def __init__(self):

        self.hexhash = lambda x: hashlib.sha256(str.encode(x)).hexdigest()


    def get_hash_sum(func):
        def wrapper(self):     
            return hashlib.sha256(str.encode(func(self))).hexdigest() 
        return wrapper      

    @property
    def final_hash_sum(self):
        hash_sum = hashlib.sha256(str.encode(self.ukey + self.domain)).digest()
        return base64.b64encode(hash_sum).decode('ascii')


class OneKeyCore(Hasher):
     
    def __init__(self, unikey=None, domain=None):

        super().__init__()
        self.domain_for_show = domain if domain else None
        self.ukey = self.hexhash(unikey) if unikey else self.get_key()
        self.domain = self.hexhash(domain.lower()) if domain else self.get_domain()
        
 
    
    @Hasher.get_hash_sum
    def get_key(self):

        required_len = 64
        
        secret_phrase = getpass('\U0001F510 Please enter your unical secret key: ')

        while not len(secret_phrase) == required_len:
              secret_phrase = getpass('\U0001F514 Please enter valid, 64 character unical secret key: ')

        return secret_phrase

    @Hasher.get_hash_sum 
    def get_domain(self):
        
        domain = input('\U0001F3E2 please enter account domain: ') or None
        
        while not domain:
            domain = input('\U0001F514 Domain lebel can\'t be empty: ') or None
        self.domain_for_show = domain
        return domain.lower()   

    def close(self):
        
        is_tuple = isinstance(self.import_error_handle, tuple)

        if is_tuple:
            print(f'\U00002705 Your password for {self.domain_for_show.upper()} copied to clipboard.')
        
        else:
            print(f'\U00002705 This is Your password {self.import_error_handle} for {self.domain_for_show.upper()}') 

    @property
    def import_error_handle(self):
        try:
            import  pyperclip
            return pyperclip.copy(self.final_hash_sum), []
        
        except ImportError:
            return self.final_hash_sum   



    
   

if __name__ == '__main__':
    one = OneKeyCore()
    one.close()
    

