#!/usr/bin/env python3.8

from user import User
from credentials import Credentials

#Creating account
def create_account(email,password):
    new_account = User(email,password)
    return new_account

#save account
def save_account(user):
    user.save_user()

#Create credential
def create_credential(name,email,password):
    new_credential = Credentials(name,email,password)
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
    print

if __name__ == '__main__':

    main()