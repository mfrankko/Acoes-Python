import pandas_datareader as pdr
from rich.table import Table
from rich import print

tickers = ['AMER3.SA', 'ABEV3.SA']
current_price = pdr.get_quote_yahoo(tickers)

table_acoes = Table("Acompanhamento de Ações")
table_acoes.add_column("AMER3", justify="center", style="cyan")
table_acoes.add_column("ABEV3", justify="center", style="cyan")


def return_quotes(tickers_info, index):
    return pdr.get_quote_yahoo(tickers_info)[index]


preco = return_quotes(tickers, "price")
change = round(return_quotes(tickers, "regularMarketChange"), 2)
high = return_quotes(tickers, "regularMarketDayHigh")
low = return_quotes(tickers, "regularMarketDayLow")

table_acoes.add_row("Preço Atual (R$)", str(preco[0]), str(preco[1]))
table_acoes.add_row("Variação de Preço", str(change[0]), str(change[1]))
table_acoes.add_row("Maior Preço", str(high[0]), str(high[1]))
table_acoes.add_row("Menor Preço", str(low[0]), str(low[1]))

print(table_acoes)
