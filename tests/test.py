import unittest
from unittest.mock import patch, Mock
import os
from viai import VIAI
from viai import AuthCredentialException
from viai.solutions import Solution, SolutionArtifact
from viai.modules import Module, Model, ModelEvaluation, SolutionArtifact
from viai.images import Image, Annotation, AnnotationSet, AnnotationSpec
import test_data


class TestViai(unittest.TestCase):

    @patch('requests.get')
    def testGetSolutions(self, mock_get):
        '''tests getting a list of solutions from the VIAI API'''
        
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = test_data.getSolutionApiData()
        
        viai = VIAI(connect=False)
        viai.solutions = viai._getSolutions()
                
        self.assertTrue(viai.solutions[0].displayName == 'solution1')
        self.assertTrue(len(viai.solutions) == 3)
        
    def testImageModel(self):
        '''Loads an image object from a single image dict'''
                
        a= test_data.mockSolutionViai()
        c = Image(test_data.getImageData(), a)
        
        self.assertTrue(c.sourceGcsUri == 'gs://bucket1/image1.jpg') 
        
    @patch('requests.get')
    def testGetImages(self, mock_get):
        '''tests loading the image object'''
        
        mock_get.return_value.status_code = 200
        image_data = test_data.getImageApiData()
        mock_get.return_value.json.return_value = image_data
        
        a = test_data.mockSolutionViai()
        b = a.solutions[0]
        b.images = b._getImages()
        
        self.assertTrue(len(b.images) == 3)
        
    @patch('requests.get')
    def testGetAnnotation(self, mock_get):
        '''tests loading an Annotation set for an Image from the VIAI'''
        
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = test_data.getAnnotationApiData()
        
        a= test_data.mockSolutionViai()
        b = Image(test_data.getImageData(), a)
        c = b._getAnnotations()
        
        self.assertTrue(b.sourceGcsUri == 'gs://bucket1/image1.jpg')
        self.assertTrue(len(c) == 2)
        
if __name__ == '__main__':
    unittest.main()