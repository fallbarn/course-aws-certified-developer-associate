def lambda_handler(event, context):
    print("In lambda handler")
    
    #  sle note: Return json including header and body.
    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "Keep being awesome Cloud Gurus!"
    }
    
    return resp
