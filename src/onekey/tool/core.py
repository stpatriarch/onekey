import hashlib
import base64
from getpass import getpass
import pyperclip as clip

def get_user_input(label, requered=False):
        
        value = input(f'{label}') or None
        while requered and not value:
            value = input(f'{label}') or None
        return value    

def get_hash_sum(secret_phrase):
     hash_sum = hashlib.sha256(str.encode(secret_phrase)).digest()
     return base64.b64encode(hash_sum).decode('ascii')


def main():
    secret_phrase = input('Please enter your unical secret phrase: ')
    while not len(secret_phrase) == 64:
        secret_phrase = input('Please enter your unical secret phrase: ')
        print('Your unical secret phrase must be a have 64 characters')
    
    # username = get_user_input('enter your username: ', requered=True)
    domain = get_user_input('please enter account domain: ', requered=True)
    
    # unihash = hash_it(f'{username + domain}')
    final_hash = get_hash_sum(f'{secret_phrase + domain}')
    password = f'Your password for {domain} is:  {final_hash[16:]}'
    print(password)
    return 0


class OneKeyCore:
     
    def __init__(self):

        self.req_len  = 64
        self.ukey = self.get_phrase()
        self.dom = self.get_domain()
        self.hash = clip.copy(self.final_hash_sum)
        print('Your password copied to clipboard')

        
    def get_hash_sum(func):
        def wrapper(self):     
            return hashlib.sha256(str.encode(func(self))).hexdigest() 
        return wrapper

    @get_hash_sum
    def get_phrase(self):
         
        secret_phrase = getpass('Please enter your unical secret phrase: ')

        while not len(secret_phrase) == self.req_len:
              secret_phrase = getpass('Please enter valid, 64 character unical secret phrase: ')

        return secret_phrase

    @get_hash_sum 
    def get_domain(self):
        
        domain = input('please enter account domain: ') or None
        
        while not domain:
            domain = input('Domain lebel can\'t be empty: ') or None
        return domain     
     
    @property
    def final_hash_sum(self):
     hash_sum = hashlib.sha256(str.encode(self.ukey + self.dom)).digest()
     return base64.b64encode(hash_sum).decode('ascii')

    




if __name__ == '__main__':
    one = OneKeyCore()
    

