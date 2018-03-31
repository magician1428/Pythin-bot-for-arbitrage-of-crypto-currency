 '''
Created on Nov 24, 2017

@author: seanm99
'''

import json
import requests
import time
import hmac
import hashlib

normal = "634f7ed4ca0c47e09cf28ca3ab7ec3e2"
apisecret = "c0cc5b13b6a64cfc9d66cffb106bfbe7"

n=time.time()
uri="https://bittrex.com/api/v1.1/account/getbalances?apikey=634f7ed4ca0c47e09cf28ca3ab7ec3e2&nonce="+str(n)

# https://github.com/ndri/python-bittrex/blob/master/bittrex.py
sign = hmac.new(b"c0cc5b13b6a64cfc9d66cffb106bfbe7", uri, hashlib.sha512).hexdigest()
headers = {'apisign': sign}
r = requests.get(uri, headers=headers)

text = r.text
parsed = json.loads(text)
limit_buy = parsed.get("result")
print(parsed)