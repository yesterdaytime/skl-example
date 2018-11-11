import decimal

class objectview(object):
    def __init__(self, d):
        self.__dict__ = d


def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError