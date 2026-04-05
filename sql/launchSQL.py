from google.cloud import bigquery

client = bigquery.Client(project="project-fec042d1-2105-4fee-851")

sql_file = "sql/transform.sql"

with open(sql_file, "r") as f:
    query = f.read()

query_job = client.query(query)

query_job.result()

print(f"Transformación ejecutada correctamente. Filas afectadas: {query_job.num_dml_affected_rows}")