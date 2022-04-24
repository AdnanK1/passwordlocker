#!/usr/bin/env python3.8

from user import User
from credentials import Credentials
import random

#Creating account
def create_account(email,password):
    new_account = User(email,password)
    return new_account

#save account
def save_account(user):
    user.save_user()

#Create credential
def create_credential(name,email1,password1):
    new_credential = Credentials(name,email1,password1)
    return new_credential

#save credential
def save_credential(credentials):
    credentials.save_credential()

#delete credential
def del_credential(credentials):
    credentials.delete_credentials()

#display credentials
def display_credentials():
    return Credentials.display_credential()

#find credentials
def find_credential(name):
    return Credentials.find_by_name(name)

#check if credentials exist
def check_existing_credentials(name):
    return Credentials.credentials_exist(name)

def main():
        print('Welcome to Password Locker. How may we call you?')
        user_name = input().capitalize()
        print(f'Hello {user_name}. What would you like to do?')
        print('\n')
        while True:
            print('Use the following to access the following: create an account \'new\', create password \'newp\', display credentials \'dc\', find credential \'fc\', exit \'exit\'')
            short_code = input().lower()

            if short_code == 'new':
                print('New User')
                print('-'*10)

                print('Enter email ...')
                email = input()

                print('Enter password here ...')
                password = input()

                save_account(create_account(email,password))#created and saved the new user
                print('\n')
                print('New user has been updated')
            
            elif short_code == 'newp':
                print('Please enter application i.e. \'Skype\'')
                name = input()

                print('Enter email used by the application ...')
                email1 = input()

                print('Would you like to write your own password \'(write)\' or auto generated \'(auto)\' ')
                password_input = input().lower()
                if password_input == 'write':
                    print('Type password here ...')
                    password1 = input()
                else:
                    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*()/'
                    while 1:
                        print('What length would you like: ...')
                        password1_len = int(input())
                        for x in range(0,password1_len):
                           password_char = random.choice(characters)
                           password1 = password_char

                save_credential(create_credential(name,email1,password1)) # saved credential      
                         


       
        

if __name__ == '__main__':

    main()