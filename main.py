from automatas import automata_enteros, automata_identificadores, automata_reales
import re

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            text_corregido= contenido.replace('(',' ( ').replace(')',' ) ').replace('=',' = ').replace(',',' , ').replace(':',' : ').replace(';',' ; ').replace('+',' + ').replace('>',' > ').replace('<',' < ')
            text_separado=text_corregido.split()
            print(text_separado)
            analizar(text_separado)

    except Exception as e:
        print(f"Error al leer el archivo: {e}")

palabrasReservadas=['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
                         'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 
                         'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while','with','yield','print']

def analizar(contenido):
    for palabra in contenido:

        if palabra in palabrasReservadas:
            print(f'{palabra}: PALABRA RESERVADA')
            
        elif automata_identificadores(palabra):
            print(f'{palabra}: IDENTIFICADOR')

        elif automata_enteros(palabra):
            print(f'{palabra}: NUMERO ENTERO')
            
        elif automata_reales(palabra):
            print(f'{palabra}: NUMERO REAL')    
    
leer_archivo('FINAL-PARADIGMAS\Test.py')