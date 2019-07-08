from dynaconf import settings as dyn_settings
from split_settings.tools import optional, include

ENV = dyn_settings.get("DJANGO_ENV", "development")

base_settings = [
    "components/common.py",
    "components/db.py",
    "components/rest.py"
]

include(*base_settings)
