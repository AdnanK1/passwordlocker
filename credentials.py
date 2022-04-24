class Credentials:
    
    credential_details = [] #empty credential_details list
    

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

   
    def __init__(self,name,email1,password1):
        # docstring removed for simplicity
        self.name = name
        self.email1 = email1
        self.password1 = password1