import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Twitter")
    
    def test_init(self):
        self.assertTrue(self.new_user.account,"Twitter")

if __name__ == '__main__':
    unittest.main()