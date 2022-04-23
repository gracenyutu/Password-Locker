import unittest
from user import User,Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each user test cases.
        '''
        self.new_user = User("Twitter")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialised properly
        '''
        self.assertTrue(self.new_user.account,"Twitter")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertTrue(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each credentials test cases.
        '''
        self.new_credentials = Credentials("gracenyutu", "frozen56")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialised properly
        '''
        self.assertTrue(self.new_credentials.username,"gracenyutu")
        self.assertTrue(self.new_credentials.password,"frozen56")

    def test_save_credentials(self):
        self.new_user.save_credential()
        self.assertTrue(len(User.credentials_list),1)

if __name__ == '__main__':
    unittest.main()