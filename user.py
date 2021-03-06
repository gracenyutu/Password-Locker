from distutils.command.build_scripts import first_line_re
import pyperclip
import random
import string

class User:
    '''
    Class to create user accounts and save their information
    '''
    users_list = []
    def __init__(self,first_name, last_name, email, password):
        '''
        Method to define the properties each user object will hold.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

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
    @classmethod
    def check_user(cls,first_name,password):
            '''
            Method that checks if the name and password entered match entries in the users_list
            '''
            current_user = ''
            for user in User.users_list:
                if (user.first_name == first_name and user.password == password):
                    current_user = user.first_name
            return current_user

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

    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
            '''
            Function to generate an 8 character password for a credential
            '''
            gen_pass=''.join(random.choice(char) for _ in range(size))
            return gen_pass

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

    @classmethod
    def find_by_site_name(cls,site_name):
        '''
        Method that takes in a site_name and returns the credentials that match it.
        '''

        for credentials in cls.credentials_list:
            if credentials.site_name == site_name:
                return credentials