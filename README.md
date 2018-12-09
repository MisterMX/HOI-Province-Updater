# Project info

Simple python script for Hearts of Iron Darkest Hour that updates the province IDs in `input/revolt_new.txt` by using `input/province_names_new.csv` and `input/province_names_old.csv` and writes it into `output/revolt_updated.txt`.

# How to run the script

1. Install Python 3 in your preferred way.
2. Run `main.py`

# Notes

The revolt file parser will remove all comments (startint with `#`) when reading and thus the output file might loose meta information.
