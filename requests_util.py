import json

import requests


class RequestsUtil:
    session = requests.session()

    def send_request(self, method, url, data, **kwargs):
        header = {"Content-Type": 'application/json'}
        method = str(method).lower()
        rep = None
        if method == 'get':
            rep = RequestsUtil.session.request(method, url=url, params=data, **kwargs)
        # post
        else:
            data = json.dumps(data)
            rep = RequestsUtil.session.request(method, url=url, data=data, headers=header, **kwargs)
        return rep.text
