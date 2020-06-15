import pypi_simple_iter

for slug, name in pypi_simple_iter.iter_projects(startswith='Django'):
    print(slug,name)
