from google.cloud import bigquery

import requests

class ApiDownloader:
    # as i get to choose the api, i'll define the url as a class parameter, bc it won't change.
    def __init__(self, url):
        self.url = url
    
    
    def download_data(self, limit=100):
        response = requests.get(self.url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        # 
        if isinstance(data, list):
            # to get always the limit nimber of records.
            return data[:limit]
        else:
            raise TypeError("API response must be a list of records")
        

class BigQueryUploader:
    # same logic as above, the project, dataset and table ids are parameters of the class, bc they won't change during the execution.
    # we assume the table is already created in BigQUery.
    def __init__(self, project_id, dataset_id, table_id):
        self.client = bigquery.Client(project=project_id)
        self.table_id = f"{project_id}.{dataset_id}.{table_id}"

    def upload_data(self, data):
        # We assume 'data' is a list of dictionaries, json like records.
        # Get the table (we manually created it in the GCP console)
        table = self.client.get_table(self.table_id)
        
        # Insert the data, use the returned errors to check if the upload was successful
        errors = self.client.insert_rows_json(table, data)
        if errors:
            print("Errors inserting rows:", errors)
        else:
            print("Data uploaded successfully to BigQuery.")



if __name__ == "__main__":
    
    ######### Entries #########:

    url = "https://jsonplaceholder.typicode.com/comments"
    limit = 100

    # GCP
    projectid = "project-fec042d1-2105-4fee-851"
    datasetid = "dataset_pruebatecnica"
    tableid = "SANDBOX_PruebaTecnica"

    ######### Instances #########

    downloader = ApiDownloader(url)

    ######### Execution #########

    # as the test suggests, ill download only 100 records
    data = downloader.download_data(limit)

    # Upload to BigQuery 
    uploader = BigQueryUploader(projectid, datasetid, tableid)
    uploader.upload_data(data)
   