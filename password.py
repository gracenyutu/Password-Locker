from user import User, Credentials

def create_user(first_name,last_name,email):
    '''
    Function to create new user
    '''
    new_user = User(first_name, last_name, email)
    return new_user

def create_credentials(site_name, username, password):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(site_name, username, password)
    return new_credentials

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def save_cred(credentials):
    '''
    Function to save credential
    '''
    credentials.save_credentials()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def del_credentials(credentials):
    '''
    Function to delete a credential
    '''
    credentials.delete_credentials()