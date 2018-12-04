from aiohttp import web
from config.settings import store


async def store_response():
    return web.json_response(data=store.tickets)


class LowerCostView(web.View):
    """View for provide the response and request for lower cost tickets."""
    async def get(self):
        """Represent the `get` method of view"""
        print('get request')
        return await store_response()


class LowerCostStatusView(web.View):

    async def get(self):
        statuses = {
            'today_updated': store.is_updated(),
            'update_status': store.update_status,
        }
        return web.json_response(statuses)
