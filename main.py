import hashlib, base64, re


def get_user_input(label, requered=False, domain=False):
        value = input(f'{label}') or None
        while requered and not value:
            value = input(f'{label}') or None
        if domain and re.match('.', value):
            value = value.split('.')[0]
        return value.lower()    

def hash_it(phrase):     
     hashsum = hashlib.sha256(str.encode(phrase)).digest()
     finalsum = base64.b64encode(hashsum).decode('ascii')
     return finalsum[:-1]

def main():
    secret_phrase = input('Please enter your unical phrase: ')
    while not len(secret_phrase) == 64:
        secret_phrase = input('Please enter your unical phrase: ')
        print('Your unical secret phrase must be a have 64 characters')
    
    username = get_user_input('enter your username: ', requered=True)
    domain = get_user_input('please enter account domain: ', requered=True, domain=True)

    unihash = hash_it(f'{username + domain}')
    final_hash = hash_it(f'{secret_phrase + unihash}')
    print(f'Your password for {username} in {domain} is:  {final_hash}')

if __name__ == '__main__':
    main()