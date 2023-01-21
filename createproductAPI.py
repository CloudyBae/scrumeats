import boto3, json

client = boto3.client('apigateway', region_name='us-east-1')

response = client.create_rest_api(
    name='ProductsApi',
    description='API to get all the food products.',
    minimumCompressionSize=123,
    endpointConfiguration={
        'types': [
            'REGIONAL',
        ]
    }
)
api_id = response["id"]

resources = client.get_resources(restApiId=api_id)
root_id = [resource for resource in resources["items"] if resource["path"] == "/"][0]["id"]

products = client.create_resource(
    restApiId=api_id,
    parentId=root_id,
    pathPart='products'
)
products_resource_id = products["id"]


product_method = client.put_method(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    authorizationType='NONE'
)

product_response = client.put_method_response(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': True,
        'method.response.header.Access-Control-Allow-Origin': True,
        'method.response.header.Access-Control-Allow-Methods': True
    },
    responseModels={
        'application/json': 'Empty'
    }
)

product_integration = client.put_integration(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)


product_integration_response = client.put_integration_response(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    statusCode='200',
    responseTemplates={
        "application/json": json.dumps({
            "product_item_arr": [
                {
                    "product_name_str": "apple pie slice",
                    "product_id_str": "a444",
                    "price_in_cents_int": 595,
                    "description_str":"amazing taste",
                    "tag_str_arr": ["pie slice","on offer"],
                    "special_int": 1
                },{
                    "product_name_str": "chocolate cake slice",
                    "product_id_str": "a445",
                    "price_in_cents_int": 595,
                    "description_str":"chocolate heaven",
                    "tag_str_arr": ["cake slice","on offer"]
                },{
                    "product_name_str": "chocolate cake",
                    "product_id_str": "a446",
                    "price_in_cents_int": 4095,
                    "description_str": "chocolate heaven",
                    "tag_str_arr": ["whole cake", "on offer"]
                }
            ]
        })
    },
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        'method.response.header.Access-Control-Allow-Methods': "'GET'",
        'method.response.header.Access-Control-Allow-Origin': "'*'"
    }
)


print ("DONE")

"""
Copyright @2021 [Amazon Web Services] [AWS]
    
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
