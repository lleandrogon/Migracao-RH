# 🚀 Projeto de Migração RH – ETL com Apache Airflow

Este projeto implementa um pipeline ETL (Extract, Transform, Load) para migração de dados de Recursos Humanos de um banco PostgreSQL para MySQL, utilizando Apache Airflow e Pandas.

---

## 📋 Visão Geral

O objetivo é automatizar o processo de migração de dados entre bancos, garantindo integridade, consistência e rastreabilidade.  
O fluxo consiste em extrair, transformar e carregar informações de tabelas do sistema de RH.

Tabelas migradas:
🏢 departamentos - Informações sobre os departamentos da empresa  
💼 cargos - Dados de cargos e posições  
👨‍💼 funcionarios - Cadastro completo de funcionários  
💰 salarios - Histórico e informações salariais  

---

## 🧩 Tecnologias Utilizadas

🌀 Apache Airflow - Orquestração do pipeline ETL  
🐳 Docker / Docker Compose - Containerização e ambiente de execução  
🐍 Python - Linguagem principal do projeto  
🧠 Pandas - Transformação e manipulação de dados  
🐘 PostgreSQL - Banco de dados de origem  
🐬 MySQL - Banco de dados de destino  

---

## ⚙️ Configuração e Instalação

### 🔧 Pré-requisitos
- Docker  
- Docker Compose  

---

### 📦 Passos para Execução

1. Clone o repositório:
   git clone <url-do-repositorio>  
   cd migracao-rh  

2. Configure os bancos de dados:
   - Configure seu PostgreSQL e MySQL locais.  
   - Certifique-se de que as credenciais estejam corretas para conexão via UI do Airflow.  

3. Inicie o Airflow com Docker:
   docker-compose up -d  

4. Acesse o Airflow:
   Abra o navegador e vá para: http://localhost:8080  

5. Verifique as DAGs:
   - Na interface do Airflow, localize a DAG de migração.  
   - Ative a DAG e clique em "Trigger DAG" para iniciar a execução.  

6. Acompanhe o pipeline:
   - Utilize o gráfico da DAG no Airflow para visualizar cada etapa (Extract → Transform → Load).  
   - Consulte os logs das tasks para verificar o progresso e possíveis erros.  

7. Valide os dados no MySQL:
   - Após a execução, acesse o banco de destino e valide se as tabelas foram carregadas corretamente.  
   - Use um cliente SQL ou o próprio terminal para conferir:  
     SELECT * FROM funcionarios LIMIT 10;  

---

## 📈 Estrutura do Pipeline

O processo ETL é composto pelas seguintes etapas:

1. Extract – Leitura dos dados do PostgreSQL  
2. Transform – Limpeza e padronização dos dados com Pandas  
3. Load – Inserção dos dados tratados no MySQL  

O Apache Airflow coordena essas etapas garantindo execução ordenada, logs e monitoramento visual.

---

## 🧠 Benefícios do Projeto

- Automação completa da migração de dados  
- Garantia de consistência e integridade  
- Escalabilidade e fácil manutenção  
- Monitoramento via UI do Airflow  
- Registro detalhado de execução e falhas  