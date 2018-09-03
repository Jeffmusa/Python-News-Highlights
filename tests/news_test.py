import unittest
from app.models import News,Articles


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.news= News('CNN','url','country',122,'late')

    def test_instance(self):
        self.assertTrue(isinstance(self.news,News))


# if __name__ == '__main__':
#     unittest.main()