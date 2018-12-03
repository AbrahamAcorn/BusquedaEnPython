def busquedaSecuencial(unaLista, datoBuscar):
    pos = 0
    encontrado = False
    
    while pos <len(unaLista) and not encontrado:
        if unaLista[pos] == datoBuscar:
            encontrado = True
        else:
            pos = pos+1
    return encontrado


listaPrueba = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(busquedaSecuencial(listaPrueba, 3))
print(busquedaSecuencial(listaPrueba, 13))

def busquedaBinaria(lista,elemento):
    primero=0
    ultimo=len(lista)-1
    while(primero<=ultimo):
        centro=int((primero+ultimo)/2)
        valorcentro=lista[centro]
        
        if elemento==valorcentro:
            return centro
        elif elemento<valorcentro:
            ultimo=centro-1
        else:
            primero=centro+1
    return -1
        
            
    