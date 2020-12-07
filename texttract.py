import boto3
import json


# Document
s3BucketName = "thantoutliersbucket"
documentName = "expense1.png"

# Amazon Textract client
textract = boto3.client('textract')



#main lambda function
def detect(event, context):
    #detect text using textract api
    response = textract.detect_document_text(
        Document={
            'S3Object': {
            'Bucket': s3BucketName,
            'Name': documentName
        }
    })

    line = []
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            #print ('\033[94m' +  item["Text"] + '\033[0m')
            line.append(item["Text"])

    return json.dumps(line)


