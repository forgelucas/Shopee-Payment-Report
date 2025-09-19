  <h1>🔎 Análise e Conciliação de Pagamentos</h1>
  <p>
    Este projeto contém dois scripts em <strong>Python</strong> para auxiliar na identificação de 
    <strong>registros duplicados</strong> em relatórios de clientes e na 
    <strong>conciliação de pagamentos</strong> com os dados exportados da plataforma (ex.: Dootax).
  </p>

  <h2>📦 Pré-requisitos</h2>
  <ul>
    <li>Python 3.x instalado</li>
    <li>Bibliotecas necessárias:
      <pre><code>pip install pandas openpyxl</code></pre>
    </li>
    <li>Arquivos de entrada em formato <strong>Excel (.xlsx)</strong></li>
  </ul>

  <h2>📝 Script 1 – <code>analiseDuplicidade.py</code></h2>

  <h3>Função</h3>
  <p>
    Analisa o relatório de pagamentos do cliente e separa os registros em 
    <strong>duplicados</strong> e <strong>únicos</strong>.
  </p>

  <h3>Fluxo</h3>
  <ol>
    <li>Carrega o relatório do cliente (<code>clienteRelatorio.xlsx</code>).</li>
    <li>Seleciona colunas-chave:
      <ul>
        <li><code>total_amount</code></li>
        <li><code>numero_nota_ajustado</code></li>
        <li><code>str_cnpj_contribuinte</code></li>
      </ul>
    </li>
    <li>Normaliza os dados (remove espaços, converte para <code>string</code>).</li>
    <li>Cria uma chave de comparação (<code>chave</code>).</li>
    <li>Identifica registros duplicados e únicos.</li>
    <li>Exporta os resultados:
      <ul>
        <li><code>arquivosDuplicados.xlsx</code></li>
        <li><code>arquivosUnicos.xlsx</code></li>
      </ul>
    </li>
  </ol>

  <h3>Saída</h3>
  <ul>
    <li><code>arquivosDuplicados.xlsx</code> → Registros com chave repetida</li>
    <li><code>arquivosUnicos.xlsx</code> → Registros sem duplicidade</li>
  </ul>

  <div class="warning">
    <strong>⚠️ Atenção</strong><br>
    As colunas no arquivo do cliente devem ter exatamente os nomes abaixo:
  </div>

  <table>
    <tr>
      <th>Nome esperado no Excel</th>
      <th>Tipo de dado</th>
      <th>Descrição</th>
    </tr>
    <tr>
      <td><code>total_amount</code></td>
      <td>string/float</td>
      <td>Valor total da transação</td>
    </tr>
    <tr>
      <td><code>numero_nota_ajustado</code></td>
      <td>string</td>
      <td>Número da nota fiscal</td>
    </tr>
    <tr>
      <td><code>str_cnpj_contribuinte</code></td>
      <td>string</td>
      <td>CNPJ do contribuinte</td>
    </tr>
  </table>

  <h2>📝 Script 2 – <code>conciliarPagamentos.py</code></h2>

  <h3>Função</h3>
  <p>
    Compara os registros <strong>duplicados do cliente</strong> com o relatório da 
    <strong>Dootax</strong>, conciliando os pagamentos.
  </p>

  <h3>Fluxo</h3>
  <ol>
    <li>Carrega os arquivos:
      <ul>
        <li><code>dootaxRelatorio.xlsx</code></li>
        <li><code>arquivosDuplicados.xlsx</code></li>
      </ul>
    </li>
    <li>Padroniza colunas:
      <ul>
        <li>Substitui vírgulas por pontos em valores numéricos</li>
        <li>Remove espaços extras</li>
      </ul>
    </li>
    <li>Cria a chave de comparação:
      <ul>
        <li><strong>Dootax</strong>: <code>TITULO_NUMERO_CONTROLE + VALOR_TOTAL</code></li>
        <li><strong>Cliente</strong>: <code>control_num + total_amount</code></li>
      </ul>
    </li>
    <li>Faz o <code>merge</code> entre registros coincidentes</li>
    <li>Seleciona colunas relevantes</li>
    <li>Exporta para <code>pagamentosConciliados.xlsx</code></li>
  </ol>

  <h3>Saída</h3>
  <p><code>pagamentosConciliados.xlsx</code> → Relatório conciliado com dados do cliente e da plataforma</p>

  <div class="warning">
    <strong>⚠️ Atenção</strong><br>
    As colunas devem estar padronizadas conforme abaixo:
  </div>

  <h4>No relatório da Dootax (<code>dootaxRelatorio.xlsx</code>):</h4>
  <table>
    <tr>
      <th>Nome esperado no Excel</th>
      <th>Tipo de dado</th>
      <th>Descrição</th>
    </tr>
    <tr>
      <td><code>VALOR_TOTAL</code></td>
      <td>float</td>
      <td>Valor total da transação</td>
    </tr>
    <tr>
      <td><code>TITULO_NUMERO_CONTROLE</code></td>
      <td>string</td>
      <td>Número de controle do título</td>
    </tr>
  </table>

  <h4>No relatório do Cliente (<code>arquivosDuplicados.xlsx</code>):</h4>
  <table>
    <tr>
      <th>Nome esperado no Excel</th>
      <th>Tipo de dado</th>
      <th>Descrição</th>
    </tr>
    <tr>
      <td><code>total_amount</code></td>
      <td>float</td>
      <td>Valor total da transação</td>
    </tr>
    <tr>
      <td><code>control_num</code></td>
      <td>string</td>
      <td>Número de controle do cliente</td>
    </tr>
  </table>

  <h2>🚀 Como Executar</h2>
  <ol>
    <li>Coloque os arquivos <code>clienteRelatorio.xlsx</code> e <code>dootaxRelatorio.xlsx</code> na mesma pasta dos scripts.</li>
    <li>Execute a análise de duplicidade:
      <pre><code>python analiseDuplicidade.py</code></pre>
      → Gera <code>arquivosDuplicados.xlsx</code> e <code>arquivosUnicos.xlsx</code>
    </li>
    <li>Execute a conciliação de pagamentos:
      <pre><code>python conciliarPagamentos.py</code></pre>
      → Gera <code>pagamentosConciliados.xlsx</code>
    </li>
  </ol>

  <h2>⚠️ Pontos de Atenção</h2>
  <ul>
    <li>Sempre valide os <strong>nomes das colunas</strong> nos relatórios antes da execução.</li>
    <li>Caso o nome seja diferente, <strong>ajuste no código</strong> para refletir corretamente.</li>
    <li>O tratamento de <strong>tipos de dados</strong> (string, float) é essencial para criar a chave de comparação.</li>
    <li>O resultado final depende da consistência entre os relatórios do cliente e da plataforma.</li>
  </ul>
