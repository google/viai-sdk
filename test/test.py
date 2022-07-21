import unittest
from unittest.mock import patch, Mock
import os
from viai import VIAI
from viai import AuthCredentialException
from viai.solutions import Solution, SolutionArtifact
from viai.modules import Module, Model, ModelEvaluation, SolutionArtifact
from viai.images import Image, Annotation, AnnotationSet, AnnotationSpec
import test_data


def mockSolutionViai():
    
    mock_get_patcher = patch('requests.get')
    mock_get = mock_get_patcher.start()    
    
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = test_data.getSolutionApiData()
    
    mock_viai = VIAI(connect=False)
    mock_viai.region = 'myregion'
    mock_viai.projectId = 'myproject'
    mock_viai.solutions = mock_viai._getSolutions()
    mock_get_patcher.stop()
    
    return mock_viai
    

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
                
        a= mockSolutionViai()
        c = Image(test_data.getImageData(), a)
        
        self.assertTrue(c.sourceGcsUri == 'gs://bucket1/image1.jpg') 
        
    @patch('requests.get')
    def testGetImages(self, mock_get):
        '''tests loading the image object'''
        
        mock_get.return_value.status_code = 200
        image_data = test_data.getImageApiData()
        mock_get.return_value.json.return_value = image_data
                
        a= mockSolutionViai()
        b = a.solutions[0]
        b.images = b._getImages()
        
        
        
        self.assertTrue(b.images[0].name == image_data['images'][0]['name'])
        self.assertTrue(b.images[0].createTime == image_data['images'][0]['createTime'])
        self.assertTrue(b.images[0].sourceGcsUri == image_data['images'][0]['sourceGcsUri'])
        self.assertTrue(b.images[0].etag == image_data['images'][0]['etag'])    
        
if __name__ == '__main__':
    unittest.main()