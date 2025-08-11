from typing import TypedDict, Union, Optional
from pathlib import Path


class TemplateOptions(TypedDict):
    context_processors: list[str]

class TemplateConfig(TypedDict):
    BACKEND: str
    DIRS: list[str]
    APP_DIRS: bool
    OPTIONS: TemplateOptions

class PasswordValidator(TypedDict):
    NAME: str

class DatabaseConfig(TypedDict):
    ENGINE: str
    NAME: Optional[Union[Path, str]]
    USER: Optional[str]
    PASSWORD: Optional[str]
    HOST: Optional[str]
    PORT: Optional[int]

class Databases(TypedDict):
    default: DatabaseConfig

