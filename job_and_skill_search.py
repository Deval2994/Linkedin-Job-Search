"""
Description: This file is only used for testing purpose
"""

import confedential as c
from fetch_data_by_webscrapping import DataFetcher
from export_data import ExportData




if __name__ == "__main__":
    # df = DataFetcher(username=c.username,password=c.password,job_title='m',size=0)
    # print(df.data_frame)

    # 4056645532
    df = DataFetcher(username=c.username, password=c.password, job_title='data', size=26)
    print(df.data_frame)
    ExportData(df.data_frame)
    # ExportData(df.data_frame,'csv')
    # ExportData(df.data_frame,'excel')
    # print('data exported')

