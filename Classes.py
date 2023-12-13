import requests
import json
from Configuration import keys

class ProgramExceptions(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
             raise ProgramExceptions(f'Repeated arguments {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ProgramExceptions(f'Cannot process {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ProgramExceptions(f'Cannot process {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ProgramExceptions(f'Cannot process {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base * amount
