import json
import requests
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