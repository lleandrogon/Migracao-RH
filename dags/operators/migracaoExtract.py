from airflow.providers.postgres.hooks.postgres import PostgresHook
import pandas

def extract_departamentos(**kwargs):
    hook = PostgresHook(postgres_conn_id = "extract_postgre")

    sql = "SELECT * FROM departamentos;"

    df = hook.get_pandas_df(sql)
    print(f"Extraídos {len(df)} departamentos")

    return df.to_json(orient = "records", date_format = "iso")

def extract_cargos(**kwargs):
    hook = PostgresHook(postgres_conn_id = "extract_postgre")

    sql = "SELECT * FROM cargos;"

    df = hook.get_pandas_df(sql)
    print(f"Extraídos {len(df)} cargos")

    return df.to_json(orient = "records", date_format = "iso")

def extract_funcionarios(**kwargs):
    hook = PostgresHook(postgres_conn_id = "extract_postgre")

    sql = "SELECT * FROM funcionarios;"

    df = hook.get_pandas_df(sql)
    print(f"Extraídos {len(df)} funcionarios")

    return df.to_json(orient = "records", date_format = "iso")

def extract_salarios(**kwargs):
    hook = PostgresHook(postgres_conn_id = "extract_postgre")
    
    sql = "SELECT * FROM salarios;"

    df = hook.get_pandas_df(sql)
    print(f"Extraídos {len(df)} salarios")

    return df.to_json(orient = "records", date_format = "iso")