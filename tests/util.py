from credentials import Credentials


class FakeBackend(object):

    def __init__(self, creds):
        self._creds = creds

    def load(self, key):
        return self._creds.get(key, None)


class BasePatchTest(object):

    def setUp(self):
        self.mock = self.patch.start()
        self.loader = Credentials([self.backend])

    def tearDown(self):
        self.patch.stop()
