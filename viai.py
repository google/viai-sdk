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

import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from viai_images import Image, Annotation, AnnotationSet, AnnotationSpec


class VIAI:
    '''The primary class for handling VIAI objects effectively in Python 
    applications'''
    
    def __init__(self, keyfile='viai-key.json', region='us-central1'):
        self.author = 'Jamie Duncan'

        self.region = 'us-central1'
        self.apiUrl = "https://visualinspection.googleapis.com/v1"
        self.credentials = self._getAuthCredentials(keyfile)  
        self.projectId = self.credentials.project_id
        self.region = region
        self.requestHeader = {"Authorization": "Bearer {}".format(self.credentials.token)}
        
        self.solutions = self._getSolutions()
        
    def _getAuthCredentials(self, keyfile):
        '''internal function to create a valid Google authenticated session and generate a JWT token
        inputs:
        keyfile - a service account json keyfile for a service acccount with at least VIAI admin role bindings'''
        
        scopes = [
            "https://www.googleapis.com/auth/cloud-platform",
            "https://www.googleapis.com/auth/userinfo.email"
            ]
        
        try:
            
            credentials = service_account.Credentials.from_service_account_file(
                keyfile,
                scopes=scopes)
            request = Request()
            credentials.refresh(request)
            
            return credentials
        
        except Exception as e:
            raise e
        
        
    def _getSolutions(self):
        '''A list of all active solution/datasets for a Project
        The objects in the list are Solution obects, which have a 1:1 relationship
        with Datasets'''

        solutionsUrl = "{}/projects/{}/locations/{}/solutions".format(self.apiUrl, self.projectId, self.region)
        request = requests.get(solutionsUrl, headers=self.requestHeader)
        
        solutions = list()
        data = request.json()
        
        for s in data['solutions']:
            solutions.append(Solution(s, self))
    
        return solutions

    
class Solution:
    '''A VIAI Solution object'''

    def __init__(self, data, VIAI):
       
        self.VIAI = VIAI
        for k,v in data.items():
            if type(v) is dict:
                exec("self.{} = {}".format(k,v))
            else:
                exec("self.{} = '{}'".format(k,v)) 
        
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])        
        self.datasetUrl = "{}/projects/{}/locations/{}/datasets/{}".format(VIAI.apiUrl, VIAI.projectId, VIAI.region, self.datasetId)
        self.annotationSets = self._getAnnotationSets()
        self.annotationSpecs = self._getAnnotationSpecs()
        self.images = self._getImages()
        
    def _getAnnotationSets(self):
        '''Pulls associated annotation sets for a Dataset/Solution
        Returns a list of AnnoationSet objects'''
        
        annotationset_url = "{}/{}".format(self.datasetUrl, 'annotationSets')
        r = requests.get(annotationset_url, headers=self.VIAI.requestHeader)
        
        annotationSets = list()
        
        data = r.json()
        for a in data['annotationSets']:
            annotationSets.append(AnnotationSet(a, self.VIAI))
            
        return annotationSets
    
    def _getAnnotationSpecs(self):
        '''Pulls associated annotation specs for a Dataset/Solution
        Returns a list of AnnotationSpec objects'''
        
        annotationspec_url = "{}/{}".format(self.datasetUrl, 'annotationSpecs')
        r = requests.get(annotationspec_url, headers=self.VIAI.requestHeader)
        
        annotationSpecs = list()
        
        data = r.json()
        for a in data['annotationSpecs']:
            annotationSpecs.append(AnnotationSpec(a, self.VIAI))
            
        return annotationSpecs 
    
    def _getImages(self):
        '''Pulls associated images within a dataset.
        Returns a list of Image objects'''
        
        images_url = "{}/{}".format(self.datasetUrl, 'images')
        r = requests.get(images_url, headers=self.VIAI.requestHeader)
        
        images = list()
        
        data = r.json()
        for a in data['images']:
            images.append(Image(a, self.VIAI))
            
        return images             

        
   


