import unittest

import mock

import credentials


class FakeBackend(object):

    def __init__(self, creds):
        self._creds = creds

    def load(self, key):
        return self._creds.get(key, None)


class TestCredentials(unittest.TestCase):

    def setUp(self):
        self._cred_dict = {
            'lol': 42
        }
        self.loader = credentials.Credentials([FakeBackend(self._cred_dict)])

    def test_require(self):
        creds = self.loader.require(['lol'])

        self.assertTrue(getattr(creds, 'lol', False), 'Creds should contain "lol"')
        self.assertEqual(creds.lol, 42)

    def test_require_missing_key(self):
        try:
            creds = self.loader.require(['lol', 'missing'])
        except KeyError:
            pass
        else:
            assert False, "Key was missing KeyError should have been thrown."

    def test_load(self):
        cred = self.loader.load('lol')

        self.assertEqual(cred, 42)

    def test_load_missing_key(self):
        try:
            cred = self.loader.load('missing')
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


class BasePatchTest(object):

    def setUp(self):
        self.mock = self.patch.start()
        self.loader = credentials.Credentials([self.backend])

    def tearDown(self):
        self.patch.stop()


class TestEnvBackend(BasePatchTest, unittest.TestCase):

    def setUp(self):
        self.backend = credentials.EnvBackend()
        self.patch = mock.patch('os.getenv', auto_spec=True)
        super(TestEnvBackend, self).setUp()

    def test_simple(self):
        self.backend.load('key')
        self.mock.assert_called_with('key')

    def test_e2e(self):
        self.loader.load('key')
        self.mock.assert_called_with('key')


if __name__ == "__main__":
    unittest.main()
