ENTITYS = ["Cajas_Rurales"]
STATISTICS = ["EF","IF","RPE_RCG"]
CODE_STATISTICS = {
    "Bancos":{"EF":"B-2201","IF":"B-2401","RPE_RCG":"B-2402"},
    "Financiera":{"EF":"B-3101","IF":"B-3301","RPE_RCG":"B-3302"},
    "Cajas_Municipales":{"EF":"C-1101","IF":"C-1301","RPE_RCG":"C-1252"},
    "Cajas_Rurales":{"EF":"C-2101","IF":"C-2301","RPE_RCG":"C-2257"}
}

MONTHS = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]
MONTH_PREFIX = ["en","fe","ma","ab","my","jn","jl","ag","se","oc","no","di"]
YEARS = [year for year in range(2001,2025)]
BANCOS = {
    'BANCO AZTECA DEL PERU': 'BANCO AZTECA',
    'BANCO AZTECA PERU': 'BANCO AZTECA',

    'BANCO CENCOSUD': 'BANCO CENCOSUD',
    
    'BANCO CONTINENTAL': 'BANCO CONTINENTAL',
    'BANCO BBVA PERU': 'BANCO CONTINENTAL',
    
    'BANCO DE COMERCIO': 'BANCO DE COMERCIO',
    'BANCOM': 'BANCO DE COMERCIO',
    
    'BANCO DE CREDITO CON SUCURSALES EN EL EXTERIOR': 'BANCO DE CREDITO DEL PERU S',
    'BANCO DE CREDITO DEL PERU CON SUCURSALES EN EL EXTERIOR': 'BANCO DE CREDITO DEL PERU S',
    'BANCO DE CREDITO DEL PERU': 'BANCO DE CREDITO DEL PERU',
    
    'BANCO DEL TRABAJO': 'BANCO DEL TRABAJO',
    
    'BANCO FALABELLA PERU': 'BANCO FALABELLA',
    'FALABELLA PERU SA': 'BANCO FALABELLA',
    
    'BANCO FINANCIERO': 'BANCO FINANCIERO',
    
    'BANCO GNB': 'BANCO GNB',
    
    'BANCO ICBC': 'BANCO ICBC',
    
    'BANCO INTERAMERICANO DE FINANZAS': 'BANCO INTERAMERICANO DE FINANZAS',
    
    'BANCO LATINO': 'BANCO LATINO',
    
    'BANCO RIPLEY': 'BANCO RIPLEY',
    
    'BANCO SANTANDER CENTRAL HISPANO': 'BANCO SANTANDER',
    'BANCO SANTANDER PERU': 'BANCO SANTANDER',
    'SANTANDER PERU SA': 'BANCO SANTANDER',

    'BANCO STANDARD CHARTERED': 'BANCO STANDARD CHARTERED',

    'BANCO SUDAMERICANO CON SUCURSALES EN EL EXTERIOR': 'BANCO SUDAMERICANO S',
    'BANCO SUDAMERICANO DEL PERU': 'BANCO SUDAMERICANO',
    'BANCO SUDAMERICANO': 'BANCO SUDAMERICANO',

    'BANCO WIESE SUDAMERIS': 'BANCO WIESE SUDAMERIS',

    'BANKBOSTON': 'BANKBOSTON',

    'BNP PARIBAS ANDES': 'BNP PARIBAS',
    'CITIBANK': 'CITIBANK',
    'DEUTSCHE BANK PERU': 'DEUTSCHE BANK',
    'HSBC BANK PERU': 'HSBC BANK',
    'INTERBANK CON SUCURSALES EN EL EXTERIOR': 'INTERBANK S',
    'INTERBANK PERU CON SUCURSALES EN EL EXTERIOR': 'INTERBANK S',
    'INTERBANK': 'INTERBANK',
    'MIBANCO': 'MIBANCO',
    'SCOTIABANK CON SUCURSALES EN EL EXTERIOR': 'SCOTIABANK S',
    'SCOTIABANK PERU CON SUCURSALES EN EL EXTERIOR': 'SCOTIABANK S',
    'SCOTIABANK PERU': 'SCOTIABANK',
    'TOTAL BANCA MULTIPE INCLUYENDO SUCURSALES EN EL EXTERIOR': 'TOTAL BANCA MULTIPLE S',
    'TOTAL BANCA MULTIPLE INCLUYE SUCURSALES EN EL EXTERIOR': 'TOTAL BANCA MULTIPLE S',
    'TOTAL BANCA MULTIPLE INCLUYENDO SUCURSALES EN EL EXTERIOR': 'TOTAL BANCA MULTIPLE S',
    'TOTAL BANCA MULTIPLE': 'TOTAL BANCA MULTIPLE'
}

