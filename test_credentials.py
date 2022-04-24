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

    def test_save_credentials(self):
        self.credential_details.save_credentials()
        self.assertEqual(len(Credentials.credential_details),1)

    def test_save_multiple_contact(self):
        self.credential_details.save_credentials()
        test_credential = Credentials('Facebook','kibe@gmail', '546894')

if __name__ == '__main__':
    unittest.main()