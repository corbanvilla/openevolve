from __future__ import annotations

from os import PathLike


class DatabaseConfig:
    db_path: str
    ...


class OpenEvolveConfig:
    database: DatabaseConfig
    ...


class Config(OpenEvolveConfig):
    ...


def load_config(path: str | PathLike[str] | None = ...) -> OpenEvolveConfig: ...
