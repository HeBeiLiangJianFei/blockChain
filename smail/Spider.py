import requests
import json
import re

url = 'https://list.vip.com/api-ajax.php?callback=getMerchandiseDroplets1&getPart=getMerchandiseInfoList&productIds=640820994%2C640820963%2C640820816%2C640820829%2C640821094%2C640821173%2C640821068%2C640820892%2C640822365%2C640821175%2C640820853%2C640820864%2C640822401%2C640820806%2C640820905%2C640821170%2C640822489%2C640820975%2C640822462%2C640823376%2C640821079%2C640821061%2C640820962%2C640821104%2C640823433%2C640821034%2C640820964%2C640820844%2C640822395%2C640823437%2C640821162%2C640821051%2C640822413%2C640821023%2C640822419%2C640821097%2C640820939%2C640822473%2C640823375%2C640822399%2C640821018%2C640820917%2C640820907%2C640820943%2C640823383%2C640823447%2C640823396%2C640821070%2C640822488%2C640822430&r=3469104&preview=0&sell_time_from=&time_from=&token=&_=1536892904329'

response = requests.get(url)
data = response.text
fa = json.dumps(data)
faa = fa['data\\']
print(faa)