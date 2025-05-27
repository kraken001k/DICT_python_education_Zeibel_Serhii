from json import JSONDecodeError
import requests

# Infinite loop of requesting base currency until we get the correct code.
while True:
    base_currency = input('Enter your base currency code (eg usd, eur, uah):\n> ').lower()
    url = f"http://www.floatrates.com/daily/{base_currency}.json"
    try:
        response = requests.get(url)
        rates = response.json()
        if not rates:
            print('Currency not found. Please retry.')
            continue
        break  # Currency found - exit the loop.
    except JSONDecodeError:
        print('Incorrect currency code. Please re-enter.')

# Exchange rate cache - pre-add usd and eur if available.
cache = {}
for code in ['usd', 'eur']:
    if code in rates:
        cache[code] = rates[code]

# Currency exchange cycle
while True:
    target_currency = input('\nEnter the target currency (or Enter to exit):\n> ').lower()
    if not target_currency:
        break  # User wants to log out

    try:
        amount = float(input('Enter the amount to exchange:\n> '))
    except ValueError:
        print('Invalid amount format. Please enter a number.')
        continue

    print('Checking cache...')
    if target_currency in cache:
        print('Course found in cache.')
        rate = cache[target_currency]['rate']
    else:
        print('The course is not in the cache, loading...')
        if target_currency in rates:
            cache[target_currency] = rates[target_currency]  # Add to cache
            rate = rates[target_currency]['rate']
        else:
            print('This currency was not found in the database.')
            continue

    # Calculating the exchange result
    exchanged = round(amount * rate, 2)
    print(f'You will receive {exchanged} {target_currency.upper()} at the rate {rate:.4f}')
