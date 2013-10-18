# -*- coding:utf8 -*-
import requests
from nose import run
from nose.tools import assert_equal


def test_helloworld():
    r = requests.get('http://127.0.0.1:8888')
    print r.text
    assert_equal(r.text, 'Hello, world')


if __name__ == '__main__':
    run(defaultTest=__name__)
