import unittest

from credentials import Credentials

from .util import FakeBackend


class TestCredentials(unittest.TestCase):

    def setUp(self):
        self._cred_dict = {
            'lol': 42
        }
        self.loader = Credentials([FakeBackend(self._cred_dict)])

    def test_require(self):
        creds = self.loader.require(['lol'])

        self.assertTrue(getattr(creds, 'lol', False),
                        'Creds should contain "lol"')
        self.assertEqual(creds.lol, 42)

    def test_require_missing_key(self):
        try:
            self.loader.require(['lol', 'missing'])
        except KeyError:
            pass
        else:
            assert False, "Key was missing KeyError should have been thrown."

    def test_load(self):
        cred = self.loader.load('lol')

        self.assertEqual(cred, 42)

    def test_load_missing_key(self):
        try:
            self.loader.load('missing')
        except KeyError:
            pass
        else:
            assert False, "Key was missing KeyError should have been thrown."

    def test_add_backend(self):
        other_fake_backend = FakeBackend({'lol2': '43'})
        self.loader.add_backend(other_fake_backend)

        self.assertEqual(len(self.loader._backends), 2)

    def test_multiple_backends(self):
        other_fake_backend = FakeBackend({'lol2': 43})
        self.loader.add_backend(other_fake_backend)

        cred = self.loader.load('lol2')
        self.assertEqual(cred, 43)

    def test_key_in_muliple_backends(self):
        other_fake_backend = FakeBackend({'lol': 43})
        self.loader.add_backend(other_fake_backend)

        cred = self.loader.load('lol')
        self.assertEqual(cred, 42)
