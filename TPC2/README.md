# TPC2

## Autor:
- **Nome:** Vasco João Timóteo Gonçalves
- **Número:** A104527

## Resumo:

Em primeiro desenvolvi um parser para processar ficheiros CSV contendo informações sobre obras musicais. Este parser utiliza expressões regulares para extrair corretamente os dados, dando atenção especial às descrições que podem estar entre aspas e conter caracteres problemáticos como quebras de linha e ponto e vírgula.
O processamento dos dados extraídos foi implementado através de funções específicas que: listam compositores de forma ordenada, calculam a distribuição de obras por período musical e agrupam os títulos das obras por período. Para estas operações, foram utilizadas estruturas de dados nativas do Python como dicionários, conjuntos e listas, aproveitando funções como sort() para ordenação.
Foi adicionada uma interface de menu que permite ao utilizador escolher quais análises deseja realizar.

## Lista de Resultados:

- [Resoluçao em Python](solucao.py)
- [Ficheiro csv](obras.csv)