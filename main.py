import asyncio
import uvloop
from asyncio import TimerHandle
from aiohttp import web
import aiojobs

from config.urls import config_routers

from libs.tickets import request_prepare_data
from libs.helpers import create_keys

from config.settings import store


async def schedule_request():
    if not store.is_updated():
        key = next(create_keys())
        if not store.store_updated(key):
            request_workers = []
            for keys in create_keys():
                # prepare pool of request functions
                if not store.is_ticket_updated(key=keys):
                    print(f'Ticket for {keys} should be updated')
                    request_workers.append(request_prepare_data(keys))
            # await the requests
            await asyncio.gather(*request_workers)


async def constant_update(loop):
    # scheduler = await aiojobs.create_scheduler()
    # await scheduler.spawn(schedule_request())
    print('Schedule infinity loop!!!', loop.time())
    # while True:
    #     print('Schedule infinity loop')
    await schedule_request()
    delay = loop.time() + 40
    print(delay)
    loop.call_at(delay, t, loop)
    #await asyncio.sleep(10, loop=loop)


def t(loop):
    print('sadad')
    a = asyncio.ensure_future(constant_update(loop=loop))
    print('sadad', a)


async def scheduler(loop):
    delay = loop.time() + 10
    print(delay)
    res = loop.call_at(delay, t, loop)
    print(res)


loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)

app = web.Application(loop=loop)


config_routers(app)

# adding the scheduler into loop
asyncio.ensure_future(scheduler(loop=loop))

web.run_app(app)



