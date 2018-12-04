from .helpers import create_keys


class Store(object):
    """This class implements simple dict storage for candles
    """
    def __init__(self):
        self.tickets = {}
        self.update_status = {}

    def is_reload(self, key):
        return self.update_status.get(key)

    def prepare_reload(self):
        for key in create_keys():
            self.update_status[key] = False

    def get_or_create(self, key, value):
        ticket = self.tickets.get(key)
        if ticket:
            return False, ticket
        self.tickets[key] = value
        return True, value

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.tickets.values()}'


class Ticket(object):
    """Current ticket"""
    def __init__(self, cost, departure, direction):
        self.cost = cost
        self.departure = departure
        self.direction = direction

    def is_updated(self):
        """Check updated the ticket"""
        return 'status'
