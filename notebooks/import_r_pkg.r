if (!require("pacman", character.only = TRUE)) {
    install.packages("pacman", repos = "https://cloud.r-project.org")
}
library(pacman)
pacman::p_load("fpp2", "fpp3", "dplyr", "tidyverse", "ggplot2")