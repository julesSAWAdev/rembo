# dagster_orchestration/dagster_orchestration/__init__.py

from dagster import Definitions, load_assets_from_modules

from .assets import resources

defs = Definitions(assets=load_assets_from_modules(
    [assets]), resources=resources)