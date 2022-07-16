import unittest
import os
from viai import VIAI, Solution, AuthCredentialException
from viai_images import Image, Annotation, AnnotationSet, AnnotationSpec

class TestViaiInit(unittest.TestCase):
    
    def testNoServiceAccountKeyfile(self):
        '''tests that AuthCredentailException is thrown if no service account information
        is passed to the function'''
        
        if os.getenv('GOOGLE_AUTHENTICATION_CREDENTIALS') is not None:
            os.environ['GOOGLE_AUTHENTICATION_CREDENTIALS'] == None
                
        self.assertRaises(AuthCredentialException, VIAI)
        
if __name__ == '__main__':
    unittest.main()