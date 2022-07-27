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

class Module:
    '''A VIAI Solution Module'''
    
    def __init__(self, data, VIAI):
        
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])
        self.VIAI = VIAI # the parent VIAI object
        self.log = VIAI.log
        self.requestHeader = VIAI.requestHeader
        
        self.log.debug("Loading Module Options")
        for k,v in data.items():
            if type(v) is dict:
                exec("self.{} = {}".format(k,v))
            else:
                exec("self.{} = '{}'".format(k,v)) 
        
        self.models = self._getModels()
                
    def _getModels(self):
        '''a getter function for the VIAI Model Class'''
        
        self.log.debug("Loading Models")
        models_url = "{}/{}".format(self.url, 'models')
        r = requests.get(models_url, headers=self.VIAI.requestHeader)
        
        models = list()
        
        data = r.json()
        if 'models' in data.keys():
            for a in data['models']:
                models.append(Model(a, self.VIAI))
            
        return models  
                
class Model:
    '''A VIAI Module Model'''
    
    def __init__(self, data, VIAI):
        
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])
        self.VIAI = VIAI
        self.log = VIAI.log
        self.requestHeader = VIAI.requestHeader
        
        try:
            self.log.debug("Loading Model Options")
            for k,v in data.items():
                if type(v) is dict:
                    exec("self.{} = {}".format(k,v))
                elif type(v) is list:
                    exec("self.{} = list({})".format(k,v))
                else:
                    exec("self.{} = '{}'".format(k,v))
        except Exception as e:
            self.log.debug("Unable to Load Model Information")
            raise e
        
        try:
            self.log.debug("Loading Evaluations")
            self.evaluations = self._getEvaluations()
        except Exception as e:
            self.log.debug("Unable to Load Evaluations")
            raise e
        
                        
    def _getEvaluations(self):
        '''Used to fetch model evaluations. 
        Returns a list of ModelEvaluation objects'''

        evaluations = list()

        try:
            if self.evaluationIds:
                for evaluation in self.evaluationIds: 
                    self.log.debug("Loading Model Evaluation - {}".format(evaluation))
                    url = "{}/modelEvaluations/{}".format(self.url, evaluation)
                    r = requests.get(url, headers=self.requestHeader)
                    
                    if r.status_code == 200:       
                        if len(r.json()) > 0:
                            data = r.json()
                            evaluations.append(ModelEvaluation(data, self.VIAI))
                        else:
                            self.log.debug("No data in Evaluation ID")
                    else:
                        self.log.debug("Non-OK response code from Model Evaluations")
                                
            return evaluations
        
        except AttributeError:
            pass
        
        except Exception as e:  # pragma: no cover
            raise e
                
class ModelEvaluation:
    '''A VIAI Model Evaluation'''
    
    def __init__(self, data, VIAI):
        
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])
        self.log = VIAI.log
        
        try:
            self.log.debug("Loading ModelEvaluation Options")
            for k,v in data.items():
                if type(v) is dict:
                    exec("self.{} = {}".format(k,v))
                elif type(v) is list:
                    exec("self.{} = list({})".format(k,v))
                else:
                    exec("self.{} = '{}'".format(k,v))

        except Exception as e: # pragma: no cover
            self.log.debug("Unable to Load Model Evaluations")
            raise e
     
                
class SolutionArtifact:
    '''A VIAI Solution Artifact'''
    
    def __init__(self, data, VIAI):
        
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])
        self.VIAI = VIAI
        self.log = VIAI.log
        
        try:
            self.log.debug("Loading Solution Artifact Options")
            for k,v in data.items():
                if type(v) is dict:
                    exec("self.{} = {}".format(k,v))
                elif type(v) is list:
                    exec("self.{} = list({})".format(k,v))
                else:
                    exec("self.{} = '{}'".format(k,v))
        
        except Exception as e: # pragma: no cover
            self.log.debug("Unable to Load Solution Artifacts")
            raise e
        