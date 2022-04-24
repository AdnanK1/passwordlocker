from curses.ascii import CR
from user import User
class Credentials:
    
    credential_details = [] #empty credential_details list

    def save_credentials(self):

        Credentials.credential_details.append(self)

    def delete_credentials(self):
        Credentials.credential_details.remove(self)

    def __init__(self,name,email,password):
        # docstring removed for simplicity
        self.name = name
        self.email = email
        self.password = password