import requests
import json
import sys

def can_be_float(amount):
    try:
        float(amount)
        return True
    except ValueError:
        sys.exit("command-line arhument is not a number")


try:
    if len(sys.argv)==1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv)==2:
        amount = sys.argv[1]
        can_be_float(amount)
        response=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        o= response.json()
        rate = o['bpi']['USD']['rate_float']
        final=float(amount)*rate
        print(f"${final:,.4f}")


except requests.RequestException:
    sys.exit("Error fetching data from the API")




