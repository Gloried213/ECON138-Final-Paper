from pathlib import Path

from dotenv import load_dotenv
from loguru import logger

# Load environment variables from .env file if it exists
load_dotenv()

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

REFERENCES_DIR = PROJ_ROOT / "references"

SAMPLE_DATA_DIR = REFERENCES_DIR / "sample_data"
RAW_SAMPLE_DATA_SOURCE_DIR = SAMPLE_DATA_DIR / "raw_data_source"
FRED_SAMPLE_DATA_DIR = RAW_SAMPLE_DATA_SOURCE_DIR / "fred"

CLEANED_SAMPLE_DATA_DIR = SAMPLE_DATA_DIR / "cleaned"
MODELS_SAMPLE_DATA_DIR = SAMPLE_DATA_DIR / "models"

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

MODELS_DIR = PROJ_ROOT / "models"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# If tqdm is installed, configure loguru with tqdm.write
# https://github.com/Delgan/loguru/issues/135
try:
    from tqdm import tqdm

    logger.remove(0)
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
except ModuleNotFoundError:
    pass
