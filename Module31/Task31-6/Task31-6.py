import requests
import re

req_1 = requests.get('http://www.columbia.edu/~fdc/sample.html')
print(re.findall(r'<h3.+>(.+)</h3>', req_1.text))
