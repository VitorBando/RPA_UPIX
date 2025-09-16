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
arquivos = glob.glob(os.path.join(origem, '*servicos*.xlsx'))
caminho_destino = os.path.join(destino, "base_a_vencer.xlsx")
caminho_destino_csv = os.path.join(destino, "base_a_vencer.csv")
arquivo = arquivos[0]

# # Lendo arquivo Excel
df = pd.read_excel(arquivo, dtype=str)

# # Limpar e padronizar nomes das colunas
df.columns = df.columns.map(lambda x: x.strip().lower().replace(" ", "_"))

df_final = df[[ 'id_cliente_servico_contrato'
                 ,'nome_razaosocial'
                 ,'valor'
                 ,'validade'
                 ,'cidade'
                 ,'servico_status'
                 ,'email_principal'
                 ,'data_inicio_contrato'
                 ,'estado'
                 ,'telefone_primario'
                 ,'servico'
                 ,'email_secundario'
                 ,'data_fim_contrato'
                ]]

# # Removendo linhas com '-' no id_cliente
df_final = df_final[~df_final['id_cliente_servico_contrato'].str.contains("-", na=False)]

# Salvando arquivo para utilização de graficos ou update em db
df_final.to_excel(caminho_destino, index=False, engine="openpyxl")
df_final.to_csv(caminho_destino_csv, index=False, sep=';', encoding='utf-8')
