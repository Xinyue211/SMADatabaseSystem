import gzip
import json


def to_json(path):
    json_list = []
    with gzip.open(path, 'rb') as gzip_f:
        raw_json = gzip_f.readline()
        while len(raw_json) > 0:
            json_list.extend(json.loads(raw_json, encoding='utf-8'))

    return json_list
