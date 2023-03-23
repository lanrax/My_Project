import json
from urllib import request


def postDetect(url, picture_list, picture_id):
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    formbody = {
        "picture_list": picture_list,
        "picture_id": picture_id
    }
    request_data = json.dumps(formbody).encode()
    response = request.Request(url=url, data=request_data, headers=headers, method='POST')  # set up the url connection
    data = request.urlopen(response).read()  # read the data
    return data
