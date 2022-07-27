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
import logging
import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from viai.solutions import Solution


class VIAI:
    '''The primary class for handling VIAI objects effectively in Python 
    applications'''
    
    def __init__(self, keyfile=None, connect=True, region='us-central1'):
        
        self.log = self._configureLogging()
        self.version = '0.0.1'
        
        self.apiUrl = "https://visualinspection.googleapis.com/v1"
        self.requestHeader = dict()
        self.projectId = str()
        self.region = region
        
        if connect == True: # pragma: no cover
            self.credentials = self._getAuthCredentials(keyfile)     
            self.solutions = self._getSolutions()
            
    def _configureLogging(self):
        '''Configures logging for a class'''
        
        logFormatter = logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s")
        rootLogger = logging.getLogger()
        
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        rootLogger.addHandler(consoleHandler)
        rootLogger.setLevel(logging.INFO)
        
        return rootLogger
        
    def loadAllSolutions(self):
        '''A helper function to load all solutions in a VIAI object. Depending on the number of datasets and images,
        this can be time-consuming.'''
        
        try:
            self.log.debug("Loading all solutions")
            for s in self.solutions:
                self.log.debug("Loading Solution - {}".format(s))
                s.load()
        except Exception as e:
            raise e
        
    def setLogLevel(self, loglevel):
        '''Sets a log-level for an instance of VIAI'''
        
        try:
            loglevel = loglevel.upper()
            self.log.setLevel(loglevel)
            self.log.info("Set logging level to {}".format(loglevel))
            
        except Exception as e:  # pragma: no cover
            raise e
                       
    def _getAuthCredentials(self, keyfile): # pragma: no cover
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
                self.log.debug("using GOOGLE_APPLICATION_CREDENTIALS variable - {}".format(service_account_file))
            elif keyfile is not None:
                service_account_file = keyfile
                self.log.debug("using keyfile parameter - {}".format(service_account_file))
                os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "{}/{}".format(os.getcwd(), keyfile)  # set the variable for other libraries
            else:
                raise AuthCredentialException
                
            credentials = service_account.Credentials.from_service_account_file(
                service_account_file,
                scopes=scopes)
            request = Request()
            credentials.refresh(request)
            
            self.projectId = credentials.project_id
            self.requestHeader = {"Authorization": "Bearer {}".format(credentials.token)}
            self.log.debug("Successfully Authenticated to GCP")
            
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

        try: 
            self.log.debug("Loading Solutions")
            solutionsUrl = "{}/projects/{}/locations/{}/solutions".format(self.apiUrl, self.projectId, self.region)
            request = requests.get(solutionsUrl, headers=self.requestHeader)
            
            if request.status_code == 200:
                solutions = list()
                data = request.json()
                
                sol_count = 0
                for s in data['solutions']:
                    self.log.debug("Loading Solution - {}".format(sol_count))
                    solutions.append(Solution(s, self))
                    sol_count += 1
        
                return solutions
            
            else:   # pragma: no cover
                self.log.debug("Unable to Access VIAI API - {}".format(solutionsUrl))
                
        except Exception as e: # pragma: no cover
            self.log.debug("Unable to Get Solutions")
            raise e
    
class AuthCredentialException(Exception):   # pragma: no cover
    '''An exception for issues with GCP Authentication'''
    
    def __init__(self):
        self.msg = "{}: Unable to load any valid GCP Service Account Files".format(self.__class__.__name__.upper())
        