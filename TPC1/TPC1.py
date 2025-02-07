def somador_on_off(l):
    i = 0
    onOff = 1
    valor = 0
    while i < len(l):  

        if i + 2 < len(l) and (l[i] == "o" or l[i]=="O"):
            if(l[i+1]== "f" or l[i+1]== "F") and (l[i+2]=="F" or l[i+2]=="f"):
                onOff = 0
                i = i+2
            elif(l[i+1]== "n" or l[i+1]== "N"):
                onOff = 1
                i = i+1       
        
        elif onOff == 1 and l[i] in "0123456789":
            num = 0
            while l[i] in "0123456789":
                num = num * 10 + int(l[i])
                i= i+1
            valor = valor + num
        elif (l[i]=="="):
            print(valor)
        i=i+1


def main():
   try:
       filename = input("Nome do ficheiro: ")
       with open(filename, 'r') as file:
           text = file.read()
           somador_on_off(text)
   except FileNotFoundError:
       print("Erro: Ficheiro não encontrado")
   except Exception as e:
       print(f"Erro: {e}")

if __name__ == "__main__":
   main()




