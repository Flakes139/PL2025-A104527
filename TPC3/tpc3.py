import re
import sys
import os

def convert_markdown_to_html(markdown_text):
    """
    Converte texto em formato Markdown para HTML.
    Suporta: cabeçalhos, negrito, itálico, listas numeradas, links e imagens.
    """
    # Converter o texto linha por linha para processar cabeçalhos e listas
    lines = markdown_text.split('\n')
    
    # Verificar se há uma lista numerada
    i = 0
    while i < len(lines):
        if re.match(r'^\d+\.\s+', lines[i]):
            # Encontrou o início de uma lista numerada
            list_items = []
            
            # Continuar coletando itens enquanto eles seguirem o padrão
            while i < len(lines) and re.match(r'^\d+\.\s+', lines[i]):
                # Remover o número e o ponto, preservando apenas o conteúdo
                content = re.sub(r'^\d+\.\s+', '', lines[i])
                list_items.append(f"<li>{content}</li>")
                i += 1
            
            # Substituir os itens originais pela lista formatada
            list_html = "<ol>\n" + "\n".join(list_items) + "\n</ol>"
            
            # Remover as linhas originais da lista
            del lines[i-len(list_items):i]
            
            # Inserir o HTML da lista no lugar
            lines.insert(i-len(list_items), list_html)
            
            # Ajustar o índice
            i = i - len(list_items) + 1
        else:
            i += 1
    
    # Processar cabeçalhos
    for i in range(len(lines)):
        lines[i] = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', lines[i])
        lines[i] = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', lines[i])
        lines[i] = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', lines[i])
    
    # Juntar as linhas novamente
    html_text = '\n'.join(lines)
    
    # Processar texto em negrito
    html_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html_text)
    
    # Processar texto em itálico
    html_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', html_text)
    
    # Processar links
    html_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html_text)
    
    # Processar imagens
    html_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', html_text)
    
    return html_text


def main():
    # Verificar se um arquivo foi fornecido como argumento
    if len(sys.argv) < 2:
        print("Uso: python markdown_converter.py arquivo.md [arquivo_saida.html]")
        print("Se o arquivo de saída não for especificado, o HTML será impresso no console.")
        return
    
    # Obter o caminho do arquivo de entrada
    input_file = sys.argv[1]
    
    # Verificar se o arquivo existe
    if not os.path.exists(input_file):
        print(f"Erro: O arquivo '{input_file}' não foi encontrado.")
        return
    
    try:
        # Ler o conteúdo do arquivo Markdown
        with open(input_file, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        
        # Converter para HTML
        html_content = convert_markdown_to_html(markdown_content)
        
        # Determinar a saída
        if len(sys.argv) > 2:
            # Se foi fornecido um arquivo de saída, escrever o HTML nele
            output_file = sys.argv[2]
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(html_content)
            print(f"HTML gerado com sucesso no arquivo '{output_file}'")
        else:
            # Caso contrário, imprimir o HTML no console
            print(html_content)
            
    except Exception as e:
        print(f"Erro ao processar o arquivo: {str(e)}")


# Executar o programa principal se for chamado diretamente
if __name__ == "__main__":
    main()