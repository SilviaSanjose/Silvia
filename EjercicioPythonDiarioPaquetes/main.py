'''
INDICE DE TODOS LOS EJERCICIOS
'''

from juegos import reinodelDragon, capitalEjer4, rimasEjer3, MasterMindEjer2,\
    sorteoBolas

print("""LISTA DE EJERCICIOS (pythondiario.com)
    Parte 3: 
        1. El Reino del Dragón
        2. Master Mind
        3. Rima de palabras
        4. Capital + intereses
    Parte 4: 
        5. Sorteo bolas descuento
    
    """)

ejercicio = int(input("¿Qué ejercicio quieres ver? "))

if ejercicio == 1:
    reinodelDragon.reinoDelDragon()
elif ejercicio ==2:
    MasterMindEjer2.jugarMasterMind()
elif ejercicio ==3:
    rimasEjer3.rimarPalabras()
elif ejercicio == 4:
    capitalEjer4.calcularCapital()
elif ejercicio ==5:
    sorteoBolas.sorteoBolasDescuento()
