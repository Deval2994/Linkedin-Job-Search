import confedential as c
from fetch_data_by_webscrapping import DataFetcher

if __name__ == "__main__":
    DataFetcher(username=c.username,password=c.password,job_title='Machine Learning',size=1)
