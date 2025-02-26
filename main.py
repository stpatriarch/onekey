import hashlib
import base64


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

if __name__ == '__main__':
    main()
