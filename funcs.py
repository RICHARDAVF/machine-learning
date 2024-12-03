import unicodedata,re
import pandas as pd
from datetime import datetime
import vars
import numpy as np
accented_chars = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")


def valid_month_year(path:str):

    date = path.split("-")[-1].split(".")[0]
    month = date[:2]
    year = date[2:]
    return  int(year)==2024 and month not in ["en","fe","ma","ab","my","jn","jl","ag"]


def clean_text(text):
    if pd.isna(text):
        return np.nan
    
    if isinstance(text,(datetime,int,float)):
        return np.nan
    text = ''.join(
        char for char in unicodedata.normalize('NFD', text)
        if unicodedata.category(char) != 'Mn'
    )
    
 
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
   
    text = re.sub(r'\s+', ' ', text)
    
   
    return text.strip()

def upper_data(df):
   
    accented_chars = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")
    
    def clean_text(text):
        return text.translate(accented_chars).upper() if isinstance(text, str) else text
    return df.map(clean_text)
def concatenate_data(data:pd.DataFrame,indice:pd.DataFrame,filename:str,filepath:str,tipe:str):
    new_filename  = f"{filepath}/{tipe}_{filename}"
    index_name = f'{filepath}/{tipe}_indices.xlsx'
    try:
        existing_data = pd.read_excel(new_filename)
        existing_data = existing_data.reset_index(drop=True)
        data = data.reset_index(drop=True)
        max_rows = max(len(existing_data), len(data))
        existing_data = existing_data.reindex(index=range(max_rows)).fillna(0)  
        data = data.reindex(index=range(max_rows)).fillna(0)  
        combined_data = pd.concat([existing_data, data], axis=1)
    except:
        combined_data = data
    indice.to_excel(index_name,index=False)
    combined_data.to_excel(new_filename, index=False)
meses_orden = {
    "en": 1, "fe": 2, "ma": 3, "ab": 4, "my": 5, "jn": 6,
    "jl": 7, "ag": 8, "se": 9, "oc": 10, "no": 11, "di": 12
}
def ordenar_columnas(column_name):

    match = re.match(r"([a-z]{2})-(\d{4})", column_name, re.IGNORECASE)
    if match:
        mes, anio = match.groups()
        mes = mes.lower()
        if mes in meses_orden:
            return (int(anio), meses_orden[mes])
def es_fecha(valor):
    # Intentar convertir a datetime y devolver True si se logra, indicando que es una fecha
    try:
        datetime.strptime(str(valor), "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False
reporte_mes1 = [f"DE {months.upper()} DE {year}" for months in vars.MONTHS for year in vars.YEARS]
reporte_mes2 = [f"AL {months.upper()} DE {year}" for months in vars.MONTHS for year in vars.YEARS]
