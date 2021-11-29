import yfinance as yf
import json

msft = yf.Ticker("MSFT")
print(json.dumps(msft.info))
