#!/usr/bin/env python
#-*- coding: utf-8 -*-
import boto3 as boto3
#local import
import config as cfg


KEY_ID = cfg.KEY_ID
SECRET_KEY = cfg.SECRET_KEY
PATH_FILE_UPLOAD = cfg.PATH_FILE_UPLOAD
PATH_FILE_BACKET = cfg.PATH_FILE_BACKET
BACKET_NAME = cfg.BACKET_NAME


def connect_to_yc(key_id: str, secret_key: str):
    session = boto3.session.Session(aws_access_key_id=key_id, aws_secret_access_key=secret_key)
    yc_client = session.client(service_name='s3', endpoint_url='https://storage.yandexcloud.net')
    return yc_client


def upload_to_yc_backet(path_to_upload_file: str,
                        backet_name: str,
                        path_to_backet: str,
                        yc_client: boto3.Session.client):
    yc_client.upload_file(path_to_upload_file, backet_name, path_to_backet)


def get_object_list_on_backet(yc_client: boto3.Session.client, backet_name: str):
    for key in yc_client.list_objects(Bucket=backet_name)['Contents']:
        print(key['Key'])


upload_to_yc_backet(PATH_FILE_UPLOAD,
                    BACKET_NAME,
                    PATH_FILE_BACKET,
                    connect_to_yc(KEY_ID, SECRET_KEY))

get_object_list_on_backet(connect_to_yc(KEY_ID, SECRET_KEY), BACKET_NAME)


if __name__ == '__main__':
    print('')