# TPC3

## Autor:
- **Nome:** Vasco João Timóteo Gonçalves
- **Número:** A104527

## Resumo:

Em primeiro lugar, desenvolvi um conversor para transformar texto em formato Markdown para HTML. Este conversor utiliza expressões regulares para identificar e converter corretamente os elementos da sintaxe básica do Markdown, prestando especial atenção a elementos complexos como listas numeradas que requerem uma atenção especial.
O processamento dos elementos Markdown foi implementado através de uma função principal que trata sequencialmente diferentes padrões: cabeçalhos de diferentes níveis (H1, H2, H3), texto em negrito e itálico, links e imagens. Para estas operações, foram utilizadas expressões regulares específicas com grupos de captura, aproveitando a função re.sub() para realizar as substituições de forma precisa.
Foi adicionada uma interface de linha de comando que permite ao utilizador fornecer um ficheiro Markdown de entrada e, opcionalmente, especificar um ficheiro de saída HTML. O programa inclui verificação de existência do ficheiro e tratamento de exceções para lidar com potenciais erros durante a leitura e escrita de ficheiros.

## Lista de Resultados:

- [Resoluçao em Python](tpc3.py)
