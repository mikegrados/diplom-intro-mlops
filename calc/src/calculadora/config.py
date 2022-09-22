
from dynaconf import Dynaconf, Validator
import os
settings = Dynaconf(
    validators=[Validator('NUMBER', 'NAME', must_exist=True)],
    envvar_prefix="DYNACONF",
    root_path=os.path.dirname(__file__),
    settings_files=['settings.toml', '.secrets.toml'],
    environment=True,
    load_dotenv=True,
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
