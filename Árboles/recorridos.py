class Nodo:
   
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


class ArbolBinario:
   
    def __init__(self, raiz):
        self.raiz = raiz

    
    def recorrer_preorden(self):
        print("Preorden: ", end='')
        self._preorden(self.raiz)
        print()


    def _preorden(self, nodo):
        if nodo:    
            print(nodo.valor, end=' ')
            self._preorden(nodo.der)
            self._preorden(nodo.izq)

    
    def recorrer_inorden(self):       
        print("Inorden:  ", end='')
        self._inorden(self.raiz)
        print()


    def _inorden(self, nodo):       
        if nodo:
            print(nodo.valor, end=' ')
            self._inorden(nodo.izq)
            self._inorden(nodo.der)

   
    def recorrer_postorden(self):
        print("Postorden:", end='')
        self._postorden(self.raiz)
        print()

    def _postorden(self, nodo):
        if nodo:
            self._postorden(nodo.izq)
            print(nodo.valor, end=' ')
            self._postorden(nodo.der)

    def recorrer_por_niveles(self):
        print("Niveles:  ", end='')
        if not self.raiz:
            print()
            return

        estructura = [self.raiz]

        while estructura:
            
            nodo_actual = estructura.pop() 
            print(nodo_actual.valor, end=' ')

            if nodo_actual.izq:
                estructura.append(nodo_actual.izq)
            if nodo_actual.der:
                estructura.append(nodo_actual.der)
        
        print()

