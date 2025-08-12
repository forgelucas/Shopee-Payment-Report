import pandas as pd

# 1. Carregar o arquivo
df = pd.read_excel('clienteRelatorio.xlsx')  

# 2. Selecionar e normalizar colunas relevantes
colunas_chave = [
    'total_amount',
    'numero_nota_ajustado',
    'str_cnpj_contribuinte'
]

for col in colunas_chave:
    df[col] = df[col].astype(str).str.strip()

# 3. Criar chave de comparação
df['chave'] = df[colunas_chave].agg('-'.join, axis=1)

# 4. Identificar duplicidades
duplicados = df[df.duplicated('chave', keep=False)]

# 5. Identificar registros únicos
unicos = df[~df['chave'].isin(duplicados['chave'])]

# 6. Exportar resultados
duplicados.to_excel('arquivosDuplicados.xlsx', index=False)
unicos.to_excel('arquivosUnicos.xlsx', index=False)

print("Análise finalizada!")
