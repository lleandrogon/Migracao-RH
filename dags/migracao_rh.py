from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from datetime import datetime
import pendulum

from operators.migracaoExtract import *

dag = DAG(
    dag_id = "postgreSQL_to_MySQL",
    schedule = "0 21 * * *",
    default_args = {
        "owner": "Airflow",
        "retries": 1,
        "start_date": pendulum.datetime(2025, 10, 31, tz = "America/Sao_Paulo"),
    },
    catchup = False,
    tags = ["pgsql", "mysql"]
)

e_cargos = PythonOperator(
    task_id = "extract_cargos",
    python_callable = extract_cargos,
    dag = dag
)

e_departamentos = PythonOperator(
    task_id = "extract_departamentos",
    python_callable = extract_departamentos,
    dag = dag
)

e_funcionarios = PythonOperator(
    task_id= "extract_funcionarios",
    python_callable = extract_funcionarios,
    dag = dag
)

e_salarios = PythonOperator(
    task_id = "extract_salarios",
    python_callable = extract_salarios,
    dag = dag
)

[e_cargos, e_departamentos, e_funcionarios, e_salarios]