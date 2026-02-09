import boto3
#import dotenv

dotenv.load_dotenv()


# Initialize S3 client
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_DEFAULT_REGION)

# List all buckets
def list_buckets():
    response = s3.list_buckets()
    return [bucket['Name'] for bucket in response['Buckets']]

# List objects in a bucket
def list_objects(bucket_name, prefix=''):
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    return [obj['Key'] for obj in response.get('Contents', [])]

# Upload file
def upload_file(file_path, bucket_name, object_name=None):
    if object_name is None:
        object_name = file_path
    s3.upload_file(file_path, bucket_name, object_name)

# Download file
def download_file(bucket_name, object_name, file_path):
    s3.download_file(bucket_name, object_name, file_path)

if __name__ == '__main__':
    print("Buckets:", list_buckets())
