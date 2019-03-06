import unittest
from app.models import *

class RoverTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the photos class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.photos= Rover('hey','yoh')

    def test_instance(self):
        self.assertTrue(isinstance(self.photos,Rover))


