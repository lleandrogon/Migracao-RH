from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.models.baseoperator import cross_downstream

from datetime import datetime
import pendulum

from operators.migracaoExtract import *
from operators.migracaoTransform import *
from operators.migracaoCreateTables import query

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

e_departamentos = PythonOperator(
    task_id = "extract_departamentos",
    python_callable = extract_departamentos,
    dag = dag
)

e_cargos = PythonOperator(
    task_id = "extract_cargos",
    python_callable = extract_cargos,
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

t_departamentos = PythonOperator(
    task_id = "transform_departamentos",
    python_callable = transform_departamentos,
    dag = dag
)

t_cargos = PythonOperator(
    task_id = "transform_cargos",
    python_callable = transform_cargos,
    dag = dag
)

t_funcionarios = PythonOperator(
    task_id = "transform_funcionarios",
    python_callable = transform_funcionarios,
    dag = dag
)

t_salarios = PythonOperator(
    task_id = "transform_salarios",
    python_callable = transform_salarios,
    dag = dag
)

create_tables = SQLExecuteQueryOperator(
    task_id = "create_tables",
    conn_id = "load_mysql",
    sql = query,
    dag = dag
)

cross_downstream(
    [e_cargos, e_departamentos, e_funcionarios, e_salarios],
    [t_cargos, t_departamentos, t_funcionarios, t_salarios]
)

cross_downstream(
    [t_cargos, t_departamentos, t_funcionarios, t_salarios],
    [create_tables]   
)