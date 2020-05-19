# -*- coding: utf-8 -*-
# @see <https://docs.min.io/docs/python-client-api-reference#put_object>

import io
import numpy as np
from minio import Minio
import sys


EXTENSION_TXT_NAME = '.txt'
EXTENSION_CSS_NAME = '.css'
EXTENSION_CSV_NAME = '.csv'
EXTENSION_HTML_NAME = '.htm or .html'
EXTENSION_ICS_NAME = '.ics'
EXTENSION_MJS_NAME = '.mjs'
EXTENSION_JS_NAME = '.js'
EXTENSION_BMP_NAME = '.bmp'
EXTENSION_GIF_NAME = '.gif'
EXTENSION_JPEG_NAME = '.jpg or .jpeg'
EXTENSION_PNG_NAME = '.png'
EXTENSION_SVG_NAME = '.svg'
EXTENSION_TIF_NAME = '.tif or .tiff'
EXTENSION_WEBP_NAME = '.webp'
EXTENSION_ACC_NAME = '.acc'
EXTENSION_MID_NAME = '.mid or .midi'
EXTENSION_MP3_NAME = '.mp3'
EXTENSION_OGA_NAME = '.oga'
EXTENSION_OPUS_NAME = '.opus'
EXTENSION_WAV_NAME = '.wav'
EXTENSION_WEBA_NAME = '.weba'
EXTENSION_3GP_NAME = '.3gp'
EXTENSION_3G2_NAME = '.3g2'
EXTENSION_AVI_NAME = '.avi'
EXTENSION_MPEG_NAME = '.mpeg'
EXTENSION_OGV_NAME = '.ogv'
EXTENSION_TS_NAME = '.ts'
EXTENSION_WEBM_NAME = '.webm'
EXTENSION_ABW_NAME = '.abw'
EXTENSION_ARC_NAME = '.arc'
EXTENSION_AZW_NAME = '.azw'
EXTENSION_BIN_NAME = '.bin'
EXTENSION_BZ_NAME = '.bz'
EXTENSION_BZ2_NAME = '.bz2'
EXTENSION_CSH_NAME = '.csh'
EXTENSION_DOC_NAME = '.doc'
EXTENSION_DOCX_NAME = '.docx'
EXTENSION_EOT_NAME = '.eot'
EXTENSION_EPUB_NAME = '.epub'
EXTENSION_GZ_NAME = '.gz'
EXTENSION_JAR_NAME = '.jar'
EXTENSION_JSON_NAME = '.json'
EXTENSION_JSONID_NAME = '.jsonld'
EXTENSION_MPKG_NAME = '.mpkg'
EXTENSION_ODP_NAME = '.odp'
EXTENSION_ODS_NAME = '.ods'
EXTENSION_ODT_NAME = '.odt'
EXTENSION_OGX_NAME = '.ogx'
EXTENSION_PDF_NAME = '.pdf'
EXTENSION_PHP_NAME = '.php'
EXTENSION_PPT_NAME = '.ppt'
EXTENSION_PPTX_NAME = '.pptx'
EXTENSION_RAR_NAME = '.rar'
EXTENSION_RTF_NAME = '.rtf'
EXTENSION_SH_NAME = '.sh'
EXTENSION_SWF_NAME = '.swf'
EXTENSION_TAR_NAME = '.tar'
EXTENSION_VSD_NAME = '.vsd'
EXTENSION_XHTML_NAME = '.xhtml'
EXTENSION_XLS_NAME = '.xls'
EXTENSION_XLSX_NAME = '.xlsx'
EXTENSION_XML_NAME = '.xml'
EXTENSION_XUL_NAME = '.xul'
EXTENSION_ZIP_NAME = '.zip'
EXTENSION_7Z_NAME = '.7z'
EXTENSION_OTF_NAME = '.otf'
EXTENSION_TTF_NAME = '.ttf'
EXTENSION_WOFF_NAME = '.woff'
EXTENSION_WOFF2_NAME = '.woff2'


