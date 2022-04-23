import pyperclip

class User:
    '''
    Class to create ser accounts and save their information
    '''
    users_list = []
    def __init__(self,account):
        '''
        Method to define the properties each user object will hold.
        '''
        self.account = account

    def save_user(self):
        User.users_list.append(self)

class Credentials:
    def __init__(self,username, password):
        self.username = username
        self.password = password  