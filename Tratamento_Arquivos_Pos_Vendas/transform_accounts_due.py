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
arquivo1 = arquivos[0]
arquivo2 = arquivos[1]

# # Lendo arquivo Excel
df_view1 = pd.read_excel(arquivo1, dtype=str)
df_view2 = pd.read_excel(arquivo2, dtype=str)

# condição para validar a vencer
if len(df_view1) < len(df_view2):
    # Limpar e padronizar nomes das colunas
    df_view1.columns = df_view1.columns.map(lambda x: x.strip().lower().replace(" ", "_"))

    df_final = df_view1[[ 'id_cliente_servico_contrato'
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

    # Removendo linhas com '-' no id_cliente
    df_final = df_final[~df_final['id_cliente_servico_contrato'].str.contains("-", na=False)]

    # Salvando arquivo para utilização de graficos ou update em db
    df_final.to_excel(caminho_destino, index=False, engine="openpyxl")
    df_final.to_csv(caminho_destino_csv, index=False, sep=';', encoding='utf-8')
else:
    # Limpar e padronizar nomes das colunas
    df_view2.columns = df_view2.columns.map(lambda x: x.strip().lower().replace(" ", "_"))

    df_final = df_view2[[ 'id_cliente_servico_contrato'
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

    # Removendo linhas com '-' no id_cliente
    df_final = df_final[~df_final['id_cliente_servico_contrato'].str.contains("-", na=False)]

    # Salvando arquivo para utilização de graficos ou update em db
    df_final.to_excel(caminho_destino, index=False, engine="openpyxl")
    df_final.to_csv(caminho_destino_csv, index=False, sep=';', encoding='utf-8')
