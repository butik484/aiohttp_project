""" This module used for registration of routes all the applications.

Example:
    `apps.example_app.urls` contain the function for registration routes of
     self application, and received initialized `aiohttp` application in local
    routes registration function.

    All calls `routes` functions placed into `config.urls` and in `main`
    module just one call initialized all routes.
"""

from apps.lower_cost.urls import lower_cost_routers


def config_routers(app):
    """Consolidated initialize routes."""
    lower_cost_routers(app)
