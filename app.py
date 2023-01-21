#reqs: flask, boto3, python-decouple
from flask import Flask, request
import json
import dynamodb_handler as dynamodb

app = Flask(__name__)


######################################################
#CHECK THE README FILE FOR INFO ON HOW TO USE THIS APP
######################################################


# Friendly reminder:
# USE THIS SYNTAX IN Postman OR OTHER SIMILAR APP TO ADD TO THE DATABASE | CHOOSE RAW DATA IN JSON FORM

    # data = {
    #         "food" : "<food>",
    #         "id"   :  <id>,
    #         "likes":  <likes>,
    #         "price": "<price>",
    #         "truck": "<truck>",
    #          "type": "<type>"
    #        }    


@app.route('/')
def root_route():
    dynamodb.CreatATableFood()
    return 'Hello World, table created'

#  Add a food entry
#  Route: http://localhost:5000/book
#  Method : POST
@app.route('/food', methods=['POST'])
def addAFood():

    data = request.get_json()
    # id, food, price, type, truck

    response = dynamodb.addItemToFood(data['id'], data['food'], data['price'], data['type'], data['truck'], data['likes'])    
    
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Added successfully',
        }

    return {  
        'msg'     : 'Some error occcured',
        'response': response
    }

#  Read a food entry
#  Route: http://localhost:5000/book/<id>
#  Method : GET
@app.route('/food/<int:id>', methods=['GET'])
def getFood(id):
    response = dynamodb.GetItemFromFood(id)
    
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        
        if ('Item' in response):
            return { 'Item': response['Item'] }

        return { 'msg' : 'Item not found!' }

    return {
        'msg': 'Some error occured',
        'response': response
    }



#  Delete a food entry
#  Route: http://localhost:5000/book/<id>
#  Method : DELETE
@app.route('/food/<int:id>', methods=['DELETE'])
def DeleteAFood(id):

    response = dynamodb.DeleteAnItemFromFood(id)

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Deleted successfully',
        }

    return {  
        'msg'     : 'Some error occcured',
        'response': response
    } 


#  Update a food entry
#  Route: http://localhost:5000/food/<id>
#  Method : PUT
@app.route('/food/<int:id>', methods=['PUT'])
def UpdateAFood(id):

    data = request.get_json()

    # data = {
    #     'food' : '<food>',
    #     'id'   : '<id>',
    #     'likes': '<likes>',
    #     'price': '<price>',
    #     'truck': '<truck>',
    #      'type': '<type>'
    # }

    response = dynamodb.UpdateItemInFood(id, data)

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg'                : 'Updated successfully',
            'ModifiedAttributes' : response['Attributes'],
            'response'           : response['ResponseMetadata']
        }

    return {
        'msg'      : 'Some error occured',
        'response' : response
    }   

#  Like a food
#  Route: http://localhost:5000/like/food/<id>
#  Method : POST
@app.route('/like/food/<int:id>', methods=['POST'])
def LikeFood(id):

    response = dynamodb.LikeAFood(id)

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg'      : 'Liked the food successfully',
            'Likes'    : response['Attributes']['likes'],
            'response' : response['ResponseMetadata']
        }

    return {
        'msg'      : 'Some error occured',
        'response' : response
    }


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)