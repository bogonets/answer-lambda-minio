# -*- coding: utf-8 -*-
# @see <https://docs.min.io/docs/python-client-api-reference#get_object>

import urllib3
import numpy as np
from minio import Minio


endpoint = str()
access_key = str()
secret_key = str()
secure = False
bucket_name = str()
object_name = str()
request_headers = dict()
sse = dict()
client = None


def str2dict(val: str):
    result = dict()
    for tokens in val.split(','):
        kv = tokens.split('=')
        if len(kv) == 1:
            result[kv[0]] = str()
        elif len(kv) >= 2:
            result[kv[0]] = kv[1]
    return result


def dict2str(val: dict):
    return ','.join(list(map(lambda x: f'{x[0]}={x[1]}', val.items())))


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
    elif key == 'request_headers':
        global request_headers
        request_headers = str2dict(val)
    elif key == 'sse':
        global sse
        sse = str2dict(val)


def on_get(key):
    if key == 'bucket_name':
        return str(bucket_name)
    elif key == 'object_name':
        return str(object_name)
    elif key == 'request_headers':
        return dict2str(request_headers)
    elif key == 'sse':
        return dict2str(sse)


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


def on_run():
    if not bucket_name:
        raise RuntimeError('Empty bucket name.')
    if not object_name:
        raise RuntimeError('Empty object name.')
    data: urllib3.response.HTTPResponse = client.get_object(
        bucket_name,
        object_name,
        request_headers=request_headers,
        sse=sse)
    return {
        'get_data': np.array(np.frombuffer(data.read(), dtype='int'))
    }


def on_destroy():
    return True


if __name__ == '__main__':
    pass
