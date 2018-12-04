import asyncio
from aiohttp import web
from config.urls import config_routers
from libs.tickets import request_prepare_data
from libs.helpers import create_keys
from config.settings import store


async def schedule_request():
    if not store.is_updated():
        key = next(create_keys())
        if not store.store_updated(key):
            func_lict = []
            for keys in create_keys():
                # prepare pool of request functions
                func_lict.append(request_prepare_data(keys))
            # await the requests
            await asyncio.gather(*func_lict)


async def constant_update(loop):
    while True:
        print('Schedule infinity loop')
        await schedule_request()
        await asyncio.sleep(10, loop=loop)


loop = asyncio.get_event_loop()
app = web.Application(loop=loop)

config_routers(app)

# adding the scheduler into loop
asyncio.ensure_future(constant_update(loop=loop))

web.run_app(app)



