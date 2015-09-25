import unittest

import mock
from credentials import JsonFileBackend

from .util import BasePatchTest


class BasePatchedJsonFileBackend(BasePatchTest):

    def setUp(self):
        self.open = mock.mock_open(
            read_data=self.read_data
        )
        self.patch = mock.patch('credentials.backends.open',
                                self.open, create=True)
        self.backend = JsonFileBackend('ignore')
        super(BasePatchedJsonFileBackend, self).setUp()


class GoodPatchedJFBackend(BasePatchedJsonFileBackend, unittest.TestCase):

    def setUp(self):
        self.read_data = '{"key":42}'
        super(GoodPatchedJFBackend, self).setUp()

    def test_simple(self):
        cred = self.backend.load('key')
        self.assertEqual(cred, 42)

    def test_e2e(self):
        cred = self.loader.load('key')
        self.assertEqual(cred, 42)

    def test_missing_key_returns_none(self):
        cred = self.backend.load('not_a_key')
        self.assertEqual(cred, None)


class BadPatchedJFBackend(BasePatchedJsonFileBackend, unittest.TestCase):

    def setUp(self):
        self.read_data = 'Not valid json'
        super(BadPatchedJFBackend, self).setUp()

    def test_malformed_json_file(self):
        cred = self.backend.load('key')
        self.assertEqual(cred, None)


class TestJsonFileBackend(unittest.TestCase):

    def setUp(self):
        self.backend = JsonFileBackend('absent')

    def test_absent_json_file(self):
        cred = self.backend.load('key')
        self.assertEqual(cred, None)
