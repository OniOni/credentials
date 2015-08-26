import os


class EnvBackend(object):

    def load(self, key):
        return os.getenv(key)
