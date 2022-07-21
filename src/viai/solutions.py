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
# limitations under the License

import os
import json
import requests
import logging
from viai.images import Image, AnnotationSet, AnnotationSpec
from viai.modules import Module

class Solution:
    '''A VIAI Solution object'''

    def __init__(self, data, VIAI):
       
        self.VIAI = VIAI
        self.log = VIAI.log
        self.requestHeader = VIAI.requestHeader
        self.apiUrl = VIAI.apiUrl
        
        self.log.debug("Loading Solution Options")
        for k,v in data.items():
            if type(v) is dict:
                exec("self.{} = {}".format(k,v))
            else:
                exec("self.{} = '{}'".format(k,v)) 
        
        self.url = "{}/{}".format(self.apiUrl, data['name'])        
        self.datasetUrl = "{}/projects/{}/locations/{}/datasets/{}".format(self.apiUrl, VIAI.projectId, VIAI.region, self.datasetId)     
        
    def load(self):
        '''Loads the various API endpoints for the solution. This is used to save time at instance
        startup for busy environments'''
        
        try:
            self.log.info("Loading Solution Data- {}".format(self.displayName   ))
            self.annotationSets = self._getAnnotationSets()
            self.annotationSpecs = self._getAnnotationSpecs()
            self.images = self._getImages()
            self.modules = self._getModules()
            self.solutionArtifacts = self._getSolutionArtifacts()
        
        except Exception as e:
            raise e
        
    def _getSolutionArtifacts(self):
        '''Pulls associated Solution Artifacts for a Solution
        Returns a list of SolutionArtifact objects'''
        
        solutionartifact_url = "{}/{}".format(self.url, 'solutionArtifacts')
        r = requests.get(solutionartifact_url, headers=self.requestHeader)
        
        solutionArtifacts = list()
        
        if r.status_code == 200:
            self.log.debug("Successfully Retrieved Solution Artifacts")
            data = r.json()
            if 'solutionArtifacts' in data.keys():
                for a in data['solutionArtifacts']:
                    solutionArtifacts.append(SolutionArtifact(a, self.VIAI))
                
            return solutionArtifacts
        else: 
            self.log.debug("Unable to Retrieve Solution Artifact - Response Code: {}",format(r.status_code)) 
        
        
    def _getAnnotationSets(self):
        '''Pulls associated annotation sets for a Dataset/Solution
        Returns a list of AnnoationSet objects'''
        
        annotationset_url = "{}/{}".format(self.datasetUrl, 'annotationSets')
        r = requests.get(annotationset_url, headers=self.requestHeader)
        
        annotationSets = list()
        
        data = r.json()
        if 'annotationSets' in data.keys():
            for a in data['annotationSets']:
                self.log.debug("Annotation Set Retrieved - {}".format(a['name']))
                annotationSets.append(AnnotationSet(a, self.VIAI))
        else:
            self.log.debug("No Annotation Sets Available")
            
        return annotationSets
    
    def _getAnnotationSpecs(self):
        '''Pulls associated annotation specs for a Dataset/Solution
        Returns a list of AnnotationSpec objects'''
        
        annotationspec_url = "{}/{}".format(self.datasetUrl, 'annotationSpecs')
        r = requests.get(annotationspec_url, headers=self.requestHeader)
        
        annotationSpecs = list()
        
        data = r.json()
        if 'annotationSpecs' in data.keys():
            for a in data['annotationSpecs']:
                self.log.debug("Loading Annotation Spec - {}".format(a['name']))
                annotationSpecs.append(AnnotationSpec(a, self.VIAI))
        else:
            self.log.debug("No Annation Specs Available")
            
        return annotationSpecs 
    
    def _getImages(self):
        '''Pulls associated images within a dataset.
        Returns a list of Image objects'''
        
        images_url = "{}/{}".format(self.datasetUrl, 'images')
        r = requests.get(images_url, headers=self.requestHeader)
        
        images = list()
        
        data = r.json()
        if 'images' in data.keys():
            for a in data['images']:
                self.log.debug("Loading Image - {}".format(a['name']))
                images.append(Image(a, self.VIAI))
        else:
            self.log.debug("No Images Available")
            
        return images
    
    def _getModules(self):
        
        '''Pulls associated modules for a solution.
        Returns a list of Module objects'''
        
        modules_url = "{}/{}/{}".format(self.apiUrl, self.name, 'modules')
        r = requests.get(modules_url, headers=self.requestHeader)
        
        modules = list()
        
        data = r.json()
        if 'modules' in data.keys():
            for a in data['modules']:
                self.log.debug("Loading Module - {}".format(a['name']))
                modules.append(Module(a, self.VIAI))
        else:
            self.log.debug("No Modules Available")
            
        return modules        

class SolutionArtifact:
    '''A VIAI Solution Artifact'''
    
    def __init__(self, data, VIAI):
        
        self.url = "{}/{}".format(self.apiUrl, data['name'])
        self.VIAI = VIAI
        self.log = VIAI.log
        
        try: 
            self.log.debug("Loading SolutionArtifact Options")
            for k,v in data.items():
                if type(v) is dict:
                    exec("self.{} = {}".format(k,v))
                elif type(v) is list:
                    exec("self.{} = list({})".format(k,v))
                else:
                    exec("self.{} = '{}'".format(k,v))
        
        except Exception as e:
            self.log.debug("Unable to Load Solution Artifacts")
            raise e