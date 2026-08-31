from functools import reduce

import pandas as pd
import typer

app = typer.Typer()

def csvs_to_dfs(folder_path):
    csv_files = [str(file) for file in folder_path.iterdir() if file.is_file()and file.suffix.lower() == '.csv']
    dfs = [pd.read_csv(file) for file in csv_files]
    return dfs

def merge_data(dfs, merge_column):
    merged_df = reduce(
        lambda left, right: pd.merge(left, right, on=merge_column, how="outer"), dfs
        )
    return merged_df

@app.command()
def main(input_path, output_path, merge_column):
    dfs = csvs_to_dfs(input_path)
    merged_df = merge_data(dfs, merge_column)
    merged_df.to_csv(output_path)

if __name__ == "__main__":
    app()