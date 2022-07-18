import os
import json
import requests
from viai_images import Image, AnnotationSet, AnnotationSpec
from viai_modules import Module

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
        
        
    def load(self):
        '''Loads the various API endpoints for the solution. This is used to save time at instance
        startup for busy environments'''
        
        try:
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
        r = requests.get(solutionartifact_url, headers=self.VIAI.requestHeader)
        
        solutionArtifacts = list()
        
        if r.status_code == 200:
            data = r.json()
            if 'solutionArtifacts' in data.keys():
                for a in data['solutionArtifacts']:
                    solutionArtifacts.append(SolutionArtifact(a, self.VIAI))
                
            return solutionArtifacts        
        
        
    def _getAnnotationSets(self):
        '''Pulls associated annotation sets for a Dataset/Solution
        Returns a list of AnnoationSet objects'''
        
        annotationset_url = "{}/{}".format(self.datasetUrl, 'annotationSets')
        r = requests.get(annotationset_url, headers=self.VIAI.requestHeader)
        
        annotationSets = list()
        
        data = r.json()
        if 'annotationSets' in data.keys():
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
        if 'annotationSpecs' in data.keys():
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
        if 'images' in data.keys():
            for a in data['images']:
                images.append(Image(a, self.VIAI))
            
        return images
    
    def _getModules(self):
        
        '''Pulls associated modules for a solution.
        Returns a list of Module objects'''
        
        modules_url = "{}/{}/{}".format(self.VIAI.apiUrl, self.name, 'modules')
        r = requests.get(modules_url, headers=self.VIAI.requestHeader)
        
        modules = list()
        
        data = r.json()
        if 'modules' in data.keys():
            for a in data['modules']:
                modules.append(Module(a, self.VIAI))
            
        return modules        

class SolutionArtifact:
    '''A VIAI Solution Artifact'''
    
    def __init__(self, data, VIAI):
        
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])
        self.VIAI = VIAI
        
        for k,v in data.items():
            if type(v) is dict:
                exec("self.{} = {}".format(k,v))
            elif type(v) is list:
                exec("self.{} = list({})".format(k,v))
            else:
                exec("self.{} = '{}'".format(k,v))