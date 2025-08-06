# Shopee-Payment-Report

## 🔍 Sobre o projeto

O **Shopee Payment Report** é uma ferramenta desenvolvida em **Python** para automatizar a **conciliação de pagamentos em duplicidade** realizados pela Shopee.

O projeto surgiu a partir de uma necessidade identificada na plataforma **Dootax**, que é utilizada para efetuar pagamentos de notas fiscais eletrônicas (NFEs) e notas de conhecimento de transporte (CTEs). A Shopee enviou um relatório contendo possíveis duplicidades, e com base nesse material, foi criado um programa capaz de identificar registros repetidos e cruzar essas informações com os pagamentos realizados pela Dootax.

A solução facilita a conferência manual, reduz riscos de erro e aumenta a eficiência na identificação de pagamentos indevidos.

---

## ⚙️ Como funciona

O projeto é dividido em duas etapas principais:

### 1️⃣ Identificação de duplicidades no relatório da Shopee

- 📥 Recebe como entrada o relatório enviado pela Shopee;
- 🔑 Utiliza **campos-chave** definidos no código para detectar registros duplicados;
- 📊 Gera dois arquivos:
  - registros únicos
  - registros duplicados

### 2️⃣ Conciliação com os dados da plataforma Dootax

- 📥 Recebe como entrada o relatório de pagamentos extraído da **Dootax**;
- 🔍 Compara os dados com os registros duplicados da Shopee;
- 🔗 Cruza os dados com base em **campos-chave correspondentes**;
- 📤 Gera um relatório final consolidado com os documentos **efetivamente pagos em duplicidade**.

---

