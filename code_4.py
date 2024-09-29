import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
    year_price = df[(df['iso_a3'] == country_code.upper()) & (df['date'].str[:4] == str(year))]
    mean_by_year = round(float(year_price['dollar_price'].mean()), 2)

    return mean_by_year


def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    country_price = df[(df['iso_a3'] == country_code.upper())]
    mean_by_country = round(float(country_price['dollar_price'].mean()), 2)

    return mean_by_country


def get_the_cheapest_big_mac_price_by_year(year):
    pass # Min


def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Max

if __name__ == "__main__":
    mean_by_year = get_big_mac_price_by_year(2010,'arg')
    print(mean_by_year)

    mean_by_country = get_big_mac_price_by_country('mex')
    print(mean_by_country)

