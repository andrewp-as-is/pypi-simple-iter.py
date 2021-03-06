<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/pypi-simple-iter.svg?maxAge=3600)](https://pypi.org/project/pypi-simple-iter/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/pypi-simple-iter.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/pypi-simple-iter.py/actions)

### Installation
```bash
$ [sudo] pip install pypi-simple-iter
```

#### Examples
```python
import pypi_simple_iter

for slug, name in pypi_simple_iter.iter_projects():
    print(slug,name)
```

iterate from file:
```python
import pypi_simple_iter
import requests

r = requests.get('https://pypi.org/simple/')
open('/tmp/simple.txt','w').write(r.text)
for slug, name in pypi_simple_iter.iter_projects_from_file('/tmp/simple.txt'):
    print(slug,name)
```

```
0 0
0-0 0-._.-._.-._.-._.-._.-._.-0
00000a 00000a
0-0-1 0.0.1
007 007
00print-lol 00print_lol
00smalinux 00SMALINUX
...
```

`startswith`
```python
for slug, name in pypi_simple_iter.iter_projects(startswith='Django'):
    print(slug,name)
```

```
django Django
django10-enumfield django10-enumfield
django1-11-zebra django1.11-zebra
...
```

#### Links
+   [Simple Index](https://pypi.org/simple/)
+   [Simple Project API](https://warehouse.pypa.io/api-reference/legacy/#simple-project-api)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
