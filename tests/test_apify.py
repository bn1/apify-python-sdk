import os
import pytest

from httmock import HTTMock, all_requests
from apify import KeyValueStore


@all_requests
def mock_page_store(url, request):
    path = (os.path.dirname(os.path.realpath(__file__)) +
            "/data" + url.path + '.json')
    with open(path, "r") as fo:
        return fo.read()


def test_init():
    store = KeyValueStore('dummy-store')
    assert isinstance(store, KeyValueStore)
    assert store.page == 0


def test_can_iterate():
    with HTTMock(mock_page_store):
        store = KeyValueStore('dummy-store')
        got_item = False
        for item in store:
            got_item = True
            break

        assert got_item
        assert store.page == 1


def test_stops_iteration():
    with HTTMock(mock_page_store):
        with pytest.raises(StopIteration):
            store = KeyValueStore('dummy-store')
            while True:
                store.next()


def test_iterating_over_all_pages():
    with HTTMock(mock_page_store):
        store = KeyValueStore('dummy-store')
        items = []
        for item in store:
            items.append(item)

        assert store.page == 4
        assert len(items) == 8


if __name__ == '__main__':
    pytest.main()