options(repr.matrix.max.rows = 10, repr.matrix.max.cols = 6)
options(width = 120)
options(jupyter.plot_mimetypes = c("image/svg+xml", "image/png"))

if (!require("pacman", character.only = TRUE)) {
  install.packages("pacman", repos = "https://cloud.r-project.org")
}
library(pacman)

pacman::p_load(
  fpp2,
  fpp3,
  dplyr,
  tidyverse,
  ggplot2,
  readxl,
  purrr,
  readr,
  here,
  xts,
  lubridate,
  tsibble,
  forecast,
  feasts,
  skimr,
  patchwork,
  ggtime
)