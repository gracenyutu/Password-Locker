import email
from user import User, Credentials
import pyperclip

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

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def check_existing_credentials(username):
    '''
    Function that check if credentials exist with the given username and return a Boolean
    '''
    return Credentials.credentials_exist(username)


def find_credential(number):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credentials.find_by_site_name(number)

def copy_credential(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credentials.find_by_site_name(site_name)

def main():
    print("Hello! Welcome to Password Locker")
    username = input()

    print(f"Hello {username}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new credentials, dc - display credentials, fs -find credentials using site_name, ex -exit the credentials list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New User")
                            print("-"*10)

                            print ("First name ....")
                            first_name = input()

                            print("Last name ...")
                            last_name = input()

                            print("Email ...")
                            email = input()


                            save_users(create_user(first_name,last_name,email)) 
                            print ('\n')
                            print(f"New User {first_name} {last_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all credentials")
                                    print('\n')

                                    for credentials in display_credentials():
                                            print(f"{credentials.site_name} {credentials.username}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')

                    elif short_code == 'fs':

                            print("Enter the site you want to search credentials for")

                            search_site_name = input()
                            if check_existing_credentials(search_site_name):
                                    search_credentials = find_credential(search_site_name)
                                    print(f"{search_credentials.username} {search_credentials.password}")
                                    print('-' * 20)

                                    print(f"Username.......{search_credentials.username}")
                                    print(f"Password.......{search_credentials.password}")
                            else:
                                    print("That site's credentials do not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()