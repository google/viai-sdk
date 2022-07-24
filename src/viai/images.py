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
import re
import logging
from google.cloud import storage

class Image:
    '''A VIAI Image Object'''
    
    def __init__(self, data, VIAI):
        
        self.log = VIAI.log
        self.VIAI = VIAI
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])
        
        self.log.debug("Loading Image Options")
        for k,v in data.items():
            if type(v) is dict: 
                exec("self.{} = {}".format(k,v))
            else:
                exec("self.{} = '{}'".format(k,v))
        
        self.annotations = self._getAnnotations()
        
    def getGcsBlob(self):
        '''Returns a GCS blob object for an Image'''
        

        try:    # pragma: no cover
            self.log.debug("Loading GCS Blob Object")
            bucket,filename = re.sub('gs://','', self.sourceGcsUri).split('/',1)
            storage_client = storage.Client()
            bkt = storage_client.get_bucket(bucket)
            blob = bkt.blob(filename)
            
            return blob

        except Exception as e:  # pragma: no cover
            self.log.debug("Unable to Load GCS Blob Object")
            raise e          


    def _getAnnotations(self):
        '''gets annotations associated with an image
        Returns a list of Annotation objects'''
    
        annotations_url = "{}/{}".format(self.url, 'annotations')
        r = requests.get(annotations_url, headers=self.VIAI.requestHeader)
        
        annotations = list()
        
        if r.status_code == 200:
            data = r.json()
            if 'annotations' in data.keys():
                self.log.debug("Loading Image Annotations")
                for a in data['annotations']:
                    annotations.append(Annotation(a, self.VIAI))
            
        else:
            self.log.debug("No Image Annotations Available - {}".format(self.name))
            
        return annotations 
    
class Annotation:
    '''A VIAI Image Annotation'''          
    
    def __init__(self, data, VIAI):
        
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])
        self.log = VIAI.log
        
        try:
            self.log.debug("Loading Annotation Parameters")
            for k,v in data.items():
                if type(v) is dict:
                    # Issue #3 would go here
                    exec("self.{} = {}".format(k,v))
                else:
                    exec("self.{} = '{}'".format(k,v))
                    
        except Exception as e: # pragma: no cover
            self.log.debug("Unable to load Annotation - {}".format(data['name']))
            raise e
                
class AnnotationSet:
    '''A VIAI Annotation Set'''
    
    def __init__(self, data, VIAI):
        
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])
        self.log = VIAI.log
        
        try:
            self.log.debug("Loading AnnotationSet Parameters")
            for k,v in data.items():
                if type(v) is dict:
                    exec("self.{} = {}".format(k,v))
                else:
                    exec("self.{} = '{}'".format(k,v))
                    
        except Exception as e: # pragma: no cover
            self.log.debug("Unable to load Annotation Set")
            raise e
        
            
class AnnotationSpec:
    '''A VIAI Annotation Spec'''
    
    def __init__(self, data, VIAI):
        
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])
        self.log = VIAI.log 
        
        try:
            self.log.debug("Loading AnnotationSpec Parameters")
            for k,v in data.items():
                if type(v) is dict:
                    exec("self.{} = {}".format(k,v))
                else:
                    exec("self.{} = '{}'".format(k,v))
        
        except Exception as e: # pragma: no cover
            self.log.debug("Unable to Load Annotation Spec")
            raise e