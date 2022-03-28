#!/usr/bin/env python
# coding: utf-8

# # Automatic Python Uploader
# ### It uploads the data files from local computer to the Amazon AWS S3 bucket using the user credentials
# - First step is to import boto3
# - And then import os
# - store aws_access_key_id and aws_secret_access_key (user's credentials from aws) in session
# - Create s3 object using boto3 resource
# - Give local file location in file_path and s3 bucket name as a argunment in Bucket()
# - Here if condition look for .csv file. You can change it to any file extension you want to upload files.

# In[5]:


import boto3
import os
#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='AKIAQ6C4XSZDPBW63CHI',
aws_secret_access_key='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'
)
#Creating S3 Resource From the Session.
s3 = session.resource('s3')
for file in os.listdir("/Users/bishal/Downloads/Snowflake-tutorial-main"):
    if '.csv' in file:
        file_path = '/Users/bishal/Downloads/Snowflake-tutorial-main/' + file
        s3.Bucket('bishaltestagain-bucket').upload_file(file_path,file)

