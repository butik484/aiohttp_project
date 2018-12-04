from .views import LowerCostView, LowerCostStatusView


def lower_cost_routers(app):
    app.router.add_view('/lower', LowerCostView)
    app.router.add_view('/status', LowerCostStatusView)
