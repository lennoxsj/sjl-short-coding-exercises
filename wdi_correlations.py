"""Compare World Development Indicators between the US and the UN's
aggregate of Least Developed Countries (LDCs).

Reads two CSV exports from the World Bank's WDI database, computes
year-over-year differences between the US and LDC values, then reports
correlations between life-expectancy gaps and a few other indicators
and plots the life-expectancy gap over time.
"""

import pandas as pd
import matplotlib.pyplot as plt


US_CSV = "US World Development Indicators.csv"
LDC_CSV = "LDC World Development Indicators.csv"


def read_wdi_csv(path):
    return pd.read_csv(
        path,
        sep=",",
        header=0,
        na_values=["NA", "", ".."],
        encoding="utf-8",
    )


def df_difference(df1, df2):
    if df1.shape != df2.shape:
        raise ValueError("dataframes have different shapes")
    if not df1.columns.equals(df2.columns):
        raise ValueError("dataframes have different columns")
    if not df1.index.equals(df2.index):
        raise ValueError("dataframes have different indexes")

    return df1 - df2


if __name__ == "__main__":
    df_us = read_wdi_csv(US_CSV)
    df_ldc = read_wdi_csv(LDC_CSV)
    df_diff = df_difference(df_us, df_ldc)

    life_exp = "Life expectancy at birth, total (years)"
    pairs = [
        ("Access to electricity (% of population)", "access to electricity"),
        ("Compulsory education, duration (years)", "years of compulsory education"),
        ("Aquaculture production (metric tons)", "aquaculture production (metric tons)"),
    ]

    print("Correlation between the US-vs-LDC gap in life expectancy and the gap in...")
    for column, label in pairs:
        corr = df_diff[life_exp].corr(df_diff[column])
        print(f"  {label}: {round(corr, 4)}")

    plt.figure(figsize=(10, 5))
    plt.plot(
        df_us["Year"],
        df_diff[life_exp],
        marker="*",
        linestyle="-",
        color="g",
        linewidth=3,
        markersize=5,
    )
    plt.title("Life expectancy at birth — gap between the US and Least Developed Countries")
    plt.xlabel("Year")
    plt.ylabel("Difference in life expectancy at birth (years)")
    plt.grid(True, linestyle="--", alpha=0.25)
    plt.tight_layout()
    plt.show()
