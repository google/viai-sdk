from unittest.mock import patch, Mock
from viai import VIAI


def getSolutionApiData():
    
    solution_api_data = {'solutions': 
    [{'name': 'projects/012456789012/locations/myregion/solutions/0123456789012345678', 
        'displayName': 'solution1', 
        'createTime': '2022-07-16T17:26:14.897814Z', 
        'updateTime': '2022-07-16T17:26:15.862524Z', 
        'datasetId': '2943948980440006656', 
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
      'etag': 'AMEw9yM_QO1g7ToYtfiu49WNAQiCZABRtmTP68K1KbdOdzFhHHSI9BTuzXXRbAtSh5MC'}, 
     {'name': 'projects/012456789012/locations/myregion/datasets/0000000000000000000/images/261072614709075724', 
      'createTime': '2022-07-16T17:27:04.672704Z', 
      'sourceGcsUri': 'gs://bucket1/image2.jpg', 
      'etag': 'AMEw9yPHbDCkIz-m5bxs3zdnd_Tfqhm_y_6RqCC9H3KiZ3WYj0957hpL5REkI5r6r1k3'}, 
     {'name': 'projects/012456789012/locations/myregion/datasets/0000000000000000000/images/762874455825945494', 
      'createTime': '2022-07-16T17:27:04.691594Z', 
      'sourceGcsUri': 'gs://bucket1/image3.jpg', 
      'etag': 'AMEw9yNEs0WZZsDNclqJX_HmP4sNEFealeMUkEcbspeDD5e-MR5Ff7crOf6h48-DTtCC'}
    ]}
    
    return image_api_data

def getImageData():
    
    image_data = {'name': 'projects/012345678910/locations/myregion/datasets/012345678910012345678910/images/012345678910123456', 
    'createTime': '2022-07-16T17:27:04.686606Z', 
    'sourceGcsUri': 'gs://bucket1/image1.jpg', 
    'etag': 'AMEw9yPjydy7P0qdAB_QZhw1lg2kS4YdhyqaSRusLdA6WkKNCmqDtbG-BiPvKTOksM5u'}
    
    return image_data

def getAnnotationApiData():
    
    annotation_api_data = {'annotations': 
    [{'name': 'projects/953081663119/locations/us-central1/datasets/6706706469108056064/images/644674171755000023/annotations/505202003928940544', 
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
                'sourceModel': 'projects/953081663119/locations/us-central1/solutions/8183427551025168384/modules/3552020692041990144/models/213111741742055424'}
        }, 
     {'name': 'projects/953081663119/locations/us-central1/datasets/6706706469108056064/images/644674171755000023/annotations/741640984365891584', 
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
               'sourceModel': 'projects/953081663119/locations/us-central1/solutions/8183427551025168384/modules/3552020692041990144/models/213111741742055424'}
        }
     ]}
    
    return annotation_api_data

def getAnnotationSetApiData():
    
    annoation_set_api_data = {'annotationSets': 
        [{'name': 'projects/953081663119/locations/us-central1/datasets/6706706469108056064/annotationSets/4513015844950769664', 
          'displayName': 'Preview Classification Predictions for models/213111741742055424', 
          'classificationLabel': {}, 
          'createTime': '2022-07-16T05:25:06.641668Z', 
          'updateTime': '2022-07-16T05:25:07.229575Z'}, 
         {'name': 'projects/953081663119/locations/us-central1/datasets/6706706469108056064/annotationSets/8871655859315277824', 
          'displayName': 'Suggested-To-Label for models/213111741742055424', 
          'classificationLabel': {}, 
          'createTime': '2022-07-16T05:25:05.337978Z', 
          'updateTime': '2022-07-16T05:25:06.028235Z'}, 
         {'name': 'projects/953081663119/locations/us-central1/datasets/6706706469108056064/annotationSets/2210832010434314240', 
          'displayName': 'Preview Object Region Predictions for models/213111741742055424', 
          'polygon': {}, 
          'createTime': '2022-07-16T05:25:03.420088Z', 
          'updateTime': '2022-07-16T05:25:04.440158Z'}, 
         {'name': 'projects/953081663119/locations/us-central1/datasets/6706706469108056064/annotationSets/5345337351084179456', 
          'displayName': 'Polygons Regions', 
          'polygon': {}, 
          'createTime': '2022-07-15T18:15:57.414388Z', 
          'updateTime': '2022-07-15T19:59:02.432985Z'}, 
         {'name': 'projects/953081663119/locations/us-central1/datasets/6706706469108056064/annotationSets/6423949461839413248', 
          'displayName': 'Predicted Classification Labels', 
          'classificationLabel': {}, 
          'createTime': '2022-07-15T18:15:57.642610Z', 
          'updateTime': '2022-07-15T18:15:57.642610Z'}, 
         {'name': 'projects/953081663119/locations/us-central1/datasets/6706706469108056064/annotationSets/7718734354708430848', 
          'displayName': 'Predicted Polygons Regions', 
          'polygon': {}, 'createTime': '2022-07-15T18:15:57.564598Z', 
          'updateTime': '2022-07-15T18:15:57.564598Z'}
    ]}
    
    return annoation_set_api_data

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