# Auto Ingestion from local machine to s3 and then to snowflake
## A. Uploading files from local machine to AWS S3 bucket
#### It uploads the data files from local computer to the Amazon AWS S3 bucket using the user credentials
- First step is to import boto3
- And then import os
- store aws_access_key_id and aws_secret_access_key (user's credentials from aws) in session
- Create s3 object using boto3 resource
- Give local file location in file_path and s3 bucket name as a argunment in Bucket()
- Here if condition look for .csv file. You can change it to any file extension you want to upload files.

## B. Ingesting files from AWS S3 to Snowflake
#### It uses snowpipe to integrate with extenal file source(S3 in this case) and upload file in snowflake database
- Create a policy in IAM in AWS
- Create a Role in IAM in AWS
- Create storage integration in Snowflake
- Create database, schema and table with same columns that of file we are going to upload. 
- Create stage in Snowflake
- Create pipe in Snowflake
- Lastly update trust relationship of new role in IAM user with snowflake Iam user id and external_id given by snowpipe
#### Please, refer to [Automating Snowpipe for Amazon S3](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-auto-s3.html#automating-snowpipe-for-amazon-s3 "Reference link to official documentation") for more detail approach of part B.
