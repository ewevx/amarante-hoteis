# Hotéis: Inteligência Preditiva aplicada ao Revenue Management (RM)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)![Google Colab](https://img.shields.io/badge/Google%20Colab-%23F9AB00.svg?style=for-the-badge&logo=google-colab&logoColor=white)![Google BigQuery](https://img.shields.io/badge/Google%20BigQuery-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)![SQL](https://img.shields.io/badge/SQL-CC2927?style=for-the-badge&logo=lists&logoColor=white)![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

Este repositório apresenta uma solução de dados *End-to-End* desenvolvida para mitigar um dos maiores desafios da indústria hoteleira de alto padrão: **a flutuação imprevisível de demanda e o risco de sub-ocupação em períodos de alta temporada em resorts de luxo** (como o **Salinas Maragogi** e o **Japaratinga Lounge**).

Utilizando uma arquitetura moderna em nuvem e modelagem preditiva via Deep Learning, o projeto automatiza a previsão de ocupação para os próximos 30 dias, gerando gatilhos dinâmicos de precificação para maximizar o RevPAR (*Revenue Per Available Room*) e otimizar a receita da rede.

---

## A Dor do Negócio 

Gerenciar a receita de resorts *All-Inclusive* exige precisão. Se a tarifa balcão permanecer muito alta em semanas de baixa procura, os quartos ficam vazios e o custo operacional fixo destrói a margem. Se a tarifa estiver baixa em períodos de explosão de demanda (como feriados e janelas de alta temporada aceleradas por buscas externas), a empresa perde a oportunidade de capturar receita.

**A Solução Prática:** 
Substituir o modelo tradicional de precificação reativa por um **Pipeline de Dados Preditivo**. Ao cruzar o comportamento histórico da curva de reservas (*Booking Curve*) com fatores externos (sazonalidade e tendências de busca do mercado), antecipamos a taxa de ocupação. O time de Revenue Management deixa de "reagir" ao mercado e passa *a ditar a estratégia de preço com até um mês de antecedência*.

---

## Arquitetura e Engenharia de Dados

O projeto foi estruturado sob os pilares da programação orientada a objetos (POO) e inversão de dependência, garantindo manutenciabilidade e escalabilidade para produção:

1. **Camada de Modelagem (Google Colab / Python / PyTorch):** Desenvolvimento de uma rede neural **LSTM Bidirecional** que processa sequências temporais de 90 dias de contexto. O modelo assimila variáveis complexas como *Lag Features* hoteleiras (7, 14, 30 e 45 dias), variáveis cíclicas temporais e feriados.
2. **Data Warehouse (Google BigQuery / GoogleSQL):** Centralização e governança dos dados. Os resultados gerados pelo modelo no Python são injetados diretamente em tabelas dedicadas na camada *Gold* do Data Warehouse.
3. **Analytics e BI (Tableau Desktop):** Construção de dashboards estratégicos alimentados por consultas SQL personalizadas (`UNION ALL`) diretamente no repositório em nuvem.

---

## Módulos do Dashboard e Análise Visual

O ecossistema visual foi dividido em 3 visões estratégicas para atender tanto o nível C-Level (Decisão Executiva) quanto o operacional tático (Analistas de RM):

### Visão 1: Painel de Controle do RevPAR Preditivo (Foco Executivo)
* **Termômetro de Metas:** Indicadores semânticos de semáforo (*Verde*: Meta Batida | *Amarelo*: Atenção | *Vermelho*: Risco Crítico) calculados com base no faturamento projetado para as próximas semanas.
* **Booking Curve Inteligente:** Gráfico de linhas sobrepostas comparando o histórico real de quartos ocupados com o comportamento tracejado da previsão gerada pela Inteligência Artificial.

<img width="1366" height="766" alt="Captura de tela 2026-06-03 151920" src="https://github.com/user-attachments/assets/d03c13eb-f5c8-4b0f-bcf6-f8c259759069" />

### Visão 2: Matriz de Elasticidade e Otimização de Tarifa (Foco Operacional)
* **Gatilhos Automáticos de Preço:** Tabela de decisão automatizada baseada no volume de demanda futura mapeada pela rede neural, exibindo alertas de ação como: *“Demanda Aquecida: Sugestão de aumento de +12% na tarifa balcão”* ou *“Baixa Procura: Avaliar Ação Promocional (-10%)”*.
* **Elasticidade-Preço:** Gráfico de dispersão cruzando a Diária Média Praticada (ADR) com a demanda futura, permitindo identificar graficamente o teto de preço antes da perda de tração de reservas.

<img width="1363" height="765" alt="Captura de tela 2026-06-03 152044" src="https://github.com/user-attachments/assets/38c1b78e-e61b-443d-b6b2-2b8a60fa5239" />

### Visão 3: Monitor de Sazonalidade e Fatores Externos (Foco Tático)
* **IA vs Google Trends:** Gráfico de eixo duplo que correlaciona o volume de interesse do público na web com a taxa de ocupação real, validando o impacto do marketing digital na conversão de vendas.
* **Matriz de Calor Temporal:** Cruzamento de meses e dias da semana para identificar com exatidão os gargalos históricos e os picos sazonais de ocupação máxima.

<img width="1363" height="756" alt="Captura de tela 2026-06-03 152121" src="https://github.com/user-attachments/assets/ec2d53f6-cb39-4c02-a2fd-ed5198f4cbb0" />

---
## Fluxo de trabalho: 
Roadmap utilizado para guiar as decisões e passo a passo do projeto

<img width="1906" height="826" alt="Captura de tela 2026-06-03 160638" src="https://github.com/user-attachments/assets/4be424e0-acd2-43ed-a23c-cf7ed9de5930" />

---

 ## Notas de Implementação e Portabilidade
 **Segurança:** As chaves privadas (.json) de contas de serviço e IDs reais de infraestrutura foram 100% omitidos e protegidos por políticas de .gitignore e variáveis de ambiente.

**Portabilidade do Tableau:** Para viabilizar a auditoria do painel por terceiros sem a necessidade de credenciais de acesso direto ao ambiente privado do Google Cloud, a conexão ativa foi convertida para Extração Local (.hyper) e empacotada no formato .twbx. O painel executa de forma offline com 100% da sua interatividade mantida.

---

## Como Executar este Projeto
1.**Camada de Dados:** Os scripts de criação de tabelas e a query lógica para o Tableau estão em /sql.

2.**Camada de Inteligência:** O fluxo experimental está documentado em /notebooks. Para produção, os scripts executáveis estruturados de forma desacoplada estão localizados em /src.

3.**Camada de Negócio:** Baixe os arquivos *.twbx* na pasta *tableau* e abra-o utilizando o Tableau Desktop ou o Tableau Reader gratuito para interagir com os filtros e analisar os gatilhos econômicos.
