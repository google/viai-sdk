import os
import json
import requests

class Module:
    '''A VIAI Solution Module'''
    
    def __init__(self, data, VIAI):
        
        self.url = "{}/{}".format(VIAI.apiUrl, data['name'])
        self.VIAI = VIAI # the parent VIAI object
        for k,v in data.items():
            if type(v) is dict:
                exec("self.{} = {}".format(k,v))
            else:
                exec("self.{} = '{}'".format(k,v)) 
                
        self.models = self._getModels()
                
    def _getModels(self):
        '''a getter function for the VIAI Model Class'''
        
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
        for k,v in data.items():
            if type(v) is dict:
                exec("self.{} = {}".format(k,v))
            elif type(v) is list:
                exec("self.{} = list({})".format(k,v))
            else:
                exec("self.{} = '{}'".format(k,v))  