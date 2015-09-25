import os
import json

try:
    import configparser
except ImportError:
    import ConfigParser as configparser


class EnvBackend(object):

    def load(self, key):
        return os.getenv(key)


class JsonFileBackend(object):

    def __init__(self, path):
        self._path = path

    def load(self, key):
        try:
            with open(self._path, 'r') as f:
                doc = json.load(f)

            return doc.get(key, None)
        except (IOError, ValueError):
            return None


class ConfigFileBackend(object):

    def __init__(self, path, section='credentials'):
        self._path = path
        self._section = section

    def load(self, key):
        try:
            config = configparser.ConfigParser()
            config.read(self._path)

            return config.get(self._section, key)

        except Exception:
            return None
