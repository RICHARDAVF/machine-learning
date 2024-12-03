import requests
import vars
import os
from  concurrent.futures import ThreadPoolExecutor
class DownloadFile:
    def __init__(self,):
        self.load_paths()
    def load_paths(self):
        print("Creando carpetas ...")
        for entity in vars.ENTITYS:
            for s in vars.STATISTICS:
                for year in vars.YEARS:
                    filepath = f"datasets/{entity}/{s}/{year}"
                    if not os.path.exists(filepath):
                        os.makedirs(filepath)
        print("Carpetas creadas ...")
    def __generate_url(self,year,month,code,month_prefix):
        url = f'https://intranet2.sbs.gob.pe/estadistica/financiera/{year}/{month}/{code}-{month_prefix}{year}.XLS'
        return  url
    def get_file(self, entity, s, year, code, month, month_prefix):
    
        url = self.__generate_url(year, month, code, month_prefix)
        
      
        response = requests.get(url, stream=True)
        
      
        if response.status_code == 200:
            
           
         
            filepath = f"datasets/{entity}/{s}/{year}/{code}-{month_prefix}{year}.xls"
            os.makedirs(os.path.dirname(filepath), exist_ok=True)

            with open(filepath, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
                
            print(f"Descargado archivo: {filepath}")
            
        else:
            print(f"Error en la descarga: {url}, código de estado: {response.status_code}")

    def download(self):
        print("Iniciando descarga ...")
        with ThreadPoolExecutor() as executor:
            tasks = []
            for entity in vars.ENTITYS:
                for s in vars.STATISTICS:
                    for year in vars.YEARS:
                        code_statistics = vars.CODE_STATISTICS[entity][s]
                        for month,month_prefix in zip(vars.MONTHS,vars.MONTH_PREFIX):
                            tasks.append(executor.submit(self.get_file,entity,s,year,code_statistics,month,month_prefix))
            for task in tasks:
                task.result()
        print("Descarga finalizada...")
        
if __name__ == "__main__":
    loader = DownloadFile()
    loader.download()