# Importações
import os
import glob
import pandas as pd
from datetime import date
from dotenv import load_dotenv


# Variáveis
load_dotenv()
hoje = date.today().strftime("%Y-%m-%d")
origem = os.path.join(r"C:\Downloads\Bases_Relatorio", hoje)
destino = os.environ['DESTINY']
caminho_destino = os.path.join(destino, "base_gerentes.xlsx")
caminho_destino_csv = os.path.join(destino, "base_gerentes.csv")
arquivos = glob.glob(os.path.join(origem, '*clientes*.xlsx'))
arquivo = arquivos[0]

# Lendo arquivo Excel
df = pd.read_excel(arquivo, dtype=str)

# Limpar e padronizar nomes das colunas
df.columns = df.columns.map(lambda x: x.strip().lower().replace(" ", "_"))

df_final = df[[ 'id_cliente'
               ,'telefone_primario'
               ,'endereco'
               ,'cidade'
               ,'estado'
               ,'email_principal'
               ,'origem_cliente'
               ,'data_cadastro'
               ,'nome_razaosocial'
               ,'telefone_secundario'
               ,'email_secundario'
               ,'cpf_cnpj'
               ,'status']]

# Removendo linhas com '-' no id_cliente
df_final = df_final[~df_final['id_cliente'].str.contains("-", na=False)]

# Salvando arquivo para utilização de graficos ou update em db
df_final.to_excel(caminho_destino, index=False, engine="openpyxl")
df_final.to_csv(caminho_destino_csv, index=False, sep=';', encoding='utf-8')
