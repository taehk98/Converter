import os
import boto3
import json
from botocore.exceptions import NoCredentialsError

def extract_text_from_image(image_file_name):
    bucket_name = "taeimagetotext"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'aws_keys.json')
    
    with open(file_path) as f:
        aws_keys = json.load(f)
    
    # Setting up aws account and textract
    aws_access_key_id = aws_keys['access_key']
    aws_secret_access_key = aws_keys['secret_key']
    region_name = 'us-east-1'
    
    s3 = boto3.client('s3', region_name=region_name,
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key)
    
    textract = boto3.client('textract', region_name=region_name,
                            aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key)
    
    # Uploading an image file to S3
    s3.upload_file(image_file_name, bucket_name, image_file_name)

    # Starting textract
    try:
        response = textract.detect_document_text(
            Document={'S3Object': {'Bucket': bucket_name, 'Name': image_file_name}}
        )

        # Getting extracted text
        extracted_text = ''
        for item in response['Blocks']:
            if item['BlockType'] == 'LINE':
                extracted_text += item['Text'] + '\n'

        # Saving the text
        text_output_filename = os.path.join(current_dir, "output.txt")
        with open(text_output_filename, 'w') as f:
            f.write(extracted_text)

        print(f"Text extracted and saved to: {text_output_filename}")
    except NoCredentialsError:
        print("Credentials not available")
    except Exception as e:
        print(f"An error occurred: {e}")