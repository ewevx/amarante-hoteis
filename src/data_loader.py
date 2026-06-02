import pandas as pd
from google.cloud import bigquery
from src.interfaces import DataLoaderInterface

class BigQueryResortLoader(DataLoaderInterface):
    def __init__(self, client: bigquery.Client, project_id: str, dataset_table: str):
        self.client = client
        self.project_id = project_id
        self.dataset_table = dataset_table

    def load_data(self) -> pd.DataFrame:
        query = f"SELECT * FROM `{self.project_id}.{self.dataset_table}`"
        df = self.client.query(query, project=self.project_id).to_dataframe()
        df = df.sort_values(by=['id_resort', 'data']).reset_index(drop=True)
        return df
