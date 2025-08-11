from os import getenv
from typing import Optional

def get_secret(secret_id: str, backup: Optional[str] = None) -> Optional[str]:
    return getenv(secret_id, backup)

pipeline = get_secret("PIPELINE", "")

if pipeline == "production":
    from .production import *
elif pipeline == "test":
    from .test import *
else:
    from .dev import *
