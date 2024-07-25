from utilidades import numeros, letras

def automata_enteros(cadena):
    numero = numeros()

    tablaEnteros=[['A', '-','C'],
                  ['A', numero,'B,D'],
                  ['C', '-','M'],
                  ['C', numero,'B,D'],
                  ['M', '-','M'],
                  ['M', numero,'M'],
                  ['B,D', '-','M'],
                  ['B,D', numero,'B,D']]
    TablaC = []
    verificador = True #revisar que (x ϵ Σ)

    Σ=['-']   #Alfabeto de entrada
    for i in numero:
       Σ.append(i) 

    EI= 'A'
    EF= 'B,D'
    EA= EI
    
    cadenas=str(cadena)
    for caracter in cadenas:
        #print (caracter)
        if caracter in Σ:
            #print ("El carcacter pertenece al alfabeto")
            for f in tablaEnteros:
                if EA == f[0] and caracter in f[1]:
                    TablaC.append([EA,caracter,f[2]])  
                    EA=f[2]
                    # print ("Estado actual es : " + str(EA))
                    break
        else:
            # print("Cadena no pertenece al alfabeto")
            verificador = False
    
    if EA != EF:
        verificador=False
    return(verificador)
    
def automata_identificadores(cadena):
    letra = letras()
    numero = numeros()

    tablaIdentificadores=[['A', '_','FINAL'],
                  ['A', letra,'FINAL'],
                  ['A', numero ,'M'],
                  ['FINAL', '_','FINAL'],
                  ['FINAL', numero,'FINAL'],
                  ['FINAL', letra,'FINAL'],
                  ['M', numero,'M'],
                  ['M', '_','M'],
                  ['M', letra,'M']]
    TablaC = []
    verificador = True #revisar que (x ϵ Σ)

    Σ=['_']   #Alfabeto de entrada
    for i in numero:
       Σ.append(i) 

    for i in letra:
       Σ.append(i) 

    EI= 'A'
    EF= 'FINAL'
    EA= EI
    
    palabras=cadena.split()

    cadenas=str(cadena)
    for caracter in cadenas:
        # print (caracter)
        if caracter in Σ:
            # print ("El carcacter pertenece al alfabeto")
            for f in tablaIdentificadores:
                if EA == f[0] and caracter in f[1]:
                    TablaC.append([EA,caracter,f[2]])  
                    EA=f[2]
                    # print ("Estado actual es : " + str(EA))
                    break
        else:
            # print("Cadena no pertenece al alfabeto")
            verificador = False

    if EA != EF:
        verificador=False
    return(verificador)

def automata_reales(cadena):
    numero = numeros()
    exp=['E','e']
    tablaReales=[['A', numero,'C,E'],
                  ['A', '-','B'],
                  ['A', exp ,'Muerto'],
                  ['A', '.' ,'D,G'],
                  ['B', numero,'C,E'],
                  ['B', '-','Muerto'],
                  ['B', exp,'Muerto'],
                  ['B', '.','D,G'],
                  ['C,E', numero,'C,E'],
                  ['C,E', exp,'F,M'],
                  ['C,E', '.','D,G'],
                  ['C,E', '-','Muerto'],
                  ['D,G', '-','Muerto'],
                  ['D,G', exp,'Muerto'],
                  ['D,G', '.','Muerto'],
                  ['D,G', numero,'H,K,L,Ñ'],
                  ['F,M', numero,'J,N,P,Q'],
                  ['F,M', '-','I,O'],
                  ['F,M', '.','Muerto'],
                  ['F,M', exp,'Muerto'],
                  ['H,K,L,Ñ', numero,'H,K,L,Ñ'],
                  ['H,K,L,Ñ', exp,'F,M'],
                  ['H,K,L,Ñ', '.','Muerto'],
                  ['H,K,L,Ñ', '-','Muerto'],
                  ['J,N,P,Q', numero,'J,N,P,Q'],
                  ['J,N,P,Q', exp,'Muerto'],
                  ['J,N,P,Q', '.','Muerto'],
                  ['J,N,P,Q', '-','Muerto'],
                  ['I,O', '-','Muerto'],
                  ['I,O', exp,'Muerto'],
                  ['I,O', '.','Muerto'],
                  ['I,O', numero,'J,N,P,Q'],
                  ['Muerto', '-','Muerto'],
                  ['Muerto', exp,'Muerto'],
                  ['Muerto', '.','Muerto'],
                  ['Muerto', numero,'Muerto'],]
    TablaC = []
    verificador = True #revisar que (x ϵ Σ)

    Σ=['-','e','E','.']   #Alfabeto de entrada
    for i in numero:
       Σ.append(i) 

    EI= 'A'
    EF= ['J,N,P,Q','H,K,L,Ñ']
    EA= EI
    
    cadenas=str(cadena)
    for caracter in cadenas:
        # print (caracter)
        if caracter in Σ:
            # print ("El carcacter pertenece al alfabeto")
            for f in tablaReales:
                if EA == f[0] and caracter in f[1]:
                    TablaC.append([EA,caracter,f[2]])  
                    EA=f[2]
                    # print ("Estado actual es : " + str(EA))
                    break
        else:
            # print("Cadena no pertenece al alfabeto")
            verificador = False
    
    if not(EA in EF):
        verificador=False
    return(verificador)
