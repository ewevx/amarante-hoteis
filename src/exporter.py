import pandas as pd
from google.cloud import bigquery
from src.interfaces import DataExporterInterface

class BigQueryPredictionExporter(DataExporterInterface):
    def __init__(self, client: bigquery.Client, destination_table: str):
        self.client = client
        self.destination_table = destination_table

    def export(self, df_predictions: pd.DataFrame):
        job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
        job = self.client.load_table_from_dataframe(
            df_predictions,
            f"{self.client.project}.{self.destination_table}",
            job_config=job_config
        )
        job.result()
        print(f"Previsões salvas em: {self.destination_table}")
