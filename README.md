# Apify

<!--[![Build Status](https://travis-ci.org/luxcem/apifier.svg?branch=master)](https://travis-ci.org/luxcem/apifier) [![codecov](https://codecov.io/gh/luxcem/apifier/branch/master/graph/badge.svg)](https://codecov.io/gh/luxcem/apifier) [![PyPI version](https://badge.fury.io/py/apifier.svg)](https://badge.fury.io/py/apifier)
-->


Apify is package with Python bindings for [apifier.com](https://apifier.com/) - a plaftorm for creating web crawlers.

## Install

Apify is available for python 2.7 and above

```
pip install apify
```

## Examples

Getting all stored records from `dummy-store`:

```python
from apify import KeyValueStore


store = KeyValueStore('dummy-store')

for record in store:
    print record
```


Getting only record pages `100, 101, ..., 198, 199` from `dummy-store`:

```python
from apify import KeyValueStore


store = KeyValueStore('dummy-store')
store.page = 99  # starts with fetching the next (100th) page

for record in store:
    if store.page == 200:
        break
		
    print record

```


## Contribute

1. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
2. Fork the [repository](https://github.com/bn1/python-apify) on GitHub to start making your changes to the **master** branch (or branch off of it).
3. Write a test which shows that the bug was fixed or that the feature works as expected.
4. Send a pull request and bug the maintainer until it gets merged and published. :)

<!-- Make sure to add yourself to AUTHORS.-->