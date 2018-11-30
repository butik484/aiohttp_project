from .views import LowerCostView


def lower_cost_routers(app):
    app.router.add_view('/lower', LowerCostView)
