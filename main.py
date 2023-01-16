import pandas_datareader as pdr
from rich.table import Table
from rich import print

tickers = ['AMER3.SA', 'ABEV3.SA']
current_price = pdr.get_quote_yahoo(tickers)

table_acoes = Table("Acompanhamento de Ações")
table_acoes.add_column("AMER3", justify="center", style="cyan")
table_acoes.add_column("ABEV3", justify="center", style="cyan")

def fcurrent_price(tickers):
    current_price = pdr.get_quote_yahoo(tickers)["price"]
    return current_price


def regular_market_change(tickers):
    market_change = pdr.get_quote_yahoo(tickers)["regularMarketChange"]
    return market_change


def regular_market_high(tickers):
    market_high = pdr.get_quote_yahoo(tickers)["regularMarketDayHigh"]
    return market_high


def regular_market_low(tickers):
    market_low = pdr.get_quote_yahoo(tickers)["regularMarketDayLow"]
    return market_low


preco = fcurrent_price(tickers)
change = round(regular_market_change(tickers), 2)
high = regular_market_high(tickers)
low = regular_market_low(tickers)

table_acoes.add_row("Preço Atual (R$)", str(preco[0]), str(preco[1]))
table_acoes.add_row("Variação de Preço", str(change[0]), str(change[1]))
table_acoes.add_row("Maior Preço", str(high[0]), str(high[1]))
table_acoes.add_row("Menor Preço", str(low[0]), str(low[1]))

print(table_acoes)
