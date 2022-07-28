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

from unittest.mock import patch, Mock
from viai import VIAI


def getSolutionApiData():
    
    solution_api_data = {'solutions': 
    [{'name': 'projects/012456789012/locations/myregion/solutions/0123456789012345678', 
        'displayName': 'solution1', 
        'createTime': '2022-07-16T17:26:14.897814Z', 
        'updateTime': '2022-07-16T17:26:15.862524Z', 
        'datasetId': '5566778899001122334', 
        'solutionType': {'cosmeticInspection': 
            {'inputType': 'POLYGONS', 'moduleType': 
                'OBJECT_DETECTION_MODULE'}}}, 
        {'name': 'projects/012456789012/locations/myregion/solutions/1123456789012345678', 
        'displayName': 'solution2', 
        'createTime': '2022-07-16T17:25:06.193340Z', 
        'updateTime': '2022-07-16T17:25:16.045872Z', 
        'datasetId': '7182399179749064704', 
        'solutionType': {'cosmeticInspection': 
            {'inputType': 'POLYGONS', 'moduleType': 'SEGMENTATION_MODULE'}}}, 
        {'name': 'projects/012456789012/locations/myregion/solutions/2123456789012345678', 
        'displayName': 'solution3', 
        'createTime': '2022-07-16T17:23:29.084506Z', 
        'updateTime': '2022-07-16T17:23:29.901307Z', 
        'datasetId': '5956857131150868480', 
        'solutionType': {'cosmeticInspection': 
            {'inputType': 'POLYGONS', 'moduleType': 'OBJECT_DETECTION_MODULE'}}}
        ]
    }
    
    return solution_api_data

def getImageApiData():
    
    image_api_data = {'images': 
    [{'name': 'projects/012456789012/locations/myregion/datasets/0000000000000000000/images/12773370737795604', 
      'createTime': '2022-07-16T17:27:04.686606Z', 
      'sourceGcsUri': 'gs://bucket1/image1.jpg', 
      'etag': 'AMEw9yM_QO1g7ToYtfiu49WNAQiCZABRtmTP68K1KbdOdzFhHHSI9BTuzXXRbAtSZZZZ'}, 
     {'name': 'projects/012456789012/locations/myregion/datasets/0000000000000000000/images/261072614709075724', 
      'createTime': '2022-07-16T17:27:04.672704Z', 
      'sourceGcsUri': 'gs://bucket1/image2.jpg', 
      'etag': 'AMEw9yPHbDCkIz-m5bxs3zdnd_Tfqhm_y_6RqCC9H3KiZ3WYj0957hpL5REkI5r6YYYY'}, 
     {'name': 'projects/012456789012/locations/myregion/datasets/0000000000000000000/images/762874455825945494', 
      'createTime': '2022-07-16T17:27:04.691594Z', 
      'sourceGcsUri': 'gs://bucket1/image3.jpg', 
      'etag': 'AMEw9yNEs0WZZsDNclqJX_HmP4sNEFealeMUkEcbspeDD5e-MR5Ff7crOf6h48-XXXX'}
    ]}
    
    return image_api_data



def getImageData():
    
    image_data = {'name': 'projects/012456789012/locations/myregion/datasets/012345678910012345678910/images/012345678910123456', 
    'createTime': '2022-07-16T17:27:04.686606Z', 
    'sourceGcsUri': 'gs://bucket1/image1.jpg', 
    'etag': 'AMEw9yPjydy7P0qdAB_QZhw1lg2kS4YdhyqaSRusLdA6WkKNCmqDtbG-BiPvKTOksM5u'}
    
    return image_data

def getModuleApiData():
    
    moduleData = {'modules': 
        [{'name': 'projects/012456789012/locations/myregion/solutions/0123456789012345678/modules/8765432109876543210', 
          'createTime': '2022-07-15T18:15:57.678675Z', 
          'updateTime': '2022-07-15T18:15:57.678675Z', 
          'displayName': 'Object Detection Module', 
          'config': {}, 
          'objectDetection': 
              {'objectRegions': 
                  [{'annotationSetId': '3456789012345678901', 
                    'annotationSet': 'projects/012456789012/locations/myregion/datasets/2345678901234567890/annotationSets/3456789012345678901'
                    }], 
                  'objectRegionPredictions': 
                      [{'annotationSetId': '4567890123456789012', 
                        'annotationSet': 'projects/012456789012/locations/myregion/datasets/2345678901234567890/annotationSets/4567890123456789012'
                        }], 
                    'classificationPredictions': 
                        [{'annotationSetId': '5678901234567890123', 
                          'annotationSet': 'projects/012456789012/locations/myregion/datasets/2345678901234567890/annotationSets/5678901234567890123'
                          }]
                        }
              }
         ]}
    
    return moduleData

