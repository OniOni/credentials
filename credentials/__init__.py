from base import Credentials
from backends import EnvBackend

backends = [EnvBackend()]
credentials = Credentials(backends)
