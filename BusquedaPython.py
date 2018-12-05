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

def busquedaBinaria(self,unaLista,elemento):
        primero = 0
        ultimo = len(unaLista)-1
        while(primero <= ultimo):
            centro = int((primero + ultimo)/2)
            valorCentro = unaLista[centro]
            print ("Comparando "+str(elemento)+" Con "+str(unaLista[centro]))

            if elemento == valorCentro:
                return centro
            elif elemento < valorCentro:
                ultimo = centro - 1 #con el fin de desplazarnos hacia la izquierda
            else:
                primero = centro + 1 #con el fin de desplazarnos hacia la derecha
        return -1
            
class hash_table:
    def __init__(self):
        self.table = [None] * 127
    
    # Hash function
    def Hash_func(self, value):
        key = 0
        for i in range(0,len(value)):
            key += ord(value[i])
        return key % 127

    def Insert(self, value):
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            self.table[hash] = value
   
    def Search(self,value):
        hash = self.Hash_func(value);
        if self.table[hash] is None:
            return None
        else:
            print("Se encontro el elemento en")
            return hex(id(self.table[hash]))
  
    def Remove(self,value):
        hash = self.Hash_func(value);
        if self.table[hash] is None:
            print("No se encontro el elemento", value)
        else:
            print("Element with value", value, "deleted")
            self.table[hash] is None;
        
        
H = hash_table()
H.Insert("Alo")
H.Insert("Bou")
H.Insert("Col")

print(H.Search("Bou"))