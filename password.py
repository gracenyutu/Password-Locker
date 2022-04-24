import email
from user import User, Credentials
import pyperclip

def create_user(first_name,last_name,email, username):
    '''
    Function to create new user
    '''
    new_user = User(first_name, last_name, email, username)
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


def find_credential(site_name):
    '''
    Function that finds credentials by using the site_name
    '''
    return Credentials.find_by_site_name(site_name)

def copy_credential(site_name):
    '''
    Function to copy a credentials details to the clipboard
    '''
    return Credentials.find_by_site_name(site_name)

def main():
    print(' ')
    print("Hello! Welcome to Password Locker.")

    while True:
        print(' ')

        print("-"*60)

        print('Use these codes to navigate: \n ca-Create an Account \n li-Log In \n ex-Exit')

        short_code = input('Enter a choice: ').lower().strip()
        if short_code == 'ca':
                print("-"*60)
                print(' ')
                print('To create a new user:')
                first_name = input('Enter your first name - ').strip()
                last_name = input('Enter your last name - ').strip()
                email = input('Enter your email - ').strip()
                save_users(create_user(first_name,last_name,email))
                print(" ")
                print(f'New Account Created for: {first_name} {last_name} with {email} using username: {username}')

        elif short_code == 'li':
                print("-"*60)
                print(" ")
                print('To login, enter your account details:')
                user_name = input('Enter your preferred username - ').strip()
                password = str(input('Enter your password - '))
                user_exists = verify_user(user_name,password)
                if user_exists == user_name:
                        print(" ")
                        print(f'Welcome {user_name}. Please choose an option to continue.')
                        print(" ")
                        while True:
                                print("_"*60)
                                print("Use these short codes : cc - create a new credentials, dc - display credentials, fs -find credentials using site_name, ex -exit the credentials list ")
                                short_code = input('Enter a choice').lower().strip()
                                print("-"*60)
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