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

if __name__ == '__main__':

    main()