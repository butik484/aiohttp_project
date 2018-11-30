from aiohttp import web


async def store_response(data):
    aa = {'some1': 'data1'}
    data.update(aa)
    return web.json_response(data=data)


class LowerCostView(web.View):
    """View for provide the response and request for lower cost tickets."""
    async def get(self):
        """Represent the `get` method of view"""
        print('get request')
        data = {'example': 'data'}
        return await store_response(data=data)
