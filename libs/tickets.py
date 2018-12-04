import aiohttp
import asyncio
from .constants import AUTHORIZATION, URL_SEARCH, RESPONSE_URL


def minimal_price(item):
    """Helper function for `key` to min function
    Example:
        min(tickets, key=minimal_price)
    Args:
        item(dict): Item of data with ticket
    Returns:
        value of amount from incoming `item` used for `min` function
    """
    price = item.get('price')
    if price:
        return price.get('amount')


async def request_data(session, request_id):
    """Function for request of data from endpoint
    Args:
        session(aiohttp.ClientSession): Session for getting information from
                                    endpoint
        request_id(str): String with ID of request.
    Returns:
        dict with response of data(dict)
    """
    async with session.get(
        url=f'{RESPONSE_URL}/{request_id}',
        headers=AUTHORIZATION,
    ) as resp:
        # let's wait the data preparing
        await asyncio.sleep(1)
        try:
            response = await resp.json()
            status = response.get('status')
            if status == 'done':
                return response
            return await request_data(session=session, request_id=request_id)

        except aiohttp.client_exceptions.ContentTypeError as error:
            print(f'need to be logged : {error}')
            # for avoid the wrong response `response.json() incorrectly
            # assumes some json responses are text` run the request again.
            return await request_data(session=session, request_id=request_id)


async def request_prepare_data(query):
    """Function for request the prepare of data from endpoint
    Args:
        query(str): Query string with combined of direct and date example
                `ALA-CIT201901121000E`
    Returns:
        lower of cost
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=URL_SEARCH,
            headers=AUTHORIZATION,
            json={'query': query}
        ) as resp:
            print(resp.status)
            try:
                response = await resp.json()
                request_id = response.get('id')
                done_data = await request_data(
                    session=session, request_id=request_id
                )
                return done_data
            except aiohttp.client_exceptions.ContentTypeError as error:
                print(f'need to be logged : {error}')
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(request_prepare_data())
# loop.close()
#
# """
# for x in direct:
#     for date in dates:
#         run request
# """
