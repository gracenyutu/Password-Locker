import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Twitter")
    
    def test_init(self):
        self.assertTrue(self.new_user.account,"Twitter")

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credentials("gracenyutu", "frozen56")
    
    def test_init(self):
        self.assertTrue(self.new_credentials.username,"gracenyutu")
        self.assertTrue(self.new_credentials.password,"frozen56")
        
if __name__ == '__main__':
    unittest.main()