import os
import boto3
import json
from botocore.exceptions import NoCredentialsError

def extract_text_from_image(bucket_name, image_file_name, job_name):
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
    # object_name = None
    # if object_name is None:
    #     object_name = os.path.basename(image_file_name)
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
        
# current_dir = os.path.dirname(os.path.abspath(__file__))    
# bucket_name = 'taeimagetotext'
# image_file_name = os.path.join(current_dir, 'testImage.jpg')    
# job_name = 'textract_job_'
# extract_text_from_image(bucket_name, image_file_name, job_name)

# file_path = os.path.join(current_dir, "output.txt")    
# # 텍스트 파일을 읽어서 리스트에 저장
# with open(file_path, 'r') as file:
#     lines = file.readlines()

# # 각 줄에서 개행 문자를 제거하고 리스트에 추가
# result = []
# for line in lines:
#     line = line.strip()  # 각 줄의 앞뒤 공백 및 개행 문자 제거
#     result.append(line)

# # 결과 출력
# print(result)