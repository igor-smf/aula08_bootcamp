from etl import pipeline_calcular_kpi_de_de_vendas_consolidado

pasta: str = 'data'
formato_saida: list = ['csv', 'parquet']
pipeline_calcular_kpi_de_de_vendas_consolidado(pasta, formato_saida)
