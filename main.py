import asyncio
from aiohttp import web
from config.urls import config_routers


async def schedule_request():
    print('Additional function update')


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



