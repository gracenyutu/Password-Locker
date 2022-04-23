from distutils.command.build_scripts import first_line_re
import pyperclip

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

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved user
        '''
        Credentials.credentials_list.remove(self)