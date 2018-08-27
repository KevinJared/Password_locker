import unittest
from credential import Credential


class TestCredential(unittest.TestCase):
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential(
            "peter", "Stewart", "34567822", "peter@gmail.com")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.first_name, "peter")
        self.assertEqual(self.new_credential.last_name, "Stewart")
        self.assertEqual(self.new_credential.password, "34567822")
        self.assertEqual(self.new_credential.email, "peter@gmail.com")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into the credential list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential(
            "Test", "user", "34567822", "test@user.com")  # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    # Delete credentials

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential(
            "Test", "user", "34567822", "test@user.com")  # new credential
        test_credential.save_credential()

        self.new_credential.delete_credential()  # Deleting a credential object
        self.assertEqual(len(Credential.credential_list), 1)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","851292","test@user.com") # new credential
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("851292")

        self.assertTrue(credential_exists)
        
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)
        
if __name__ == '__main__':
    unittest.main()