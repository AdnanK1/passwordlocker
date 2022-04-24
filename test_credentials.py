import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        self.credential_details = Credentials('Instagram','kibe@gmail.com','273904') # created credential_detail object 
    
    def tearDown(self):
        Credentials.credential_details = [] #Resets Object

    def test_init(self):
        self.assertEqual(self.credential_details.name, 'Instagram')
        self.assertEqual(self.credential_details.email,'kibe@gmail.com')
        self.assertEqual(self.credential_details.password,'273904')