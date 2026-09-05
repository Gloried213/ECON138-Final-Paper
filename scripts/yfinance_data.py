import pandas as pd
import typer
import yfinance as yf

from src.config import CLEANED_SAMPLE_DATA_DIR

app = typer.Typer()

def get_stock(ticker, start_date: str, end_date: str, merge_column)-> pd.DataFrame:
    stock_history = yf.Ticker(ticker).history(start=start_date, end=end_date, interval = '1mo')
    stock_history['Ticker'] = ticker
    stock_history = stock_history.reset_index(names=merge_column)
    stock_history[merge_column] = stock_history[merge_column].dt.strftime("%Y-%m-%d")
    return stock_history

def get_stocks(tickers, start_date, end_date, merge_column):
    stock_data_list = []
    for ticker in tickers:
        stock_data = get_stock(ticker, start_date, end_date, merge_column)
        stock_data_list.append(stock_data)
    all_stock_data = pd.concat(stock_data_list, ignore_index=True)
    return all_stock_data

@app.command()
def main(tickers = "AAPL", 
         start_date = "2021-01-01",
         end_date = "2026-08-30",
         output_path = CLEANED_SAMPLE_DATA_DIR/ "stock.csv", 
         merge_column = 'Date'):
    stock_data = get_stocks(tickers, start_date, end_date, merge_column)
    stock_data.to_csv(output_path)

if __name__ == "__main__":
    app()