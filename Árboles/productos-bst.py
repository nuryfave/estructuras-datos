class NodoProducto:
    def __init__(self, id_producto, precio):
        self.id_producto = id_producto
        self.precio = precio
        self.izquierdo = None
        self.derecho = None

class InventarioBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, id_p, precio):
        if self.raiz is None:
            self.raiz = NodoProducto(id_p, precio)
        else:
            self._insertar_recursivo(self.raiz, id_p, precio)

    def _insertar_recursivo(self, nodo_actual, id_p, precio):
       
        if precio <= nodo_actual.precio:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoProducto(id_p, precio)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, id_p, precio)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoProducto(id_p, precio)
            else:
                self._insertar_recursivo(nodo_actual.derecho, id_p, precio)

    def buscar_rango(self, nodo, precio_min, precio_max, resultados=None):
        if resultados is None:
            resultados = []
        
        if nodo is None:
            return resultados

        if precio_min < nodo.precio:
            self.buscar_rango(nodo.izquierdo, precio_min, precio_max, resultados)
        
        if precio_min <= nodo.precio <= precio_max:
            resultados.append(nodo.id_producto)
        
        if precio_min > nodo.precio:
            self.buscar_rango(nodo.derecho, precio_min, precio_max, resultados)

        return resultados

# Ejemplo de uso 
inv = InventarioBST()
productos = [("Laptop", 1200), ("Mouse", 25), ("Monitor", 300), ("Teclado", 25)]
for p in productos:
    inv.insertar(p[0], p[1])

# El usuario busca productos entre 20 y 50 USD
print(f"Productos en rango: {inv.buscar_rango(inv.raiz, 20, 50)}")
