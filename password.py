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