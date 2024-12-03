import pandas as pd
import vars
import os
import numpy as np
from funcs import clean_text,valid_month_year,ordenar_columnas
from datetime import datetime
from funcs import reporte_mes1,es_fecha
from variables import variables_all_cm,variables_upper_cm,variables_all_f,variables_upper_f
import json
import pathlib
class GetVariables:
    def __init__(self,urlpatterns:str,statistics:str,type_entity:str):
        self.type_entity = type_entity
        self.size_variables = 0
        self.var_uppers =   variables_upper_cm
        self.var_all = variables_all_cm
        # self.var_uppers = variables_upper_f if type_entity== "Financiera" else variables_upper_cm
        # self.var_all = variables_all_f if type_entity== "Financiera" else variables_all_cm
        self.urlpatterns = urlpatterns
        self.statistics = statistics
        self.variables:dict = {"ACTIVO":{},"PASIVO":{}}
        self.upper_variable:dict = {"ACTIVO":{},"PASIVO":{}}
        self.type_data = "ACTIVO"
        self.entitys:set = set()
        self.filename = None
    def ingreso_compraventa(self,df:pd.DataFrame)->pd.DataFrame:
        indice = df[df['ACTIVO'].str.strip()== 'Ingresos por Compraventa de Valores no Devengados'].index

        df.drop(indice, inplace=True,axis=0)
        return df.reset_index(drop=True)
    def clean_firts_moment(self,df:pd.DataFrame)->pd.DataFrame:
        df.dropna(axis=0,how="all",inplace=True)
        df.dropna(axis=1,how="all",inplace=True)
        return df.reset_index(drop=True).copy(deep=True)
    def get_data_total(self,df:pd.DataFrame):
        column_total = [i for i in range(len(df.columns)) if str(df.iloc[1, i]).strip().upper() == 'TOTAL']
        nombres = df.iloc[0, [i - 2 for i in column_total]].reset_index(drop=True)
        df.iloc[0, column_total] = nombres
        df.iloc[0, [i - 2 for i in column_total]] = np.nan
        df = df.dropna(axis=1, subset=[0], how='any').reset_index(drop=True)
        df.columns = df.iloc[0]
        df.drop(index=[0,1],axis=0,inplace=True)
        df = df.loc[:, ~df.columns.duplicated()]
        try:
            df.drop(columns=["Activo"],inplace=True)
        except:
            print("ARCHIVO SIN CAMPO ACTIVO DUPLICADO")
        return df.reset_index(drop=True).copy(deep=True)
    def get_name_entity(self,name_entity)->str:
        try:
            if self.type_entity == "Financiera":
                return vars.FINANCIERAS[name_entity]
            elif self.type_entity == "Cajas_Municipales":
                return vars.CAJAS_MUNICIPALES[name_entity]
            elif self.type_entity == "Cajas_Rurales":
                return vars.CAJAS_RURALES[name_entity]
            elif self.type_entity == "Bancos":
                return vars.BANCOS[name_entity]
            else:
                return name_entity
        except:
            return name_entity
    def get_variables(self,df:pd.DataFrame)->pd.DataFrame:
        try:


            variables = list(df["ACTIVO"].map(clean_text).to_list())
            var_upper = None
            var_type = "ACTIVO"
            for index,var in enumerate(variables):
                if var.isupper():
                    var_upper = var
                    self.upper_variable[var_type][var_upper] = f"fila {index}"
                if var.isupper() and var == "OBLIGACIONES CON EL PUBLICO":
                    var_type = "PASIVO"
                if  var.isupper() and var not in self.variables[var_type] :
                    self.variables[var_type][var] = {}
                    continue
                if not var.isupper() and var not in self.variables[var_type][var_upper]:
                    self.variables[var_type][var_upper][var] = f"fila {index}"

            df["ACTIVO"] = variables
            return df
        except Exception as e:
            raise ValueError(str(e),"get_variable",var_type,var_upper)
    def get_col_row_activo(self,df:pd.DataFrame)->list[int,int]:
        col = 0
        row = 0
        for item in df.itertuples():
  
            index,col1,col2,col3 = item
            row = index
            if str(col1).strip().upper()=="ACTIVO":
                col = 0
                break
            elif str(col2).strip().upper()=="ACTIVO":
                col = 1
                break
            elif str(col3).strip().upper()=="ACTIVO":
                col = 2
                break
        
        return [col,row]
    def verifi_var(self,var_name:str):
        if "Ver cuadro" in var_name or "Ver Cuadro" in var_name:
            return var_name.split("Ver cuadro N")[0].strip()
        return var_name
    def create_files_clean(self,df:pd.DataFrame):
        try:
            variables = list(df["ACTIVO"].to_list())
            new_variables = []
            var_type = "ACTIVO"
            var_upper = None
            for var in variables:
                var = self.verifi_var(var)
                if var.upper() == "OBLIGACIONES CON EL PUBLICO":
                    var_type = "PASIVO"
                if var.isupper():
                    var_upper = var
                    row_header = self.var_uppers[var_type][var]
                    new_variables.append(row_header)
                else:
                    row_header = self.var_uppers[var_type][var_upper]
                    row_children = self.var_all[var_type][row_header][var]
                    new_variables.append(row_children)
            df.insert(0,"row_name",new_variables) 
            df = df.copy(deep=True).reset_index(drop=True)
    
            rango_completo = pd.DataFrame({'row_name': [f'fila {i}' for i in range(0, 102)]})

            df_completo = pd.merge(rango_completo[["row_name"]], df, on='row_name', how='left')
            df_vass = pd.read_excel(f"Variables {self.type_entity}.xlsx")
            df_completo["ACTIVO"] = df_vass[["VARIABLES/FECHA"]]
            return df_completo.copy(deep=True).reset_index(drop=True)
        except Exception as e:
            raise ValueError(str(e),var_type,var_upper,"create_files_clean")
    def create_file_by_entity(self,df:pd.DataFrame,month:str,year:int):

        try:
            entintys = list(df.columns[2:])
        
            for entity in entintys:
                data = df[[entity]].copy(deep=True)
                data.columns = [f"{month}-{year}"]
                data = data.reset_index(drop=True)
                directory = f"date_joins/{self.type_entity}"
                os.makedirs(directory,exist_ok=True)
                clean_name = clean_text(entity).upper()
                filename =  self.get_name_entity(clean_name)+".xlsx"
                filepath = f"{directory}/{filename}"
                file_path = pathlib.Path(filepath)
                if file_path.exists():
                    df_exist = pd.read_excel(filepath)
                    new_df = pd.concat([df_exist,data],axis=1)
                else:
                    new_df = data
                new_df.to_excel(filepath,index=False)
        except Exception as e:
            raise ValueError(str(e),"create_file_by_entity")
            
    
    def read_directory(self):

        for year in vars.YEARS:
            pathname = f"{self.urlpatterns}/{self.type_entity}/{self.statistics}/{year}"
            for file in os.listdir(pathname):
                try:
                    filepath = f"{pathname}/{file}"

                    self.filename = file
                    df = self.read_file(filepath)

                    df = self.get_variables(df)

                    df = self.create_files_clean(df)
    
                    file_name = file.split(".")[0]+".xlsx"
                    os.makedirs(f"data_clean/{self.type_entity}/EF/{year}",exist_ok=True)
                    df.to_excel(f"data_clean/{self.type_entity}/EF/{year}/{file_name}",index=False)
                    month = file.split("-")[-1].split(".")[0][:2]
                    self.create_file_by_entity(df,month,year)
                    print(f"Archivo {filepath} procesado")
                except Exception as e:
                    print(str(e),"read_directory",filepath)
       
            
        # with open(f"Variables_all_{self.type_entity}.json","w") as file:
        #     json.dump(self.variables,file,indent=4)
        # with open(f"variables_upper_{self.type_entity}.json","w") as file:
        #     json.dump(self.upper_variable,file,indent=4)

    def create_df_variables(self):
        data = {"VARIABLES/FECHA":[],"FILA":[]}
        for type_var in ["ACTIVO","PASIVO"]:
            for key,value in self.var_uppers[type_var].items():
                data["VARIABLES/FECHA"].append(key)
                data["FILA"].append(value)
                if value in self.var_all[type_var]:
                    for k,v in self.var_all[type_var][value].items():
                        data["VARIABLES/FECHA"].append(k)
                        data["FILA"].append(v)
        df_variables = pd.DataFrame(data)
        df = df_variables.drop_duplicates(subset=["FILA"]).reset_index(drop=True)
        self.size_variables = len(df)
        df.to_excel(f"Variables {self.type_entity}.xlsx",index=False)
    def read_file(self,path:str)->pd.DataFrame:
        try:
            if valid_month_year(path):
                raise ValueError("Archivo no valido")
            sheet_name = self.valid_file(path)
            df = pd.read_excel(io=path,sheet_name=sheet_name,header=None)
            df = self.clean_firts_moment(df).reset_index(drop=True)
            col,row = self.get_col_row_activo(df.iloc[:15,:3])
            df = df.iloc[row:,col:].copy(deep=True).reset_index(drop=True)
            df.iloc[0,0] = "ACTIVO"
            df.iloc[1,0] = "MONEDA"
            df = self.get_data_total(df)
            df = self.ingreso_compraventa(df)
            df.dropna(inplace=True)
            df.reset_index(drop=True)
            return df
        except Exception as e:
            raise ValueError(str(e),"read_file")
    def valid_file(self,path)->str:
        try:
            file = pd.ExcelFile(path)
            sheet_names = file.sheet_names
            return sheet_names[0]
        except Exception as e:
            raise ValueError(str(e))
    def reporte_balance_general(self, filename):
        urlpattern = f"date_joins/{self.type_entity}"
        dataframes = {}
        df_vars = pd.read_excel(f"Variables {self.type_entity}.xlsx")
        for file in os.listdir(urlpattern):
            filepath = f"{urlpattern}/{file}"
            df = pd.read_excel(filepath)
            df_name = file.split('.')[0]
            order_columns = sorted(df.columns, key=ordenar_columnas)
            df = df[order_columns]
            df = df.reset_index(drop=True)
            new_df = pd.concat([df_vars[["VARIABLES/FECHA"]], df], axis=1)
            dataframes[df_name] = new_df
        with pd.ExcelWriter(filename) as writer:
            for sheet, df in dataframes.items():
                df.to_excel(writer, sheet_name=sheet[:30], index=False)       
if __name__ == "__main__":
    urlpattern = "datasets"
    instance = GetVariables(urlpattern,"EF","Cajas_Municipales")
    instance.create_df_variables()
    instance.read_directory()
    instance.reporte_balance_general("Balance General Cajas Municipales.xlsx")