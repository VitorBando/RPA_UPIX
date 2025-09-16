# Importações
import os
import glob
import pandas as pd
from datetime import date
from dotenv import load_dotenv


# Variáveis
load_dotenv()
destino = os.environ['DESTINY']

hoje = date.today().strftime("%Y-%m-%d")
origem = os.path.join(r"C:\Downloads\Bases_Relatorio", hoje)
arquivos = glob.glob(os.path.join(origem, '*cancelamento*.xlsx'))
caminho_destino = os.path.join(destino, "base_cancelados.xlsx")
caminho_destino_csv = os.path.join(destino, "base_cancelados.csv")
arquivo = arquivos[0]

# Lendo arquivo Excel
df = pd.read_excel(arquivo, dtype=str)

# Limpar e padronizar nomes das colunas
df.columns = df.columns.map(lambda x: x.strip().lower().replace(" ", "_"))

# Selecionando colunas
df_final = df[[ 'id_cliente'
               ,'nome_razaosocial'
               ,'motivo_cancelamento'
               ,'valor'
               ,'cpf_cnpj'
               ,'obs_cancelamento'
               ,'telefone_primario'
               ,'telefone_secundario'
               ,'endereco'
               ,'cidade'
               ,'email_principal'
               ,'email_secundario'
               ,'data_cancelamento'
               ,'tecnologia'
               ,'servico'
               ,'origem_cliente'
               ,'estado'
                ]]

# Removendo linhas com '-' no id_cliente
df_final = df_final[~df_final['id_cliente'].str.contains("-", na=False)]

# Salvando arquivo para utilização de graficos ou update em db
df_final.to_excel(caminho_destino, index=False, engine="openpyxl")
df_final.to_csv(caminho_destino_csv, index=False, sep=';', encoding='utf-8')
