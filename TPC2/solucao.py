import re
import sys

def ler_dataset_com_regex(arquivo):
    """
    Função que lê o dataset utilizando expressões regulares
    """
    # Ler o conteúdo completo do arquivo
    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    # Separar cabeçalho do resto do conteúdo
    partes = conteudo.split('\n', 1)
    cabecalhos = partes[0].strip().split(';')
    conteudo_dados = partes[1] if len(partes) > 1 else ""
    
    # Padrão regex para cada registro completo
    # Captura cada linha: nome, descrição (com ou sem aspas), ano, período, compositor, duração e id
    padrao_registro = re.compile(
        r'([^;\n]+);' # nome: qualquer coisa até o primeiro ;
        r'(?:"((?:[^"]|""|\n|"[^"]*")+?)"|([^;\n]+));' # descrição: entre aspas (pode ter aspas internas, quebras de linha) OU sem aspas
        r'([^;\n]+);' # anoCriacao
        r'([^;\n]+);' # periodo
        r'([^;\n]+);' # compositor
        r'([^;\n]+);' # duracao
        r'([^;\n]+)' # _id
    , re.DOTALL
    )
    
    obras = []
    for match in padrao_registro.finditer(conteudo_dados):
        # Captura todos os grupos
        nome = match.group(1).strip()
        # A descrição pode estar no grupo 2 (com aspas) ou grupo 3 (sem aspas)
        desc = match.group(2) if match.group(2) is not None else match.group(3)
        desc = desc.strip() if desc else ""
        # Dados restantes
        ano_criacao = match.group(4).strip()
        periodo = match.group(5).strip()
        compositor = match.group(6).strip()
        duracao = match.group(7).strip()
        id_obra = match.group(8).strip()
        
        # Criar dicionário para a obra atual
        obra = {
            cabecalhos[0]: nome,
            cabecalhos[1]: desc,
            cabecalhos[2]: ano_criacao,
            cabecalhos[3]: periodo,
            cabecalhos[4]: compositor,
            cabecalhos[5]: duracao,
            cabecalhos[6]: id_obra
        }
        obras.append(obra)
    
    return obras

def listar_compositores(obras):
    compositores = set()
    for obra in obras:
        if 'compositor' in obra:
            compositores.add(obra['compositor'])
    return sorted(list(compositores))

def distribuicao_por_periodo(obras):
    distribuicao = {}
    for obra in obras:
        if 'periodo' in obra:
            periodo = obra['periodo']
            if periodo in distribuicao:
                distribuicao[periodo] += 1
            else:
                distribuicao[periodo] = 1
    return distribuicao

def titulos_por_periodo(obras):
    """
    Agrupa os títulos das obras por período e retorna um dicionário onde
    as chaves são os períodos e os valores são listas ordenadas de títulos
    """
    titulos_por_periodo = {}
    for obra in obras:
        if 'periodo' in obra and 'nome' in obra:
            periodo = obra['periodo']
            titulo = obra['nome']
            
            if periodo not in titulos_por_periodo:
                titulos_por_periodo[periodo] = []
                
            titulos_por_periodo[periodo].append(titulo)
    
    # Ordenar os títulos dentro de cada período
    for periodo in titulos_por_periodo:
        titulos_por_periodo[periodo].sort()
        
    return titulos_por_periodo

def mostrar_menu():
    print("\n===== MENU =====")
    print("1. Listar compositores ordenados")
    print("2. Mostrar distribuição por período")
    print("3. Listar títulos por período")
    print("4. Executar todas as opções")
    print("0. Sair")
    print("================")
    
    try:
        opcao = int(input("Escolha uma opção: "))
        return opcao
    except ValueError:
        print("Erro: Digite um número válido.")
        return mostrar_menu()



def main():
    # Verificar argumentos da linha de comando
    if len(sys.argv) != 2:
        arquivo = "obras.csv"
    else:
        arquivo = sys.argv[1]
    
    # Ler dados do arquivo
    try:
        obras = ler_dataset_com_regex(arquivo)
        print(f"Dados carregados com sucesso. {len(obras)} obras encontradas.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return
    
    while True:
        opcao = mostrar_menu()
        
        if opcao == 0:
            print("Encerrando programa...")
            break
            
        elif opcao == 1:
            # Listar compositores ordenados
            compositores = listar_compositores(obras)
            print("\n== Compositores ordenados ==")
            for compositor in compositores:
                print(compositor)
                
        elif opcao == 2:
            # Mostrar distribuição por período
            distribuicao = distribuicao_por_periodo(obras)
            print("\n== Distribuição por período ==")
            for periodo, contagem in distribuicao.items():
                print(f"{periodo}: {contagem}")
                
        elif opcao == 3:
            # Listar títulos por período
            titulos = titulos_por_periodo(obras)
            print("\n== Títulos por período ==")
            for periodo, lista_titulos in titulos.items():
                print(f"{periodo}:")
                for titulo in lista_titulos:
                    print(f"  {titulo}")
                    
        elif opcao == 4:
            # Executar todas as opções
            compositores = listar_compositores(obras)
            distribuicao = distribuicao_por_periodo(obras)
            titulos = titulos_por_periodo(obras)
            
            print("\n== Compositores ordenados ==")
            for compositor in compositores:
                print(compositor)
                
            print("\n== Distribuição por período ==")
            for periodo, contagem in distribuicao.items():
                print(f"{periodo}: {contagem}")
                
            print("\n== Títulos por período ==")
            for periodo, lista_titulos in titulos.items():
                print(f"{periodo}:")
                for titulo in lista_titulos:
                    print(f"  {titulo}")
                    
        else:
            print("Opção inválida. Por favor, escolha novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()