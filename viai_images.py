import json
import requests
import re
from google.cloud import storage

class Image:
    '''A VIAI Image Object'''
    
    def __init__(self, data, VIAI):
        
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])
        self.VIAI = VIAI
        for k,v in data.items():
            if type(v) is dict:
                exec("self.{} = {}".format(k,v))
            else:
                exec("self.{} = '{}'".format(k,v))
        self.annotations = self._getAnnotations()
        
    def getGcsBlob(self):
        '''Returns a GCS blob object for an Image'''
        
        # we need to massage the soruce string
        bucket,filename = re.sub('gs://','', self.sourceGcsUri).split('/',1)
        storage_client = storage.Client()
        bkt = storage_client.get_bucket(bucket)
        blob = bkt.blob(filename)
                
        return blob
        
                
    def _getAnnotations(self):
        '''gets annotations associated with an image
        Returns a list of Annotation objects'''
        
        annotations_url = "{}/{}".format(self.url, 'annotations')
        r = requests.get(annotations_url, headers=self.VIAI.requestHeader)
        
        annotations = list()
        
        data = r.json()
        if 'annotations' in data.keys(): # if there are annotations
            for a in data['annotations']:
                annotations.append(Annotation(a, self.VIAI))
            
        return annotations 
    
class Annotation:
    '''A VIAI Image Annotation'''          
    
    def __init__(self, data, VIAI):
        
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])
        for k,v in data.items():
            if type(v) is dict:
                exec("self.{} = {}".format(k,v))
            else:
                exec("self.{} = '{}'".format(k,v)) 
                
class AnnotationSet:
    '''A VIAI Annotation Set'''
    
    def __init__(self, data, VIAI):
        
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])
        for k,v in data.items():
            if type(v) is dict:
                exec("self.{} = {}".format(k,v))
            else:
                exec("self.{} = '{}'".format(k,v))  
        
            
class AnnotationSpec:
    '''A VIAI Annotation Spec'''
    
    def __init__(self, data, VIAI):
        
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])
        for k,v in data.items():
            if type(v) is dict:
                exec("self.{} = {}".format(k,v))
            else:
                exec("self.{} = '{}'".format(k,v))      