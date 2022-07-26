# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
        
    def testImage(self):
        '''Loads an image object from a single image dict'''
                
        a= test_data.mockSolutionViai()
        c = Image(test_data.getImageData(), a)
        
        self.assertTrue(c.sourceGcsUri == 'gs://bucket1/image1.jpg') 
        
    @patch('requests.get')
    def testGetImages(self, mock_get):
        '''Loads an Image list from the VIAI API'''
        
        mock_get.return_value.status_code = 200
        image_data = test_data.getImageApiData()
        mock_get.return_value.json.return_value = image_data
        
        a = test_data.mockSolutionViai()
        b = a.solutions[0]
        b.images = b._getImages()
        
        self.assertTrue(len(b.images) == 3)
        
    @patch('requests.get')
    def testGetAnnotationSets(self, mock_get):
        '''Loads a list of AnnotationSets from the VIAI API'''
        
        mock_get.return_value.status_code = 200
        annotationSetData = test_data.getAnnotationSetApiData()
        mock_get.return_value.json.return_value = annotationSetData
        
        a = test_data.mockSolutionViai()
        b = a.solutions[0]
        c = b._getAnnotationSets()
        
        self.assertTrue(len(c) == 6)
        
    @patch('requests.get')
    def testGetSolutionArtifact(self, mock_get):
        '''Loads a Solution Artifact from the VIAI API'''
        
        mock_get.return_value.status_code = 200
        solutionArtifactData = test_data.getSolutionArtifactData()
        mock_get.return_value.json.return_value = solutionArtifactData
        
        a = test_data.mockSolutionViai()
        b = a.solutions[0]
        c = b._getSolutionArtifacts()[0]
        
        self.assertEqual(c.displayName, 'mycontainer')        
        
    @patch('requests.get')
    def testGetModules(self, mock_get):
        '''Loads Modules for a Solution from the VIAI API'''
        
        mock_get.return_value.status_code = 200
        moduleData = test_data.getModuleApiData()
        mock_get.return_value.json.return_value = moduleData
        
        a = test_data.mockSolutionViai()
        b = a.solutions[0]
        c = b._getModules()
        
        self.assertEquals(c[0].displayName, 'Object Detection Module')       
        
    @patch('requests.get')
    def testGetAnnotation(self, mock_get):
        '''Loads an Annotation set for an Image from the VIAI API'''
        
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = test_data.getAnnotationApiData()
        
        a= test_data.mockSolutionViai()
        b = Image(test_data.getImageData(), a)
        c = b._getAnnotations()
        
        self.assertTrue(b.sourceGcsUri == 'gs://bucket1/image1.jpg')
        self.assertTrue(len(c) == 2)
        
    @patch('requests.get')
    def testGetAnnotationSpecs(self, mock_get):
        '''Loads an AnnotationSpec list from the VIAI API'''
        
        mock_get.return_value.status_code = 200
        annotationSpecData = test_data.getAnnotationSpecApiData()
        mock_get.return_value.json.return_value = annotationSpecData
        
        a = test_data.mockSolutionViai()
        b = a.solutions[0]
        c = b._getAnnotationSpecs()
        
        self.assertTrue(len(c) == 4)
        
    @patch('requests.get')
    def testGetModels(self, mock_get):
        '''Loads test Model objects within a test Module'''
        
        mock_get.return_value.status_code = 200
        modelData = test_data.getModelApiData()
        mock_get.return_value.json.return_value = modelData
        
        a = test_data.mockModuleViai()
        b = a.solutions[0].modules[0]
        c = b._getModels()
                
        self.assertEqual(c[0].createTime, '2022-07-15T20:01:27.082718Z')
        
    def testChangeLogLevel(self):
        '''Changes the VIAI object log level with the setLogLevel function'''
        
        a= test_data.mockSolutionViai()
        old_level = a.log.level
        a.setLogLevel('debug')
        
        self.assertNotEqual(old_level, a.log.level)
        self.assertEquals(a.log.level, 10)
        
if __name__ == '__main__':
    unittest.main()