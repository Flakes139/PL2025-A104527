import sys
def somador_on_off(l):
    i = 0
    onOff = 1
    valor = 0
    texto_atual = ""
    saida = []
    
    while i < len(l):
        if i + 2 < len(l) and (l[i] == "o" or l[i]=="O"):
            if(l[i+1]== "f" or l[i+1]== "F") and (l[i+2]=="F" or l[i+2]=="f"):
                onOff = 0
                texto_atual += l[i:i+3]
                i = i+3
                continue
            elif(l[i+1]== "n" or l[i+1]== "N"):
                onOff = 1
                texto_atual += l[i:i+2]
                i = i+2
                continue
        elif onOff == 1 and l[i] in "0123456789":
            num = 0
            while i < len(l) and l[i] in "0123456789":
                num = num * 10 + int(l[i])
                texto_atual += l[i]
                i= i+1
            valor = valor + num
            continue
        elif l[i]=="=":
            texto_atual += "="
            saida.append(texto_atual)
            saida.append(f">> {valor}")
            texto_atual = ""
            i=i+1
            continue
        texto_atual += l[i]
        i += 1
    
    if texto_atual:
        saida.append(texto_atual)
    saida.append(f">> {valor}")
    return "\n".join(saida)

def main():
    try:
        text = sys.stdin.read()
        if text.endswith('\n'):
            text = text[:-1]
        resultado = somador_on_off(text)
        print(resultado)
    except Exception as e:
        print(f"Erro: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()