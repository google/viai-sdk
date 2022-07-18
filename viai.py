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

import os
import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from viai_solutions import Solution


class VIAI:
    '''The primary class for handling VIAI objects effectively in Python 
    applications'''
    
    def __init__(self, keyfile=None, region='us-central1', loadAll=False):
        self.author = 'Jamie Duncan'

        self.region = 'us-central1'
        self.apiUrl = "https://visualinspection.googleapis.com/v1"
        self.credentials = self._getAuthCredentials(keyfile)  
        self.projectId = self.credentials.project_id
        self.region = region
        self.requestHeader = {"Authorization": "Bearer {}".format(self.credentials.token)}
        
        self.solutions = self._getSolutions()
        if loadAll == True:
            self._loadAllSolutions()
        
    def _loadAllSolutions(self):
        '''A helper function to load all solutions in a VIAI object. Depending on the number of datasets and images,
        this can be time-consuming.'''
        
        try:
            for s in self.solutions:
                s.load()
        except Exception as e:
            raise e
            
                
    def _getAuthCredentials(self, keyfile):
        '''internal function to create a valid Google authenticated session and generate a JWT token
        inputs:
        keyfile - a service account json keyfile for a service acccount with at least VIAI admin role bindings'''
        
        scopes = [
            "https://www.googleapis.com/auth/cloud-platform",
            "https://www.googleapis.com/auth/userinfo.email"
            ]
        
        try:
            if os.getenv('GOOGLE_APPLICATION_CREDENTIALS') is not None:
                service_account_file = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
            elif keyfile is not None:
                service_account_file = keyfile
                os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "{}/{}".format(os.getcwd(), keyfile)  # set the variable for other libraries
            else:
                raise AuthCredentialException
                
            credentials = service_account.Credentials.from_service_account_file(
                service_account_file,
                scopes=scopes)
            request = Request()
            credentials.refresh(request)
            
            return credentials
        
        except AuthCredentialException as e:
            print(e.msg)
            raise e
     
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
    
class AuthCredentialException(Exception):
    '''An exception for issues with GCP Authentication'''
    
    def __init__(self):
        self.msg = "{}: Unable to load any valid GCP Service Account Files".format(self.__class__.__name__.upper())

        
   


