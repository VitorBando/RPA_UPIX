# Importações
import zipfile
import os
import glob
from dotenv import load_dotenv
from datetime import date

# Variáveis
load_dotenv()
dirs = os.environ['DIR']
destino = os.environ['DESTINY']
hoje = date.today().strftime("%Y-%m-%d")

destino_hoje = os.path.join(destino, hoje)
os.makedirs(destino_hoje, exist_ok=True)

# Encontra todos os arquivos .zip na pasta
arquivos_hubsoft_zip = glob.glob(os.path.join(dirs, '*.zip'))

# Percorre cada arquivo ZIP
for arquivo in arquivos_hubsoft_zip:
    # Nome base do arquivo ZIP (sem extensão) para criar subpasta
    nome_base = os.path.splitext(os.path.basename(arquivo))[0]
        
    # Extrai o ZIP para a subpasta
    with zipfile.ZipFile(arquivo, 'r') as zip_ref:
        zip_ref.extractall(destino_hoje)
    