def getSolutionArtifactData():
    
    solutionArtifactApiData = {'solutionArtifacts': 
        [{'name': 'projects/012456789012/locations/myregion/solutions/0123456789012345678/solutionArtifacts/6789012345678901234', 
          'createTime': '2022-07-16T16:40:38.612416Z', 
          'displayName': 'mycontainer', 
          'models': 
              ['projects/012456789012/locations/myregion/solutions/0123456789012345678/modules/8765432109876543210/models/001122334455667788'], 
              'exportType': 'CPU_CONTAINER', 
              'containerExportLocation': 
                  {'outputUri': 'gcr.io/myproject/s1h:s1hash'}, 
              'aiplatformModelName': '//aiplatform.googleapis.com/projects/012456789012/locations/myregion/models/8675309867530986753', 
              'purpose': 'unknown'}
         ]}
    
    return solutionArtifactApiData

def getAnnotationApiData():
    
    annotation_api_data = {'annotations': 
    [{'name': 'projects/012456789012/locations/myregion/datasets/2345678901234567890/images/644674171755000023/annotations/505202003928940544', 
    'createTime': '2022-07-16T05:27:08.347970Z', 
    'annotationSpecId': '1364927687407173632', 
    'annotationSetId': '2210832010434314240', 
    'parentAnnotationId': '0', 
    'polygon': 
        {'normalizedBoundingPoly': 
            {'normalizedVertices': 
                [{'x': 0.5571082, 'y': 0.08970523}, 
                {'x': 0.6148128, 'y': 0.08970523}, 
                {'x': 0.6148128, 'y': 0.821314}, 
                {'x': 0.5571082, 'y': 0.821314}]}, 
            'confidenceScore': 0.18633613}, 
        'source': {'type': 'MACHINE_PRODUCED', 
                'sourceModel': 'projects/012456789012/locations/myregion/solutions/0123456789012345678/modules/8765432109876543210/models/001122334455667788'}
        }, 
     {'name': 'projects/012456789012/locations/myregion/datasets/2345678901234567890/images/644674171755000023/annotations/741640984365891584', 
      'createTime': '2022-07-16T05:27:09.592468Z', 
      'annotationSpecId': '1364927687407173632', 
      'annotationSetId': '2210832010434314240', 
      'parentAnnotationId': '0', 
      'polygon': 
          {'normalizedBoundingPoly': {'normalizedVertices': 
              [{'x': 0.65545577}, 
               {'x': 0.69538885}, 
               {'x': 0.69538885, 'y': 0.70678973}, 
               {'x': 0.65545577, 'y': 0.70678973}]}, 
           'confidenceScore': 0.1998433}, 
          'source': 
              {'type': 'MACHINE_PRODUCED', 
               'sourceModel': 'projects/012456789012/locations/myregion/solutions/0123456789012345678/modules/8765432109876543210/models/001122334455667788'}
        }
     ]}
    
    return annotation_api_data

def getAnnotationSetApiData():
    
    annoation_set_api_data = {'annotationSets': 
        [{'name': 'projects/012456789012/locations/myregion/datasets/2345678901234567890/annotationSets/4513015844950769664', 
          'displayName': 'Preview Classification Predictions for models/001122334455667788', 
          'classificationLabel': {}, 
          'createTime': '2022-07-16T05:25:06.641668Z', 
          'updateTime': '2022-07-16T05:25:07.229575Z'}, 
         {'name': 'projects/012456789012/locations/myregion/datasets/2345678901234567890/annotationSets/8871655859315277824', 
          'displayName': 'Suggested-To-Label for models/001122334455667788', 
          'classificationLabel': {}, 
          'createTime': '2022-07-16T05:25:05.337978Z', 
          'updateTime': '2022-07-16T05:25:06.028235Z'}, 
         {'name': 'projects/012456789012/locations/myregion/datasets/2345678901234567890/annotationSets/2210832010434314240', 
          'displayName': 'Preview Object Region Predictions for models/001122334455667788', 
          'polygon': {}, 
          'createTime': '2022-07-16T05:25:03.420088Z', 
          'updateTime': '2022-07-16T05:25:04.440158Z'}, 
         {'name': 'projects/012456789012/locations/myregion/datasets/2345678901234567890/annotationSets/3456789012345678901', 
          'displayName': 'Polygons Regions', 
          'polygon': {}, 
          'createTime': '2022-07-15T18:15:57.414388Z', 
          'updateTime': '2022-07-15T19:59:02.432985Z'}, 
         {'name': 'projects/012456789012/locations/myregion/datasets/2345678901234567890/annotationSets/5678901234567890123', 
          'displayName': 'Predicted Classification Labels', 
          'classificationLabel': {}, 
          'createTime': '2022-07-15T18:15:57.642610Z', 
          'updateTime': '2022-07-15T18:15:57.642610Z'}, 
         {'name': 'projects/012456789012/locations/myregion/datasets/2345678901234567890/annotationSets/4567890123456789012', 
          'displayName': 'Predicted Polygons Regions', 
          'polygon': {}, 'createTime': '2022-07-15T18:15:57.564598Z', 
          'updateTime': '2022-07-15T18:15:57.564598Z'}
    ]}
    
    return annoation_set_api_data

