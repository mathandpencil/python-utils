import boto3
import logging

__aws_access_key_id = 'xxxxx'
__aws_secret_access_key = 'yyyyyyyy'

logger = logging.getLogger(__name__)

class S3(object):

    def __init__(self, aws_access_key_id, aws_secret_access_key):
        self.aws_access_key_id =  aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self._S3 = boto3.resource('s3')

    def get_file_from_s3(self, bucket_name, file_name_on_s3, file_name_on_hd):
        """ get a file from a bucket to your local hard drive off of s3"""
        obj = self._S3.Object(bucket_name, file_name_on_s3)
        with open(file_name_on_hd, "a+") as file:
            file.write(obj.get()['Body'].read().decode('utf-8'))

    def add_file_to_s3(self, bucket_name, name_on_s3, path_to_file):
        """ add a file to a random bucket on s3."""
        self._S3.Bucket(bucket_name).put_object(
            Key=name_on_s3,
            Body=open(path_to_file, 'rb'))
        logger.info(u'{} was added to {} as name {}'.format(
            path_to_file,
            bucket_name,
            name_on_s3,
        ))

    def get_secure_url(self):
        """ get the secure url of an object on s3."""

if __name__ == "__main__":
    _s3 = S3(__aws_access_key_id, __aws_secret_access_key)

    _data = {
        'bucket_name': 'da-bucket',
        'name_on_s3': 'da-file-name-on-s3',
        'path_to_file': 'da-path-on-your-local-hardrive',
    }
    _s3.add_file_to_s3(**_data)

    _s3.get_file_from_s3('da-bucket', 'da-file-name-on-s3', 'da-new-file-name')
