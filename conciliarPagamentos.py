import pandas as pd

# 1. Carregar os arquivos 
dootax = pd.read_excel('dootaxRelatorio.xlsx', dtype=str)
cliente = pd.read_excel('arquivosDuplicados.xlsx.xlsx', dtype=str)

# 2. Padronizar nomes das colunas usadas na comparação
dootax['VALOR_TOTAL'] = dootax['VALOR_TOTAL'].str.replace(",", ".").astype(float).round(2)
dootax['TITULO_NUMERO_CONTROLE'] = dootax['TITULO_NUMERO_CONTROLE'].str.strip()

cliente['total_amount'] = cliente['total_amount'].str.replace(",", ".").astype(float).round(2)
cliente['control_num'] = cliente['control_num'].astype(str).str.strip()

# 3. Criar chave de comparação nos dois arquivos
dootax['chave'] = dootax['TITULO_NUMERO_CONTROLE'] + "-" + dootax['VALOR_TOTAL'].astype(str)
cliente['chave'] = cliente['control_num'] + "-" + cliente['total_amount'].astype(str)

# 4. Fazer o merge apenas das linhas coincidentes
conciliado = pd.merge(dootax, cliente, on='chave', suffixes=('_dootax', '_cliente'))

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
relatorio_final.to_excel("pagamentosConciliados.xlsx", index=False)

print("Arquivo 'pagamentos_conciliacao.xlsx' gerado com sucesso.")
