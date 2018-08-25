class Credential:
    '''
    Class that generates new instances of credentials.
    '''

    credential_list = []  # Empty credential list

    def __init__(self, first_name, last_name, number, email):

 
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New credential first name.
            last_name : New credential last name.
            number: New credential phone number.
            email : New credential email address.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email
