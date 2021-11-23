# python app.py -d1 Moje_data -s1 data1 -d2 Moje_data -s2 data2 -jc Datum -jt outer -cl all -uf parquet -up data/clear_data.parquet
import argparse
import pandas as pd
import mydatapreprocessing
import sys
import numpy as np


parser = argparse.ArgumentParser(description="Calculate volume of a Cylinder")
group1 = parser.add_mutually_exclusive_group()
group1.add_argument("-c1", "--csv_file1", type=open, help="Address of the first csv file.")
group1.add_argument("-s1", "--sql_file1", type=str, help="Address of the first sql database.")
group1.add_argument("-p1", "--parquet_file1", type=str, help="Address of the first parquet database.")
# group1.add_argument("-e1", "--xlsx_file1", type=open, help="Address of the xlsx file 1")
group2 = parser.add_mutually_exclusive_group()
group2.add_argument("-c2", "--csv_file2", type=open, help="Address of the second csv file.")
group2.add_argument("-s2", "--sql_file2", type=str, help="Address of the second sql database.")
group2.add_argument("-p2", "--parquet_file2", type=str, help="Address of the second parquet database.")
# group2.add_argument("-e2", "--xlsx_file2", type=open, help="Address of the xlsx file 2")
parser.add_argument("-d1", "--dat_name1", type=str, help="Name of database 1.")
parser.add_argument("-d2", "--dat_name2", type=str, help="Name of database 2.")
parser.add_argument("-jc", "--join_column", type=str, help="Name of joining column.")
parser.add_argument(
    "-jt",
    "--join_type",
    type=str,
    help="Type of merge to be performed.",
    choices=["left", "right", "outer", "inner", "cross"],
)
parser.add_argument(
    "-cl",
    "--clear",
    type=str,
    help="Name of joining column.(all-clears duplicities and rows with NaN values, dupl- clears duplicities, nan- clears NaN values, none- turn off the cleaning)",
    choices=["all", "dupl", "nan", "none"],
)
parser.add_argument(
    "-uf",
    "--upload_format",
    type=str,
    help="Format of joined dataset.",
    choices=["parquet", "csv", "xlsx"],
)
parser.add_argument(
    "-up",
    "--upload_path",
    type=str,
    help="Adrress of uploaded file.",
)
args = parser.parse_args()


### Loading data

# excel_file1 = args.xlsx_file1
# excel_file2 = args.xlsx_file2
dat_name1 = args.dat_name1
sql_file1 = args.sql_file1
dat_name2 = args.dat_name2
sql_file2 = args.sql_file2
parquet_file1 = args.parquet_file1
parquet_file2 = args.parquet_file2
## Loading data 1

if args.csv_file1:
    df1 = pd.read_csv(args.csv_file1)
    print(df1)
elif args.parquet_file1:
    df1 = pd.read_parquet(parquet_file1)
    print(df1)
# elif args.xlsx_file1:
#     df1 = pd.read_excel(excel_file1)
#     print(df1)
elif args.dat_name1:
    if args.sql_file1:
        df1 = mydatapreprocessing.database.database_load(
            server=".", database=dat_name1, query=sql_file1, trusted_connection=True
        )
        print("First dataset")
        print(df1)
    else:
        print("There's no table 1 name.")
        sys.exit()
else:
    if args.sql_file1:
        print("error: There's no sql database 1 name")
        sys.exit()
    else:
        print("error: There's no input argument for first dataset")
        sys.exit()

## Loading data 1

if args.csv_file2:
    df2 = pd.read_csv(args.csv_file2)
    print(df2)
elif args.parquet_file2:
    df2 = pd.read_parquet(parquet_file2)
    print(df2)
# elif args.xlsx_file2:
#     df1 = pd.read_excel(excel_file2)
#     print(df1)
elif args.dat_name2:
    if args.sql_file2:
        df2 = mydatapreprocessing.database.database_load(
            server=".", database=dat_name2, query=sql_file2, trusted_connection=True
        )
        print("Second dataset")
        print(df2)
    else:
        print("error: There's no table 2 name.")
        sys.exit()
else:
    if args.sql_file2:
        print("error: There's no sql database 2 name.")
        sys.exit()
    else:
        print("error: There's no input argument for second dataset.")
        sys.exit()

##Joining dataframe

join_type = args.join_type
join_column = args.join_column

if args.join_type:
    if args.join_column:
        if join_column == "Datum":
            df1[join_column] = pd.to_datetime(df1[join_column])
            df2[join_column] = pd.to_datetime(df2[join_column])

        df3 = df1.merge(df2, on=join_column, how=join_type)
        print(join_type + " join was successfull")
        print("Joinded dataset")
        print(df3)
    else:
        print("error: There's no merge column name.")
        sys.exit()
else:
    if args.join_column:
        if join_column == "Datum":
            df1[join_column] = pd.to_datetime(df1[join_column])
            df2[join_column] = pd.to_datetime(df2[join_column])

        df3 = df1.merge(df2, on=join_column, how="outer")
        print("Outer join was successfull")
        print("Joinded dataset")
        print(df3)
    else:
        print("error: There's no join argument.")
        sys.exit()


### Clear dacl_ta

type = args.clear

if args.clear:
    if type == "all":
        df3 = df3.drop_duplicates()
        df3 = df3.replace(r"^\s*$", np.nan, regex=True)
        df3 = df3.dropna()
        df3 = df3.reset_index(drop=True)
        print("Cleared data")
        print(df3)
    elif type == "dupl":
        df3 = df3.drop_duplicates()
        df3 = df3.reset_index(drop=True)
        print("Cleared data")
        print(df3)
    elif type == "nan":
        df3 = df3.replace(r"^\s*$", np.nan, regex=True)
        df3 = df3.dropna()
        df3 = df3.reset_index(drop=True)
        print("Cleared data")
        print(df3)
    elif type == "none":
        df3 = df3.reset_index(drop=True)
        print("Data clearing was skipped")
else:
    df3 = df3.drop_duplicates()
    df3 = df3.replace(r"^\s*$", np.nan, regex=True)
    df3 = df3.dropna()
    df3 = df3.reset_index(drop=True)
    print("Cleared data")
    print(df3)


### Uploading data

uformat = args.upload_format
upath = args.upload_path


if args.upload_format:
    if args.upload_path:
        if uformat == "parquet":
            df3.to_parquet(upath, index=False)
            print("Dataset was succesfully uploaded in ." + uformat + " format to adrress: " + upath)
        elif uformat == "csv":
            df3.to_csv(upath, index=False)
            print("Dataset was succesfully uploaded in ." + uformat + " format to adrress: " + upath)
        elif uformat == "xlsx":
            df3.to_csv(upath, index=False)
            print("Dataset was succesfully uploaded in ." + uformat + " format to adrress: " + upath)

    else:
        print("error: There's no upload path.")
        sys.exit()
else:
    if args.upload_path:
        print("error: There's file format for uploading.")
        sys.exit()
    else:
        print("error: There's no input argument for file uploading.")
        sys.exit()
