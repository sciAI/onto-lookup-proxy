# swagger_client.ResourceApi

All URIs are relative to *http://176.31.200.199:80*

Method | HTTP request | Description
------------- | ------------- | -------------
[**concepts**](ResourceApi.md#concepts) | **GET** /repositories/{repository}/ontologies/{ontology}/concepts | 
[**ontologies**](ResourceApi.md#ontologies) | **GET** /repositories/{repository}/ontologies | 
[**repositories**](ResourceApi.md#repositories) | **GET** /repositories | 


# **concepts**
> list[Concept] concepts(repository, ontology, plain=plain)





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourceApi()
repository = 'repository_example' # str | 
ontology = 'ontology_example' # str | 
plain = true # bool |  (optional)

try: 
    # 
    api_response = api_instance.concepts(repository, ontology, plain=plain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->concepts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**|  | 
 **ontology** | **str**|  | 
 **plain** | **bool**|  | [optional] 

### Return type

[**list[Concept]**](Concept.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ontologies**
> list[Ontology] ontologies(repository, plain=plain)





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourceApi()
repository = 'repository_example' # str | 
plain = true # bool |  (optional)

try: 
    # 
    api_response = api_instance.ontologies(repository, plain=plain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->ontologies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**|  | 
 **plain** | **bool**|  | [optional] 

### Return type

[**list[Ontology]**](Ontology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories**
> list[Repository] repositories()





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourceApi()

try: 
    # 
    api_response = api_instance.repositories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->repositories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Repository]**](Repository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

