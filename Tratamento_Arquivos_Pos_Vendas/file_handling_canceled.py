import os
import glob
import win32com.client as win32
from datetime import date

# Pasta de origem
hoje = date.today().strftime("%Y-%m-%d")
origem = os.path.join(r"C:\Downloads\Bases_Relatorio", hoje)
arquivos = glob.glob(os.path.join(origem, '*cancelamento*.xlsx'))

# Inicializa o Excel
excel = win32.gencache.EnsureDispatch('Excel.Application')
excel.Visible = False  # Mantenha False para rodar em background
excel.DisplayAlerts = False

for arquivo in arquivos:
    try:
        # Abre o arquivo
        wb = excel.Workbooks.Open(os.path.abspath(arquivo))
        
        # Define o caminho para salvar o novo arquivo
        nome_arquivo = os.path.basename(arquivo)
        caminho_corrigido = os.path.join(origem, nome_arquivo)
        
        # Salva novamente
        wb.SaveAs(os.path.abspath(caminho_corrigido), FileFormat=51)  # 51 = xlOpenXMLWorkbook (.xlsx)
        wb.Close()
        print(f"Arquivo salvo com sucesso: {caminho_corrigido}")
    except Exception as e:
        print(f"Erro ao processar {arquivo}: {e}")

# Fecha o Excel
excel.Quit()
