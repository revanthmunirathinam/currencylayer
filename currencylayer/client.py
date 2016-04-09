import datetime
import requests


class Client(object):
    """ Client implementation for currencylayer
    """
    base_url = 'http://apilayer.net/api/'
    endpoint_live = base_url + 'live'
    endpoint_historical = base_url + 'historical'
    endpoint_convert = base_url + 'convert'
    endpoint_time_frame = base_url + 'timeframe'
    endpoint_change = base_url + 'change'
    endpoint_currencies = base_url + 'list'

    def __init__(self, access_key):
        self.client = requests.Session()
        self.client.params.update({'access_key': access_key})

    def currencies(self):
        response = self.client.get(self.endpoint_currencies)
        return response.json()

    def live_rates(self, base_currency='USD'):
        if isinstance(base_currency, list):
            base_currency = ','.join(base_currency)
        response = self.client.get(self.endpoint_live, params={'source': base_currency})
        return response.json()

    def live_rates_for(self, currencies, base_currency='USD'):
        currencies = ','.join(currencies)
        response = self.client.get(self.endpoint_live, params={'currencies': currencies, 'source': base_currency})
        return response.json()

    def historical(self, date=datetime.date.today(), base_currency='USD'):
        response = self.client.get(self.endpoint_historical, params={'date': date, 'source': base_currency})
        return response.json()

    def convert(self, from_currency, to_currency, amount, date=datetime.date.today()):
        response = self.client.get(self.endpoint_convert,
                                   params={'from': from_currency, 'to': to_currency, 'amount': amount, 'date': date})
        return response.json()

    def timeframe(self, start_date, end_date, currencies, base_currency='USD'):
        if isinstance(currencies, list):
            currencies = ','.join(currencies)
        response = self.client.get(self.endpoint_time_frame,
                                   params={'currencies': currencies, 'start_date': start_date, 'end_date': end_date,
                                           'source': base_currency})
        return response.json()
