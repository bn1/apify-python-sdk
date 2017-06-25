import requests


URL_BASE = 'https://api.apifier.com/v2'


class KeyValueStore(object):
    def __init__(self, store_id):
        self.store_id = store_id
        self.page = 0

        self.buffer = []

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if not len(self.buffer):
            self._get_next_page()
        return self.buffer.pop(0)

    def _get_next_page(self):
        self.page += 1

        url = '%(URL_BASE)s/key-value-stores/%(store_id)s/records/PAGES-%(page)09d?raw=1' % {
            'URL_BASE': URL_BASE,
            'store_id': self.store_id,
            'page': self.page
        }
        response = requests.get(url)
        items = response.json()
        if type(items) is list:
            self.buffer = items
        else:
            raise StopIteration
