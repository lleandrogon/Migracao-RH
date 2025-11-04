from airflow.providers.mysql.hooks.mysql import MySqlHook

def load_departamentos(**kwargs):
    departamentos = kwargs["ti"].xcom_pull(task_ids = "transform_departamentos")

    mysql_hook = MySqlHook(
        mysql_conn_id = "load_mysql",
        schema = "empresa_rh"
    )

    sql = """
        INSERT INTO departamentos (id, nome, cidade, uf)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            nome = VALUES(nome),
            cidade = VALUES(cidade),
            uf = VALUES(uf)
    """

    for row in departamentos.itertuples(index = False, name = None):
        mysql_hook.run(sql, parameters = row)

def load_cargos(**kwargs):
    cargos = kwargs["ti"].xcom_pull(task_ids = "transform_cargos")

    mysql_hook = MySqlHook(
        mysql_conn_id = "load_mysql",
        schema = "empresa_rh"
    )

    sql = """
        INSERT INTO cargos (id, nome, salario_base, id_departamento)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            nome = VALUES(nome),
            salario_base = VALUES(salario_base),
            id_departamento = VALUES(id_departamento)
    """

    for row in cargos.itertuples(index = False, name = None):
        mysql_hook.run(sql, parameters = row)

def load_funcionarios(**kwargs):
    funcionarios = kwargs["ti"].xcom_pull(task_ids = "transform_funcionarios")

    mysql_hook = MySqlHook(
        mysql_conn_id = "load_mysql",
        schema = "empresa_rh"
    )

    sql = """
        INSERT INTO funcionarios (id, nome, email, cpf, data_admissao, id_cargo, id_departamento)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            nome = VALUES(nome),
            cpf = VALUES(cpf),
            data_admissao = VALUES(data_admissao),
            id_cargo = VALUES(id_cargo),
            id_departamento = VALUES(id_departamento)
    """

    for row in funcionarios.itertuples(index = False, name = None):
        mysql_hook.run(sql, parameters = row)

def load_salarios(**kwargs):
    salarios = kwargs["ti"].xcom_pull(task_ids = "transform_salarios")

    mysql_hook = MySqlHook(
        mysql_conn_id = "load_mysql",
        schema = "empresa_rh"
    )

    sql = """
        INSERT INTO salarios (id, id_funcionario, valor, data_inicio, data_fim)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            id_funcionario = VALUES(id_funcionario),
            valor = VALUES(valor),
            data_inicio = VALUES(data_inicio),
            data_fim = VALUES(data_fim)
    """

    for row in salarios.itertuples(index = False, name = None):
        mysql_hook.run(sql, parameters = row)