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
        '''
        test_save_user test case to test if the users object is saved into
         the users list
        '''
        self.new_user.save_user()
        self.assertTrue(len(User.users_list),1)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can delete credentials account from credentials_list.
        '''
        self.new_user.save_user()
        test_users = User("bob", "dred", "bobdred@gmail.com")
        test_users.save_user()

        self.new_user.delete_user()
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
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials()
        self.assertTrue(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save several credential objects to our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Chegg","johnbrown","12jo43")
        test_credentials.save_credentials()
        self.assertTrue(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can delete credentials account from credentials_list.
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("hackerrank","adidas", "8*9%ad")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertTrue(len(Credentials.credentials_list),1)

    def test_display_credentials(self):
        '''
        a test that ensures the method returns a list of all credentials saved
        '''
        self.assertTrue(Credentials.display_credentials(),Credentials.credentials_list)

    def test_credentials_exists(self):
        '''
        test to check if a credential exists on credentials_list.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("facebook","cleopatra","cleo909")
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("cleopatra")

        self.assertTrue(credentials_exists)

    def test_find_credentials_by_site_name(self):
        '''
        test to check if we can find the credentials by site_name and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("tiktok", "celeb", "tok@#en")
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_site_name("tiktok")

        self.assertTrue(found_credentials.site_name,test_credentials.site_name)

if __name__ == '__main__':
    unittest.main()