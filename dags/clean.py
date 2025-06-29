import pandas as pd
import datetime

def pre_process():
    print("Before adding data column")
    df = pd.read_csv("~/ip_files/countries.csv")
    df['process_date'] = datetime.date.today()
    df = df.fillna("empty_string")
    df.to_csv("~/ip_files/countries_clean.csv")
    print("File is clean and date is added in file")