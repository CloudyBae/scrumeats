----------SCRUM EATS READ ME----------

--Please use a search function quickly locate your desired notes section.




    TABLE OF CONTENTS:

        dynamodb_handler notes
        app.py notes
        terraform notes




-----dynamodb_handler.py notes-----


-YOU MUST DO THIS IN ORDER FOR THE APP TO BE ABLE TO COMMUNICATE WITH AWS.

-Find your AWS credentials and paste them in the correct variable slots at the top of dynamodb_handler.py file.
  Be sure to maintain quotation marks around each line of credentials.

  *Config file dedicated to patching in credentials to come soon.*


----end dynamodb_handler notes----


-----app.py notes-----


-NOTE: First-time users may have to manually enter data into their table.
        This app does not currently support the full provisioning of a table with data in it from scratch.
        Please use our associated Terraform file or the desired equivalent.
        However, this app will create a table named "Food" if one does not already exist.


-Use the syntax below when making requests to the DB.


    {
    "food" : "<food>",
    "id"   :  <id>,
    "likes":  <likes>,
    "price": "<price>",
    "truck": "<truck>",
    "type": "<type>"
    }  


-Make sure you are using the correct path for each request type.

    Example:

    The line below is the function that adds an item.

        @app.route('/food', methods=['POST'])

    Go to the location that the app is running on (typically: http://localhost:5000).
    And then add the '/food' (remove single quotes) from the app route line to the end of the address.

    Then make sure you are using the correct function associated with that address.
    In this case we are making a 'POST' request as stated in the methods=['POST'] portion of the line.

    As long as your syntax is correct and you are making the correct type of request to the correct address, your item will post and you should see a message saying that your request was successful.

    If you do not see that message, double check your syntax, request type, and address.

    If problem persists, contact Scrum Eats support for help.


----end app.py notes----