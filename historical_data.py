import yfinance as yf

def fetch_symbol(symbol):
    data = yf.download(symbol, period="max", auto_adjust=True)
    print(data.iloc[0]['Date'])


fetch_symbol('AAPL')

