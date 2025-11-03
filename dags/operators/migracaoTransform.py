import pandas

def transform_departamentos(**kwargs):
    departamentos = kwargs["ti"].xcom_pull(task_ids = "extract_departamentos")
    df = pandas.read_json(departamentos, orient = "records")

    df = df.rename(columns = {"localizacao": "cidade"})

    map_uf = {
        # Sudeste
        "são paulo": "SP",
        "rio de janeiro": "RJ", 
        "belo horizonte": "MG",
        "vitória": "ES",
        "campinas": "SP",
        "são bernardo do campo": "SP",
        "são josé dos campos": "SP",
        "ribeirão preto": "SP",
        "uberlândia": "MG",
        "contagem": "MG",
        "juiz de fora": "MG",
        "niterói": "RJ",
        "duque de caxias": "RJ",
        "serra": "ES",
        "vila velha": "ES",
        
        # Sul
        "porto alegre": "RS",
        "curitiba": "PR",
        "florianópolis": "SC",
        "caxias do sul": "RS",
        "pelotas": "RS",
        "canoas": "RS",
        "joinville": "SC",
        "blumenau": "SC",
        "londrina": "PR",
        "maringá": "PR",
        "ponta grossa": "PR",
        
        # Centro-Oeste
        "brasília": "DF",
        "goiânia": "GO",
        "campo grande": "MS",
        "cuiabá": "MT",
        "aparecida de goiânia": "GO",
        "anápolis": "GO",
        "rio verde": "GO",
        
        # Nordeste
        "salvador": "BA",
        "fortaleza": "CE", 
        "recife": "PE",
        "maceió": "AL",
        "natal": "RN",
        "joão pessoa": "PB",
        "teresina": "PI",
        "são luís": "MA",
        "aracaju": "SE",
        "feira de santana": "BA",
        "juazeiro do norte": "CE",
        "olinda": "PE",
        "jaboatão dos guararapes": "PE",
        "paulista": "PE",
        
        # Norte
        "manaus": "AM",
        "belém": "PA",
        "porto velho": "RO", 
        "rio branco": "AC",
        "macapá": "AP",
        "boa vista": "RR",
        "santarém": "PA",
        "palmas": "TO",
        "ananindeua": "PA"
    }

    df["uf"] = df["cidade"].str.lower().map(map_uf)

    return df

def transform_cargos(**kwargs):
    cargos = kwargs["ti"].xcom_pull(task_ids = "extract_cargos")
    df = pandas.read_json(cargos, orient = "records")

    df["salario_base"] = pandas.to_numeric(df["salario_base"], errors = "coerce")
    df["salario_base"] = df["salario_base"] + 500

    return df

def transform_funcionarios(**kwargs):
    funcionarios = kwargs["ti"].xcom_pull(task_ids = "extract_funcionarios")
    df = pandas.read_json(funcionarios, orient = "records")

    df["email"] = [
        "anasouzateste@email.com",
        "brunooliveirateste@email.com",
        "carlossilvateste@email.com",
        "danielamendesteste@email.com",
        "eduardolimateste@email.com"
    ]

    return df

def transform_salarios(**kwargs):
    salarios = kwargs["ti"].xcom_pull(task_ids = "extract_salarios")
    df = pandas.read_json(salarios, orient = "records")

    df["valor"] = pandas.to_numeric(df["valor"], errors = "coerce")
    df["valor"] = df["valor"] + 500

    return df