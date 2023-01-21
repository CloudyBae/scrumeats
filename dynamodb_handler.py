import boto3
from decouple import config


# PATCH IN AWS CREDENTIALS BEFORE EVERY USE
AWS_ACCESS_KEY_ID     ="ASIAXDNIZS3HZVSBAQ6M"
AWS_SECRET_ACCESS_KEY ="a9EKphaKEEL2CMP8/zk+G0U0/9/K2aOM4r5goQXv"
AWS_SESSION_TOKEN     ="FwoGZXIvYXdzEAgaDKqmZ+13ozM58B3qBiK/AQ875rlM9WkubFCr9R1c+juumZp164+4RpQ6XwEcUpuTJZsqt5Wk37SBHc8oSmRG1hjBaoZKYZwMXrGFcJERK4zykZe/EAGsftTd+1fNaMfhfH+1w/CEahOT2K3LzqoS9hxmdKAWuiaZMWvD8moZPUrf4CZikK5dpqX7UG3twvE33nuDbmVSXBwcvKpvxHmzZEO6AG36NhWE/o67TBEGxaNWXpFmAC75kqgYY7mMZqdHDPjvJ2Hl3FpLog2mx766KN6wlpsGMi2ktslwdIJW0PckIEUlSV/qXjY9ePlrelxvQsooB078n668MOLyvauTrE9VaA4="
REGION_NAME           ="us-east-1"


client = boto3.client(
    'dynamodb',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    aws_session_token     = AWS_SESSION_TOKEN,
    region_name           = REGION_NAME,
)

resource = boto3.resource(
    'dynamodb',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    aws_session_token     = AWS_SESSION_TOKEN,
    region_name           = REGION_NAME,
)

# Creates our DynamoDb Table called "Food"
def CreatATableFood():
        
    client.create_table(
        AttributeDefinitions = [ # Name and type of the attributes 
            {
                'AttributeName': 'id',  # Name of the attribute
                'AttributeType': 'N',   # N -> Number (S -> String, B-> Binary)

                'AttributeName': 'food',
                'AttributeType': 'S',

                'AttributeName': 'price',
                'AttributeType': 'N',

                'AttributeName': 'truck',
                'AttributeType': 'S',

                'AttributeName': 'likes',
                'AttributeType': 'N'
            }
        ],
        TableName = 'Food', # Name of the table 
        KeySchema = [       # Partition key/sort key attribute 
            {
                'AttributeName': 'id',   # 'HASH' -> partition key, 'RANGE' -> sort key
                'KeyType'      : 'HASH', 
            
                'AttributeName': 'truck',
                'KeyType'      : 'RANGE'
            }
        ],
        BillingMode = 'PAY_PER_REQUEST',
        Tags = [ # OPTIONAL 
            {
                'Key'  : 'test-resource',
                'Value': 'dynamodb-test'            }
        ]
    )


FoodTable = resource.Table('Food') # Defines FoodTable resource

def addItemToFood(id, food, price, type, truck, likes): # Adds an item with attributes to the table
    response = FoodTable.put_item(
        Item = {
            'id'    :  id,
            'truck' :  truck,
            'food'  :  food,
            'price' :  price,
            'type'  :  type,
            'likes' :  likes
        }
    )  
    return response


def GetItemFromFood(id): # Reads the attributes of an item from the DB with given ID
    response = FoodTable.get_item(
        Key = {
            'id'     : id,
        },
        AttributesToGet=[
            'id', 'food', 'price', 'type', 'truck', 'likes'
        ]
    )   
    return response


def UpdateItemInFood(id, data:dict): # Updates an item listing in the DB | MORE FEATURES TO COME
    response = FoodTable.update_item(
        Key = {
            'id': id
        },
        AttributeUpdates={
            'food': {
                'Value'  : data['food'],
                'Action' : 'PUT' # available options -> DELETE(delete), PUT(set), ADD(increment)
            },
            'price': {
                'Value'  : data['price'],
                'Action' : 'PUT'
            },
            'type': {
                'Value' : data['type'],
                'Action' : 'PUT'
            },
            'likes': {
                'Value' : data['likes'],
                'Action' : 'PUT'
            },
            'truck': {
                'Value' : data['truck'],
                'Action' : 'PUT'
            }
        },
        ReturnValues = "UPDATED_NEW" # returns the new updated values
    )   
    return response

#### "LIKE" FEATURE BELOW IS IN BETA | NOT FULLY CONFIGURED ####

def LikeAFood(id):
    response = FoodTable.update_item(
        Key = {
            'id': id
        },
        AttributeUpdates = {
            'likes': {
                'Value'  : 1,   # Add '1' to the existing value
                'Action' : 'ADD'
            }
        },
        ReturnValues = "UPDATED_NEW"
    )    # The 'likes' value will be of type Decimal, which should be  converted to python int type, to pass the response in json format.    response['Attributes']['likes'] = int(response['Attributes']['likes']) 
    return response



def DeleteAnItemFromFood(id): # Deletes an entry from the DB altogether
    response = FoodTable.delete_item(
        Key = {
            'id': id
        }
    )    
    return response

