import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
    year_price_df = df[(df['iso_a3'] == country_code.upper()) & (df['date'].str[:4] == str(year))]
    mean_by_year = round(float(year_price_df['dollar_price'].mean()), 2)

    return mean_by_year

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    country_price_df = df[(df['iso_a3'] == country_code.upper())]
    mean_by_country = round(float(country_price_df['dollar_price'].mean()), 2)

    return mean_by_country

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    min_df = df[(df['date'].str[:4] == str(year))]
    min_value_index = min_df['dollar_price'].idxmin()
    min_row = df.loc[min_value_index]
    cheapest = f"{min_row['name']}({min_row['iso_a3']}): ${round(min_row['dollar_price'], 2)}"

    return cheapest

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    max_df = df[(df['date'].str[:4] == str(year))]
    max_value_index = max_df['dollar_price'].idxmax()
    max_row = df.loc[max_value_index]
    expensive = f"{max_row['name']}({max_row['iso_a3']}): ${round(max_row['dollar_price'], 2)}"

    return expensive

if __name__ == "__main__":
    mean_by_year = get_big_mac_price_by_year(2010,'arg')
    print(mean_by_year)

    mean_by_country = get_big_mac_price_by_country('mex')
    print(mean_by_country)

    min_value = get_the_cheapest_big_mac_price_by_year(2008)
    print(min_value)

    max_value = get_the_most_expensive_big_mac_price_by_year(2014)
    print(max_value)

