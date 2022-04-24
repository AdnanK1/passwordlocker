from curses.ascii import CR

class Credentials:
    
    credential_details = [] #empty credential_details list
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*()/'

    def save_credentials(self):

        Credentials.credential_details.append(self)

    def delete_credentials(self):
        Credentials.credential_details.remove(self)

    @classmethod
    def credentials_exist(cls,name):
        for credentials in cls.credential_details:
            if credentials.name == name:
                return True

        return False

    @classmethod
    def find_by_name(cls,name):
        for credentials in cls.credential_details:
            if credentials.name == name:
                return credentials

    @classmethod
    def display_credential(cls):
        return cls.credential_details

   
    def __init__(self,name,email,password):
        # docstring removed for simplicity
        self.name = name
        self.email = email
        self.password = password