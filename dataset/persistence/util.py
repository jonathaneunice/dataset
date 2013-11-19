from datetime import datetime
from inspect import isgenerator

from sqlalchemy import Integer, UnicodeText, Float, DateTime, Boolean

def guess_type(sample):
    if isinstance(sample, bool):
        return Boolean
    elif isinstance(sample, int):
        return Integer
    elif isinstance(sample, float):
        return Float
    elif isinstance(sample, datetime):
        return DateTime
    return UnicodeText


class ResultIter(object):
    """ SQLAlchemy ResultProxies are not iterable to get a
    list of dictionaries. This is to wrap them. """

    def __init__(self, result_proxies, row_type=dict):
        if not isgenerator(result_proxies):
            result_proxies = iter((result_proxies, ))
        self.result_proxies = result_proxies
        self.row_type = row_type
        self.count = 0
        if not self._next_rp():
            raise StopIteration

    def _next_rp(self):
        try:
            self.rp = self.result_proxies.next()
            self.count += self.rp.rowcount
            self.keys = self.rp.keys()
            return True
        except StopIteration:
            return False

    def next(self):
        row = self.rp.fetchone()
        if row is None:
            if self._next_rp():
                return self.next()
            else:
                # stop here
                raise StopIteration
        return self.row_type(zip(self.keys, row))

    def __iter__(self):
        return self
