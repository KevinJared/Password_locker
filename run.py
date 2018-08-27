#!/usr/bin/env python3.6
from credential import Credential


def create_credential(fname, lname, password, email):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(fname, lname, password, email)
    return new_credential


def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()


def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()


def find_credential(username):
    '''
    Function that finds a credential by username and returns the credential
    '''
    return Credential.find_by_username(username)


def check_existing_credentials(user_name):
    '''
    Function that check if a credential exists with that username and return a Boolean
    '''
    return Credential.credential_exist(username)


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()


def main():
    print("Hey Welcome to your password locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, ex -exit the credential list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New credential")
            print("-"*10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("password ...")
            p_word = input()

            print("Email address ...")
            e_address = input()

            # create and save new credential.
            save_credentials(create_credential(
                f_name, l_name, p_word, e_address))
            print ('\n')
            print(f"New credential {f_name} {l_name} created")
            print ('\n')

        elif short_code == 'dc':

            if display_credentials():
                print("This is a list of all your credentials")
                print('\n')

                for credential in display_credentials():
                    print(f"{credential.first_name} {credential.last_name} .....{credential.password}")

                print('\n')
            else:
                print('\n')
                print("You dont have any credentials saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the email you want to search for")

            search_email= input()
            if check_existing_credentials(search_email):
                search_credential = find_credential(search_email)
                print(f"{search_credential.first_name} {search_credential.last_name}")
                print('-' * 20)

                print(f"Last name.......{search_credential.f_name}")
                print(f"First name.......{search_credential.password}")
            else:
                print("That credential does not exist")

        elif short_code == "ex":
            print("See you soon ..")
            break
        else:
            print("Please use the short codes provided")


if __name__ == '__main__':

    main()
