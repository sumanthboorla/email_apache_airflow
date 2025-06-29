# country data which start with I letter
import pandas as pd

def filter_function():
    print("Applying filter which starts with countries with I")
    df = pd.read_csv("~/ip_files/countries_clean.csv")
    df = df[df['country'].str.startswith("I")]
    df.to_csv("~/op_files/countries_filtered.csv")

    