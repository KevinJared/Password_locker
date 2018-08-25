import unittest
from credential import Credential


class TestCredential(unittest.TestCase):

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
            "James", "Muriuki", "0712345678", "james@ms.com")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.first_name, "James")
        self.assertEqual(self.new_credential.last_name, "Muriuki")
        self.assertEqual(self.new_credential.number, "0712345678")
        self.assertEqual(self.new_credential.email, "james@ms.com")


    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into the credential list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

if __name__ == '__main__':
    unittest.main()