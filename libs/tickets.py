import aiohttp
import asyncio
from .constants import AUTHORIZATION, URL_SEARCH, RESPONSE_URL
from config.settings import store


def get_amount(item):
    """Helper function for `key` to min function
    Example:
        min(tickets, key=get_amount)
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
            print(
                f'Status of prepare of data: {status} for id: {request_id}'
            )
            if status == 'done':
                return response
            return await request_data(session=session, request_id=request_id)

        except aiohttp.client_exceptions.ContentTypeError as error:
            print(f'need to be logged : {error}')
            # for avoid the wrong response `response.json() incorrectly
            # assumes some json responses are text` run the request again.
            return await request_data(session=session, request_id=request_id)


async def request_prepare_data(key):
    """Function for request the prepare of data from endpoint
    Args:
        key(str): Query string with combined of direct and date example
                `ALA-CIT20190112`
    Returns:
        lower of cost
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=URL_SEARCH,
            headers=AUTHORIZATION,
            json={'query': f'{key}1000E'}
        ) as resp:
            print(
                f'{resp.status} for key {key} and status is '
                f'{store.is_ticket_updated(key)}'
            )
            try:
                response = await resp.json()
                request_id = response.get('id')
                done_data = await request_data(
                    session=session, request_id=request_id
                )
                # get lower of cost ticket from returned data set
                if done_data.get('items'):
                    lowest_cost_ticket = min(
                        done_data['items'], key=get_amount
                    )
                    # store the data into base
                    store.get_or_create(key=key, value=lowest_cost_ticket)

                return done_data
            except aiohttp.client_exceptions.ContentTypeError as error:
                print(f'need to be logged : {error}')
