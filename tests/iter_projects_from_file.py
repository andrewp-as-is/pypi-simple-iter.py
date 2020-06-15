import pypi_simple_iter
import requests

r = requests.get('https://pypi.org/simple/')
open('/tmp/simple.txt','w').write(r.text)
for slug, name in pypi_simple_iter.iter_projects_from_file('/tmp/simple.txt'):
    print(slug,name)
