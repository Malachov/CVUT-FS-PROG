# DataFormatsConverter

## Description

This is tool for data consolidation. On the beginning there can be files in excel file, csv, parquet or sql database. There is one interface that load the data, control whether there are some NaN values, if happens, it will clear such a records and then it store it in parquet.

It is a CLI tool with no GUI. If it's a database source, setup username and password with system args.

## Links

link_to_Jira_project_epic.com


## Used tools and libraries

- Python
- Pandas
- Argparse