def getAnnotationSpecApiData():
    
    annotation_spec_api_data = {'annotationSpecs': 
        [{'name': 'projects/012456789012/locations/myregion/datasets/2345678901234567890/annotationSpecs/337000313913344', 
          'displayName': 'defect', 
          'createTime': '2022-07-15T18:15:53.943662Z', 
          'updateTime': '2022-07-15T18:15:53.943662Z', 
          'color': {'red': 0.003921569, 'green': 0.654902, 'blue': 0.003921569}}, 
         {'name': 'projects/012456789012/locations/myregion/datasets/2345678901234567890/annotationSpecs/711905741438451712', 
          'displayName': 'included', 
          'createTime': '2022-07-15T18:15:55.397589Z', 
          'updateTime': '2022-07-15T18:15:55.397589Z', 
          'color': {'red': 0.44313726, 'green': 0.0627451, 'blue': 0.5019608}}, 
         {'name': 'projects/012456789012/locations/myregion/datasets/2345678901234567890/annotationSpecs/1364927687407173632', 
          'displayName': 'line', 
          'createTime': '2022-07-15T18:23:19.503174Z',
          'updateTime': '2022-07-15T18:23:19.503174Z', 
          'color': {'red': 0.7607843, 'green': 0.6666667, 'blue': 0.22352941}}, 
         {'name': 'projects/012456789012/locations/myregion/datasets/2345678901234567890/annotationSpecs/1900011618134130688', 
          'displayName': 'excluded', 
          'createTime': '2022-07-15T18:15:56.660784Z', 
          'updateTime': '2022-07-15T18:15:56.660784Z', 
          'color': {'red': 0.68235296, 'green': 0.6509804, 'blue': 0.8156863}}
         ]
        }
 
    return annotation_spec_api_data

def getModelApiData():
    
    ModelApiData = {'models': [{
        'name': 'projects/012456789012/locations/myregion/solutions/0123456789012345678/modules/8765432109876543210/models/001122334455667788', 
        'createRequestTime': '2022-07-15T20:01:27.082718Z', 
        'createTime': '2022-07-15T20:01:27.082718Z', 
        'updateTime': '2022-07-16T05:28:39.669807Z', 
        'evaluationIds': ['3344556677889900112'], 
        'config': 
            {'model_mode': 'MEDIUM_LEARNING_CAPACITY', 
             'max_training_wall_clock_seconds': 86400}, 
        'trainingDuration': '279972s'}
        ]
    }

    return ModelApiData

def mockSolutionViai():
    
    mock_get_patcher = patch('requests.get')
    mock_get = mock_get_patcher.start()    
    
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = getSolutionApiData()
    
    mock_viai = VIAI(connect=False)
    mock_viai.region = 'myregion'
    mock_viai.projectId = 'myproject'
    mock_viai.solutions = mock_viai._getSolutions()
    mock_get_patcher.stop()
    
    return mock_viai

def mockImageViai():
    
    mock_get_patcher = patch('requests.get')
    mock_get = mock_get_patcher.start()    
    
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = getImageApiData()
    
    mock_viai = mockSolutionViai()  # a VIAI instance with mock'd solution data
    mock_viai.images = mock_viai._getImages()
    mock_get_patcher.stop()
    
    return mock_viai

def mockModuleViai():
    
    mock_get_patcher = patch('requests.get')
    mock_get = mock_get_patcher.start()    
    
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = getModuleApiData()
    
    a = mockSolutionViai()  # a VIAI instance with mock'd solution data
    solution1 = a.solutions[0]
    solution1.modules = a.solutions[0]._getModules()
    mock_get_patcher.stop()
    
    return a
