from .helpers import create_keys


class Store(object):
    """This class implements simple dict storage for tickets"""

    def __init__(self):
        self.tickets = {}
        self.update_status = {}
        self.today_updated = False

    def _prepare_reload(self):
        """Prepare to reload of date for `today` data"""
        for key in create_keys():
            self.update_status[key] = False

    def store_updated(self, key):

        if not self.update_status.get(key):
            # creat keys
            self.today_updated = False
            self._prepare_reload()
            return False

        if all([value for key, value in self.update_status.items()]):
            self.today_updated = True
            return True

    def is_updated(self):
        return self.today_updated

    def is_ticket_updated(self, key):
        return self.update_status.get(key, False)

    def _update_status(self, key):
        value = self.update_status.get(key)
        print(f'Logging {value}')
        if not value:
            # raise exception ?
            self.update_status[key] = True
            print('updated', self.update_status[key])

    def get_or_create(self, key, value):
        ticket = self.tickets.get(key)
        if ticket:
            return False, ticket
        self.tickets[key] = value
        self._update_status(key)
        return True, value

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.tickets.values()}'
