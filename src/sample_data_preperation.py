from pathlib import Path

from loguru import logger
from scripts import csv_handler, yfinance_data
import typer

from src.config import CLEANED_SAMPLE_DATA_DIR, FRED_SAMPLE_DATA_DIR, MODELS_SAMPLE_DATA_DIR

app = typer.Typer()

@app.command()
def main(
    merge_column = "observation_date",
    fred: Path = FRED_SAMPLE_DATA_DIR,
    fred_out: Path = CLEANED_SAMPLE_DATA_DIR/ "fred.csv",
    model_in: Path = CLEANED_SAMPLE_DATA_DIR,
    model_out: Path = MODELS_SAMPLE_DATA_DIR/ "MODEL.csv"
):
    logger.info("Processing fred dataset...")
    csv_handler.main(input_path=fred,
                     output_path= fred_out, merge_column=merge_column)
    
    logger.info("Processing yfinance dataset...")
    yfinance_data.main(tickers= ["VDE","^VIX"],
                       merge_column= merge_column)
    
    logger.info("Processing model dataset...")
    csv_handler.main(input_path=model_in,
                     output_path=model_out,
                     merge_column=merge_column)
    
    logger.success("Processing dataset complete.")

if __name__ == "__main__":
    app()
