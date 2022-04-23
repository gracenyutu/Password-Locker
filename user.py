from distutils.command.build_scripts import first_line_re
import pyperclip
import random

class User:
    '''
    Class to create user accounts and save their information
    '''
    users_list = []
    def __init__(self,first_name, last_name, email):
        '''
        Method to define the properties each user object will hold.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def save_user(self):
        '''
        save_user method saves user objects into users_list
        '''
        User.users_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user
        '''
        User.users_list.remove(self)

class Credentials:
    '''
    Class to create credentials accounts and save their information
    '''
    credentials_list = []
    def __init__(self,site_name,username, password):
        '''
        Method to define the properties each credentials object will hold.
        '''
        self.username = username
        self.password = password
        self.site_name = site_name

    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into credentials_list
        '''
        Credentials.credentials_list.append(self)

    def test_find_credentials_by_site_name(self):
        '''
        test to check if we can find the credentials by site_name and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("tiktok", "celeb", "tok@#en")
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_site_name("tiktok")

        self.assertEqual(found_credentials.site_name,test_credentials.site_name)
    def delete_credentials(self):
        '''
        delete_credentials method deletes saved credentials
        '''
        Credentials.credentials_list.remove(self)

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found contact
        '''

        self.new_credentials.save_credentials()
        Credentials.copy_email("0712345678")

        self.assertEqual(self.new_contact.email,pyperclip.paste())

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    @classmethod
    def credentials_exist(cls,username):
        '''
        Method that checks if a credentials exists from the credentials list.
        '''
        for credentials in cls.credentials_list:
            if credentials.username == username:
                    return True

        return False