import pandas as pd

# 1. Carregar os arquivos 
dootax = pd.read_excel('shopee_pagamentos_dez_fev.xlsx', dtype=str)
shopee = pd.read_excel('shopee_duplicados_DEZ_FEV.xlsx', dtype=str)

# 2. Padronizar nomes das colunas usadas na comparação
dootax['VALOR_TOTAL'] = dootax['VALOR_TOTAL'].str.replace(",", ".").astype(float).round(2)
dootax['TITULO_NUMERO_CONTROLE'] = dootax['TITULO_NUMERO_CONTROLE'].str.strip()

shopee['total_amount'] = shopee['total_amount'].str.replace(",", ".").astype(float).round(2)
shopee['control_num'] = shopee['control_num'].astype(str).str.strip()

# 3. Criar chave de comparação nos dois arquivos
dootax['chave'] = dootax['TITULO_NUMERO_CONTROLE'] + "-" + dootax['VALOR_TOTAL'].astype(str)
shopee['chave'] = shopee['control_num'] + "-" + shopee['total_amount'].astype(str)

# 4. Fazer o merge apenas das linhas coincidentes
conciliado = pd.merge(dootax, shopee, on='chave', suffixes=('_dootax', '_shopee'))

# 5. Selecionar somente as colunas desejadas
colunas_desejadas = [
    'chave',
    'company_cnpj',
    'insert_date',
    'period',
    'doc_type',
    'state',
    'total_amount',
    'barcode',
    'control_num',
    'payment_id',
    'payment_date',
    'cnpj_contribuinte',
    'numero_nota_ajustado'
]
relatorio_final = conciliado[colunas_desejadas]

# 6. Salvar resultado
relatorio_final.to_excel("pagamentos_conciliacao.xlsx", index=False)

print("Arquivo 'pagamentos_conciliacao.xlsx' gerado com sucesso.")
