import unittest

import mock
from credentials import EnvBackend

from .util import BasePatchTest


class TestPatchedEnvBackend(BasePatchTest, unittest.TestCase):

    def setUp(self):
        self.backend = EnvBackend()
        self.patch = mock.patch('os.getenv', auto_spec=True)
        super(TestPatchedEnvBackend, self).setUp()

    def test_simple(self):
        self.backend.load('key')
        self.mock.assert_called_with('key')

    def test_e2e(self):
        self.loader.load('key')
        self.mock.assert_called_with('key')


class TestEnvBackend(unittest.TestCase):

    def setUp(self):
        self.backend = EnvBackend()

    def test_missing_key_returns_none(self):
        cred = self.backend.load('this_key_should_not_be_in_any_env_42')
        self.assertEqual(cred, None)
