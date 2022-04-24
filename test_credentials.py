import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        self.credential_details = Credentials('Instagram','kibe@gmail.com','273904') # created credential_detail object 
    
    def tearDown(self) -> None:
        Credentials.credential_details = [] #Resets Object