# -*- coding: utf-8 -*-
# @see <https://docs.min.io/docs/python-client-api-reference#put_object>

import io
import numpy as np
from minio import Minio


endpoint = str()
access_key = str()
secret_key = str()
secure = False
bucket_name = str()
object_name = str()
client = None


def on_set(key, val):
    if key == 'endpoint':
        global endpoint
        endpoint = str(val)
    elif key == 'access_key':
        global access_key
        access_key = str(val)
    elif key == 'secret_key':
        global secret_key
        secret_key = str(val)
    elif key == 'secure':
        global secure
        secure = bool(secure)
    elif key == 'bucket_name':
        global bucket_name
        bucket_name = str(val)
    elif key == 'object_name':
        global object_name
        object_name = str(val)


def on_get(key):
    if key == 'bucket_name':
        return str(bucket_name)
    elif key == 'object_name':
        return str(object_name)


def on_create():
    return True


def on_init():
    global client
    client = Minio(endpoint,
                   access_key=access_key,
                   secret_key=secret_key,
                   secure=secure)
    return True


def on_valid():
    return bucket_name and object_name


def on_run(put_data):
    if not bucket_name:
        raise RuntimeError('Empty bucket name.')
    if not object_name:
        raise RuntimeError('Empty object name.')
    buffer = put_data.tobytes()
    client.put_object(bucket_name, object_name, io.BytesIO(buffer), len(buffer))


def on_destroy():
    return True


if __name__ == '__main__':
    pass
