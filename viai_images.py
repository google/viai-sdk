import json
import requests
import re
from google.cloud import storage

class Image:
    '''A VIAI Image Object'''
    
    def __init__(self, data, VIAI):
        
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])
        self.VIAI = VIAI
        self.log = VIAI.log
        
        self.log.debug("Loading Image Options")
        for k,v in data.items():
            if type(v) is dict:
                exec("self.{} = {}".format(k,v))
            else:
                exec("self.{} = '{}'".format(k,v))
        self.annotations = self._getAnnotations()
        
    def getGcsBlob(self):
        '''Returns a GCS blob object for an Image'''
        
        # we need to massage the soruce string
        try:
            self.log.debug("Loading GCS Blob Object")
            bucket,filename = re.sub('gs://','', self.sourceGcsUri).split('/',1)
            storage_client = storage.Client()
            bkt = storage_client.get_bucket(bucket)
            blob = bkt.blob(filename)
            
            return blob

        except Exception as e:
            self.log.debug("Unable to Load GCS Blob Object")
            raise e          


    def _getAnnotations(self):
        '''gets annotations associated with an image
        Returns a list of Annotation objects'''
        
        annotations_url = "{}/{}".format(self.url, 'annotations')
        r = requests.get(annotations_url, headers=self.VIAI.requestHeader)
        
        annotations = list()
        
        data = r.json()
        if 'annotations' in data.keys(): # if there are annotations
            self.log.debug("Loading Image Annotations")
            for a in data['annotations']:
                annotations.append(Annotation(a, self.VIAI))
        
        else:
            self.log.debug("No Image Annotations Available")
        
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
                    exec("self.{} = {}".format(k,v))
                else:
                    exec("self.{} = '{}'".format(k,v))
                    
        except Exception as e:
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
                    
        except Exception as e:
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
        
        except Exception as e:
            self.log.debug("Unable to Load Annotation Spec")
            raise e