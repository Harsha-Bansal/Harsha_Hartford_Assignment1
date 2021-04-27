import boto3


def list_files(bucket):
    """
    Function to list files in a given S3 bucket
    """
    s3 = boto3.client('s3')
    contents = []

    folder_list = list_folder(bucket, s3)
    for folder in folder_list:
         print(folder)
         contents.append(folder)
    print(contents)
    return contents

def list_filename(bucket,filename):
    s3 = boto3.client('s3')
    contents = []
    file_lists = list_file(bucket,s3,filename)
    print(file_lists)
    for file_list in file_lists:
        if(file_list['Size'] != 0):
	    contents.append(file_list['Key'])
    return contents

def list_file(bucket,s3,filename):
    var = []
    response = s3.list_objects(Bucket=bucket, Prefix=filename+'/')['Contents']
    for content in response:
        var.append(content)
    return var

def list_folder(bucket, s3):
    response = s3.list_objects_v2(Bucket=bucket, Prefix='', Delimiter='/')
#    print(response)
    for content in response.get('CommonPrefixes', '[]'):
        yield content.get('Prefix')