NAME_EXTENSTION_TO_MIME = {
    EXTENSION_TXT_NAME : 'text/plain',
    EXTENSION_CSS_NAME : 'text/css',
    EXTENSION_CSV_NAME : 'text/csv',
    EXTENSION_HTML_NAME : 'text/html',
    EXTENSION_ICS_NAME : 'text/calendar',
    EXTENSION_MJS_NAME : 'text/javascript',
    EXTENSION_JS_NAME : 'text/javascript',
    EXTENSION_BMP_NAME : 'image/bmp',
    EXTENSION_GIF_NAME : 'image/gif',
    EXTENSION_JPEG_NAME : 'image/jpeg',
    EXTENSION_PNG_NAME : 'image/png',
    EXTENSION_SVG_NAME : 'image/svg+xml',
    EXTENSION_TIF_NAME : 'image/tiff',
    EXTENSION_WEBP_NAME : 'image/webp',
    EXTENSION_ACC_NAME : 'audio/aac',
    EXTENSION_MID_NAME : 'audio/midi',
    EXTENSION_MP3_NAME : 'audio/mpeg',
    EXTENSION_OGA_NAME : 'audio/ogg',
    EXTENSION_OPUS_NAME : 'audio/opus',
    EXTENSION_WAV_NAME : 'audio/wav',
    EXTENSION_WEBA_NAME : 'audio/webm',
    EXTENSION_3GP_NAME : 'video/3gpp',
    EXTENSION_3G2_NAME : 'video/3gpp2',
    EXTENSION_AVI_NAME : 'video/x-msvideo',
    EXTENSION_MPEG_NAME : 'video/mpeg',
    EXTENSION_OGV_NAME : 'video/oggv',
    EXTENSION_TS_NAME : 'video/mp2t',
    EXTENSION_WEBM_NAME : 'video/webm',
    EXTENSION_ABW_NAME : 'application/x-abiword',
    EXTENSION_ARC_NAME : 'application/x-freearc',
    EXTENSION_AZW_NAME : 'application/vnd.amazon.ebook',
    EXTENSION_BIN_NAME : 'application/octet-stream',
    EXTENSION_BZ_NAME : 'application/x-bzip',
    EXTENSION_BZ2_NAME : 'application/x-bzip2',
    EXTENSION_CSH_NAME : 'application/x-csh',
    EXTENSION_DOC_NAME : 'application/msword',
    EXTENSION_DOCX_NAME : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    EXTENSION_EOT_NAME : 'application/vnd.ms-fontobject',
    EXTENSION_EPUB_NAME : 'application/epub+zip',
    EXTENSION_GZ_NAME : 'application/gzip',
    EXTENSION_JAR_NAME : 'application/java-archive',
    EXTENSION_JSON_NAME : 'application/json',
    EXTENSION_JSONID_NAME : 'application/ld+json',
    EXTENSION_MPKG_NAME : 'application/vnd.apple.installer+xml',
    EXTENSION_ODP_NAME : 'application/vnd.oasis.opendocument.presentation',
    EXTENSION_ODS_NAME : 'application/vnd.oasis.opendocument.spreadsheet',
    EXTENSION_ODT_NAME : 'application/vnd.oasis.opendocument.text',
    EXTENSION_OGX_NAME : 'application/ogg',
    EXTENSION_PDF_NAME : 'application/pdf',
    EXTENSION_PHP_NAME : 'application/x-httpd-php',
    EXTENSION_PPT_NAME : 'application/vnd.ms-powerpoint',
    EXTENSION_PPTX_NAME : 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    EXTENSION_RAR_NAME : 'application/vnd.rar',
    EXTENSION_RTF_NAME : 'application/rtf',
    EXTENSION_SH_NAME : 'application/x-sh',
    EXTENSION_SWF_NAME : 'application/x-shockwave-flash',
    EXTENSION_TAR_NAME : 'application/x-tar',
    EXTENSION_VSD_NAME : 'application/vnd.visio',
    EXTENSION_XHTML_NAME : 'application/xhtml+xml',
    EXTENSION_XLS_NAME : 'application/vnd.ms-excel',
    EXTENSION_XLSX_NAME : 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    EXTENSION_XML_NAME : 'application/xml',
    EXTENSION_XUL_NAME : 'application/vnd.mozilla.xul+xml',
    EXTENSION_ZIP_NAME : 'application/zip',
    EXTENSION_7Z_NAME : 'application/x-7z-compressed',
    EXTENSION_OTF_NAME : 'font/otf',
    EXTENSION_TTF_NAME : 'font/ttf',
    EXTENSION_WOFF_NAME : 'font/woff',
    EXTENSION_WOFF2_NAME : 'font/woff2'

}
NAME_MIME_TO_EXTENSTION = {v: k for k, v in NAME_EXTENSTION_TO_MIME.items()}


endpoint = str()
access_key = str()
secret_key = str()
secure = False
bucket_name = str()
object_name = str()
client = None
extension = 'text/plain'

def on_set(key, val):
    # sys.stdout.write(f"k: {key}, v: {val}\n")
    # sys.stdout.flush()
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
    elif key == 'extension':
        global extension
        extension = NAME_EXTENSTION_TO_MIME[val]


def on_get(key):
    if key == 'extension':
        return NAME_MIME_TO_EXTENSTION[extension]


def on_init():
    global client
    # sys.stdout.write(f"[MinioPutObject] endpoint: {endpoint}, access: {access_key}, secret: {secret_key}, secure: {secure}")
    # sys.stdout.flush()

    client = Minio(endpoint,
                   access_key=access_key,
                   secret_key=secret_key,
                   secure=secure)
    return True


def on_valid():
    return True


def on_run(bucket_name, object_name, data):
    #sys.stdout.write(f"[MinioPutObject] bucket name: {bucket_name}, object name: {object_name}")
    #sys.stdout.flush()
    if len(bucket_name) <= 0:
        raise RuntimeError('Empty bucket name.')
    if len(object_name) <= 0:
        raise RuntimeError('Empty object name.')

    b_name = "".join([chr(item) for item in bucket_name])
    o_name = "".join([chr(item) for item in object_name])

    buffer = data.tobytes()
    client.put_object(b_name, o_name, io.BytesIO(buffer), len(buffer), extension)


def on_destroy():
    return True


if __name__ == '__main__':
    pass
