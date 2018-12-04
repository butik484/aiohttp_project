from datetime import datetime, timedelta
from .constants import DIRECTIONS


def get_query_date():
    """ Generator creating date for query

    Returns:
        date(str): Returned the string with date in next format 'YYYYmd'
                example `20181230`
    """
    request_date = datetime.now()
    end_request_date = request_date + timedelta(days=30)
    while request_date < end_request_date:
        yield request_date.strftime('%Y%m%d')
        request_date += timedelta(days=1)


def create_keys():
    """Helper generator for creating the string key for items, example
    `ALA-CIT20190112`

    Yields:
        key for item(str): Example `ALA-CIT20181230`
    """
    for direction in DIRECTIONS:
        for date in get_query_date():
            yield f'{direction}{date}'
