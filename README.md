# VIAI-SDK

A project to make working with the VIAI (https://cloud.google.com/solutions/visual-inspection-ai) REST API easier. 

## Design

The current pre-alpha design: ![VIAI-SDK Class Degign](img/viai-sdk.drawio.png)

## Usage

Basic tasks for the VIAI SDK.

### Starting out

```
>>> from viai import VIAI
>>> a = VIAI(keyfile='viai-key.json')
>>> dir(a)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_getAuthCredentials', '_getSolutions', '_loadAllSolutions', 'apiUrl', 'author', 'credentials', 'projectId', 'region', 'requestHeader', 'solutions']
```

## Loading a Solution/Dataset

```
>>> b = a.solutions[0]
>>> b
<viai.Solution object at 0x7ff0a9497310>
>>> dir(b)
['VIAI', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_getAnnotationSets', '_getAnnotationSpecs', '_getImages', 'createTime', 'datasetId', 'datasetUrl', 'displayName', 'load', 'name', 'solutionType', 'updateTime', 'url']
>>> b.load()
```

## Working with images in a solution

```
>>> c = b.images[0]
>>> c.name
'projects/953081663119/locations/us-central1/datasets/2943948980440006656/images/12773370737795604'
>>> c.sourceGcsUri
'gs://processedstyle3/IMG_1970.HEIC.jpg'
>>> d = c.getGcsBlob()
>>> dir(d)
['STORAGE_CLASSES', '_CHUNK_SIZE_MULTIPLE', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_acl', '_bucket', '_changes', '_chunk_size', '_do_download', '_do_multipart_upload', '_do_resumable_upload', '_do_upload', '_encryption_headers', '_encryption_key', '_extract_headers_from_download', '_get_content_type', '_get_download_url', '_get_transport', '_get_upload_arguments', '_get_writable_metadata', '_initiate_resumable_upload', '_patch_property', '_properties', '_query_params', '_require_client', '_set_properties', 'acl', 'bucket', 'cache_control', 'chunk_size', 'client', 'component_count', 'compose', 'content_disposition', 'content_encoding', 'content_language', 'content_type', 'crc32c', 'create_resumable_upload_session', 'custom_time', 'delete', 'download_as_bytes', 'download_as_string', 'download_as_text', 'download_to_file', 'download_to_filename', 'encryption_key', 'etag', 'event_based_hold', 'exists', 'from_string', 'generate_signed_url', 'generation', 'get_iam_policy', 'id', 'kms_key_name', 'make_private', 'make_public', 'md5_hash', 'media_link', 'metadata', 'metageneration', 'name', 'open', 'owner', 'patch', 'path', 'path_helper', 'public_url', 'reload', 'retention_expiration_time', 'rewrite', 'self_link', 'set_iam_policy', 'size', 'storage_class', 'temporary_hold', 'test_iam_permissions', 'time_created', 'time_deleted', 'update', 'update_storage_class', 'updated', 'upload_from_file', 'upload_from_filename', 'upload_from_string', 'user_project']
```

## Contributing

Merge requests are always welcome, and reach out to me at jamieduncan@google.com with ideas and questions!