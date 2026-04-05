from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.models.baseoperator import chain
from airflow.sdk.bases.operator import BaseOperator


# deprecated, i won't use it although it shows on the instructions. 
# from airflow.operators.dummy import DummyOperator

# as the document indicates.
default_args = {
'owner': 'airflow',
'depends_on_past': False,
'start_date': datetime(1900, 1, 1),
'retries': 1,
'retry_delay': timedelta(seconds=5)
}

# custom operator to show the time difference between now and a given date.
class TimeDiff(BaseOperator):

    # inheriting the BaseOperator class.
    def __init__(self, diff_date=None, *args, **kwargs):
        # allows to use parent class constructor and all the parameters it has.
        super().__init__(*args, **kwargs)

        self.diff_date = diff_date

    # we use the designated method execute from the BaseOperator class to execute our custom logic.
    def execute(self, context):
        print(datetime.now() - self.diff_date)


with DAG("test", 
    default_args=default_args,
    description="Test DAG Prueba Tecnica",
    catchup=False,
    # CRON expression. Minute - Hour - Day - Month - Weekday
    schedule="0 3 * * *",
    tags=['testing'],
) as dag: 

    # dummy operator is deprecated, so we use the empty operator instead.
    start = EmptyOperator(task_id="start_execution")
    end = EmptyOperator(task_id="end_execution")
    
    
    i = 10 
    tasks = []

    for i in range(1, i + 1):
        if i % 2 == 0:
            task = EmptyOperator(task_id=f"task_{i}")
            tasks.append(task)

    #we append only the even tasks, as the instructions indicate.    

    show_time_diff = TimeDiff(
        task_id = "show_time_diff",
        diff_date = datetime(2023, 1, 1)
    )

chain(
    start,
    tasks,
    show_time_diff,
    end,
)

# a hook is a way to interact with systems, such as db, api...
# a connection on the other hand is a way to store credentials and connection information for those systems.
# So, when we want to interact with a system, we can use both but hooks provide a higher level of abstraction and often include additional functionality, 
# such as error handling and retries, it simplifyies things. 