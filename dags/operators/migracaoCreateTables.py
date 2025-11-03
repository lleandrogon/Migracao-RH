query = """
    CREATE TABLE IF NOT EXISTS departamentos(
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100),
        cidade VARCHAR(100),
        uf VARCHAR(2)
    );

    CREATE TABLE IF NOT EXISTS cargos(
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100),
        salario_base DECIMAL(10,2),
        id_departamento INT,
        FOREIGN KEY (id_departamento) REFERENCES departamentos(id)
    );

    CREATE TABLE IF NOT EXISTS funcionarios(
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100),
        email VARCHAR(255),
        cpf VARCHAR(14),
        data_admissao DATE,
        id_cargo INT,
        id_departamento INT,
        FOREIGN KEY (id_cargo) REFERENCES cargos(id),
        FOREIGN KEY (id_departamento) REFERENCES departamentos(id)
    );

    CREATE TABLE IF NOT EXISTS salarios(
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        id_funcionario INT,
        valor DECIMAL(10,2),
        data_inicio DATE,
        data_fim DATE,
        FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id)
    );
"""