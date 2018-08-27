class Credential:
    '''
    Class that generates new instances of credentials.
    '''

    credential_list = []  # Empty credential list

    def __init__(self, first_name, last_name, password, email):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New credential first name.
            last_name : New credential last name.
            password: New credential  password.
            email : New credential email address.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email


# save credential
    def save_credential(self):
        '''
        save_credential method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)

# delete credential
    def delete_credential(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def credential_exist(cls, password):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            password:  password to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.password == password:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list