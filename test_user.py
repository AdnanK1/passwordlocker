import unittest
from user import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
       
       self.new_user = User('adnang720@gmail.com','2ba29s') # created user_detail object
    
    def test_inti(self):
        self.assertEqual(self.new_user.email,'adnang720@gmail.com')
        self.assertEqual(self.new_user.password,'2ba29s')

if __name__ == '__main__':
    unittest.main()