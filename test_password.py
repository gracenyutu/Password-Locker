import unittest
from user import User,Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each user test cases.
        '''
        self.new_user = User("grace", "nyutu", "gnyutu@gmail.com")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialised properly
        '''
        self.assertTrue(self.new_user.first_name,"grace")
        self.assertTrue(self.new_user.last_name,"nyutu")
        self.assertTrue(self.new_user.email,"gnyutu@gmail.com")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertTrue(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each credentials test cases.
        '''
        self.new_credentials = Credentials("twitter", "gracenyutu", "frozen56")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialised properly
        '''
        self.assertTrue(self.new_credentials.site_name,"twitter")
        self.assertTrue(self.new_credentials.username,"gracenyutu")
        self.assertTrue(self.new_credentials.password,"frozen56")

    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertTrue(len(Credentials.credentials_list),1)

if __name__ == '__main__':
    unittest.main()