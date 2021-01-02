import os
import time
import secrets
import clipboard
os.system('cls')

try:
    print('How strong do you want your password to be? ')
    ask = input('(a) Letters\n(b) Letters + Numbers\n(c) Letters + Numbers + Special Characters\n : ')

    if ask == 'a':
        time.sleep(2)
        os.system('cls')
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        try:
            leng = int(input('How long should your password be? '))
        except:
            print("Oh no. You didn't enter a number! Please try again.")
        pas = ''
        for x in range(leng):
            pas = pas + secrets.choice(chars)
        
        time.sleep(2)
        os.system('cls')
        print('Your new password is: ' + pas)
        clipboard.copy(pas)
        print('Password copied to clipboard!')


    elif ask == 'b':
        time.sleep(2)
        os.system('cls')
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        try:
            leng = int(input('How long should your password be? '))
        except:
            print("Oh no. You didn't enter a number! Please try again.")
        pas = ''
        for x in range(leng):
            pas = pas + secrets.choice(chars)
        
        time.sleep(2)
        os.system('cls')
        print('Your new password is: ' + pas)
        clipboard.copy(pas)
        print('Password copied to clipboard!')

    elif ask == 'c':
        time.sleep(2)
        os.system('cls')
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
        try:
            leng = int(input('How long should your password be? '))
        except:
            print("Oh no. You didn't enter a number! Please try again.")
        pas = ''
        for x in range(leng):
            pas = pas + secrets.choice(chars)
        
        time.sleep(2)
        os.system('cls')
        print('Your new password is: ' + pas)
        clipboard.copy(pas)
        print('Password copied to clipboard!')

    else:
        time.sleep(2)
        os.system('cls')
        print("Wrong input :\ ")


    time.sleep(3)
    quit()
except:
    print('An error occurred. Sorry!')
