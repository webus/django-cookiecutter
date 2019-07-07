import os
import dynaconf
from split_settings.tools import optional, include

ENV = os.getenv("DJANGO_ENV", "development")

base_settings = [
    "components/common.py"
]

include(*base_settings)
