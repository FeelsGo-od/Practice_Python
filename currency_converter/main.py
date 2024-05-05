import logging
import os
import requests


api_key = 'your_api'
base_url = "https://api.freecurrencyapi.com/v1/latest"

# adding simple logging
log_file = os.path.join(os.path.dirname(__file__), 'currency_converter.log')
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_file,
    filemode='a'
)

class CurrencyNotFoundError(Exception):
    pass

class InvalidBaseCurrencyError(Exception):
    pass

class InvalidTargetCurrencyError(Exception):
    pass


def fetch_exchange_rates(base_currency="USD", currencies=None):
    """ Docstrings
    Fetches the latest exchange rates from the API.
    
    Args:
        base_currency (str): The base currency code (default is "USD")
        currencies (str): Comma-separated list of target currency codes (default is None).

    Returns:
        dict: A dictionary containing exchange rates for the specified currencies

    Raises:
        InvalidBaseCurrencyError: If the base currency code is invalid
        InvalidTargetCurrencyError: If any of the target currency codes are invalid.
        Exception: If any other error occurs.
    """
    try:
        params = {
            "apikey": api_key,
            "base_currency": base_currency,
            "currencies": currencies
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            exchange_rates = data['data']
            return exchange_rates
        elif response.status_code == 422:
            error_data = response.json()
            if "base_currency" in error_data.get('errors', {}):
                raise InvalidBaseCurrencyError("Invalid base currency code.")
            elif "currencies" in error_data.get('errors', {}):
                raise InvalidTargetCurrencyError("Invalid target currency code(s).")
        else:
            raise Exception(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise Exception(f'An error occured while fetching exchange rates: {e}')
    except Exception as e:
        raise Exception(f"An error occurred: {e}")


def convert_currency(amount, from_currency, to_currency):
    """
    Converts the specified amount from one currency to another.

    Args:
        amount (float): The amount to be converted.
        from_currency (str): The source currency code.
        to_currency (str): The target currency code(s)

    Returns:
        dict: A dictionary containing the converted amounts for each target currency

    Raises:
        CurrencyNotFoundError: If any of the target currency codes are not found in exchange rates.
        InvalidBaseCurrencyError: If the base currency code is invalid.
        InvalidTargetCurrencyError: If any of the target currency codes are invalid.
        Exception: If any other error occurs.
    """
    to_currencies = to_currency.split(',')
    
    converted_amounts = {}
    try:
        exchange_rates = fetch_exchange_rates(base_currency=from_currency, currencies=to_currency)
        
        if exchange_rates:
            for currency in to_currencies:
                if currency in to_currencies:
                    if isinstance(exchange_rates, dict):
                        if currency in exchange_rates:
                            conversion_rate = exchange_rates[currency]
                            converted_amount = amount * conversion_rate
                            converted_amounts[currency] = converted_amount
                        else:
                            raise CurrencyNotFoundError(f'Currency "{currency} not found in exchange rates."')
                    else:
                        logging.error(f'Currency "{currency}" not found in exchange rates.')
                        raise CurrencyNotFoundError(f'Currency "{currency}" not found in exchange rates.')
        return converted_amounts
    except Exception as e:
        raise Exception(f"An error occurred while converting currency: {e}")        

if __name__ == '__main__':
    while True:
        try:
            amount = float(input("Enter the amount you want to convert: "))
        except KeyboardInterrupt:
            print('\nExiting the program...')
            break
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        from_currency = input("Enter the source currency code (e.g., USD): ").upper()
        if len(from_currency) != 3 or not from_currency.isalpha():
            print("Please enter a valid 3-letter currency code.")
            continue

        to_currency = input("Enter the target currency code(s) (e.g., EUR or EUR,RUB,PLN): ").upper()
        if any(not currency.isalpha() or len(currency) != 3 for currency in to_currency.split(',')):
            print("Please enter a valid 3-letter currency codes.")
            continue

        try:
            converted_amount = convert_currency(amount, from_currency, to_currency)
            if converted_amount is not None:
                print(f'{amount} {from_currency} is equivalent to:')
                for currency, value in converted_amount.items():
                    print(f'{value:.2f} {currency}')
                break
        except (InvalidBaseCurrencyError, InvalidTargetCurrencyError, CurrencyNotFoundError) as e:
            print(e)
        except Exception as e:
            print(e)