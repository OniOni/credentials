import os

from .base import Credentials
from .backends import EnvBackend, JsonFileBackend

backends = [EnvBackend(), JsonFileBackend(os.path.expanduser('~/.credentials.json'))]
credentials = Credentials(backends)
