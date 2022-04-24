import unittest
from user import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User('Vanitas','adnang720@gmail.com','2ba29s') # created user_detail object
    
    def tearDown(self):
        User.user_detail = [] # Resets object

    def test_init(self):
        self.assertEqual(self.new_user.username,'Vanitas')
        self.assertEqual(self.new_user.email,'adnang720@gmail.com')
        self.assertEqual(self.new_user.password,'2ba29s')

    def test_save_user_details(self):
        self.new_user.save_user() 
        self.assertEqual(len(User.user_detail),1)

    
       

if __name__ == '__main__':
    unittest.main()