CAJAS_MUNICIPALES = {
    "AREQUIPA": "AREQUIPA",
    "CMAC AREQUIPA": "AREQUIPA",
    "CMAC AREQUIPA": "AREQUIPA",
    "CHINCHA": "CHINCHA",
    "CMAC CHINCHA": "CHINCHA",
    "CMAC CHINCHA": "CHINCHA",
    "CUSCO": "CUSCO",
    "CMAC CUSCO": "CUSCO",
    "CMAC CUSCO": "CUSCO",
    "DEL SANTA": "DEL SANTA",
    "CMAC DEL SANTA": "DEL SANTA",
    "CMAC DEL SANTA": "DEL SANTA",
    "HUANCAYO": "HUANCAYO",
    "CMAC HUANCAYO": "HUANCAYO",
    "CMAC HUANCAYO": "HUANCAYO",
    "ICA": "ICA",
    "CMAC ICA": "ICA",
    "CMAC ICA": "ICA",
    "MAYNAS": "MAYNAS",
    "CMAC MAYNAS": "MAYNAS",
    "CMAC MAYNAS": "MAYNAS",
    "PAITA": "PAITA",
    "CMAC PAITA": "PAITA",
    "CMAC PAITA": "PAITA",
    "PISCO": "PISCO",
    "CMAC PISCO": "PISCO",
    "CMAC PISCO": "PISCO",
    "PIURA": "PIURA",
    "CMAC PIURA": "PIURA",
    "CMAC PIURA": "PIURA",
    "SULLANA": "SULLANA",
    "CMAC SULLANA": "SULLANA",
    "CMAC SULLANA": "SULLANA",
    "TACNA": "TACNA",
    "CMAC TACNA": "TACNA",
    "CMAC TACNA": "TACNA",
    "TRUJILLO": "TRUJILLO",
    "CMAC TRUJILLO": "TRUJILLO",
    "CMAC TRUJILLO": "TRUJILLO",
    "LIMA": "LIMA",
    "CMCP LIMA": "LIMA",
    "CAJA MUNICIPAL DE CREDITO POPULAR LIMA": "LIMA",
    "TOTAL CAJAS MUNICIPALES": "TOTALES",
    "TOTAL CAJAS MUNICIPALES DE AHORRO Y CREDITO": "TOTALES AHORRO Y CREDITO"
}
CAJAS_RURALES  = {
    'CAJAMARCA': 'CAJAMARCA',
    'CRAC CAJAMARCA': 'CAJAMARCA',
    'CAJASUR': 'CAJASUR',
    'CRAC CAJASUR': 'CAJASUR',
    'CHAVIN': 'CHAVIN',
    'CRAC CHAVIN': 'CHAVIN',
    'CRAC CAT': 'CAT',
    'CRAC CENSOSUD SCOTIA': 'CENSOSUD SCOTIA',
    'CRAC CREDINKA': 'CREDINKA',
    'CRAC CRUZ DE CHALPON': 'CRUZ DE CHALPON',
    'CRUZ DE CHALPON': 'CRUZ DE CHALPON',
    'CRAC DEL CENTRO': 'DEL CENTRO',
    'CRAC INCASUR': 'INCASUR',
    'CRAC LA LIBERTAD': 'LA LIBERTAD',
    'LA LIBERTAD': 'LA LIBERTAD',
    'CRAC LIBERTADORES DE AYACUCHO': 'LIBERTADORES DE AYACUCHO',
    'LIBERTADORES AYACUCHO': 'LIBERTADORES DE AYACUCHO',
    'CRAC LOS ANDES': 'LOS ANDES',
    'LOS ANDES': 'LOS ANDES',
    'CRAC NOR PERU': 'NOR PERU',
    'CRAC NUESTRA GENTE': 'NUESTRA GENTE',
    'CRAC PROFINANZAS': 'PROFINANZAS',
    'PROFINANZAS': 'PROFINANZAS',
    'CRAC PRYMERA': 'PRYMERA',
    'PRYMERA': 'PRYMERA',
    'CRAC QUILLABAMBA': 'QUILLABAMBA',
    'QUILLABAMBA': 'QUILLABAMBA',
    'CRAC RAIZ': 'RAIZ',
    'CRAC SAN MARTIN': 'SAN MARTIN',
    'SAN MARTIN': 'SAN MARTIN',
    'CRAC SENOR DE LUREN': 'SENOR DE LUREN',
    'SENOR DE LUREN': 'SENOR DE LUREN',
    'CRAC SIPAN': 'SIPAN',
    'TOTAL CAJAS RURALES DE AHORRO Y CREDITO': 'TOTAL CAJAS RURALES',
    'TOTAL CAJAS RURALES': 'TOTAL CAJAS RURALES'
}

FINANCIERAS =  {

    "FINANCIERA EDIFICAR": "FINANCIERA EDIFICAR",
    "FINANCIERA EDYFICAR": "FINANCIERA EDIFICAR",
    "FINANCIERA CONFIANZA": "FINANCIERA CONFIANZA",
    "FINANCIERA CREAR": "FINANCIERA CREAR",
    "FINANCIERA CREDINKA": "FINANCIERA CREDINKA",
    "FINANCIERA EFECTIVA": "FINANCIERA EFECTIVA",
    "FINANCIERA NUEVA VISION": "FINANCIERA NUEVA VISION",
    "FINANCIERA OH": "FINANCIERA OH",
    "FINANCIERA PROEMPRESA": "FINANCIERA PROEMPRESA",
    "FINANCIERA QAPAQ": "FINANCIERA QAPAQ",
    "FINANCIERA SURGIR": "FINANCIERA SURGIR",
    "FINANCIERA TFC SA": "FINANCIERA TFC SA",
    "FINANCIERA UNIVERSAL": "FINANCIERA UNIVERSAL",
    "FINANCIERA UNO": "FINANCIERA UNO",
    "AMERIKA FINANCIERA": "AMERIKA FINANCIERA",
    "CMR": "CMR",
    "COMPARTAMOS FINANCIERA": "COMPARTAMOS FINANCIERA",
    "CORDILLERA": "CORDILLERA",
    "CREDISCOTIA FINANCIERA": "CREDISCOTIA FINANCIERA",
    "DAEWOO": "DAEWOO",
    "FINANC DE CREDITO": "FINANC DE CREDITO",
    "MITSUI AUTO FINANCE": "MITSUI AUTO FINANCE",
    "SOLUCION FINANCIERA DE CREDITO": "SOLUCION FINANCIERA DE CREDITO",
    "TOTAL EMPRESAS FINANCIERAS": "TOTAL EMPRESAS FINANCIERAS",
    "VOLVO FINANCE": "VOLVO FINANCE"

}
