# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Simplemente Enlazada 
# ===========================================

# Clase Nodo
class Nodo:
	def __init__(self, data):
		self.data = data
		self.siguiente = None

# CLase Listas enlazada simple
class ListaSE:
	def __init__(self):
		self.cabeza = None
  
  	# Lista Vacia
	def vacio(self):
		if sel.cabeza == None:
      		print("Está vacia")
		else:
      		print("Lista no vacia")

	# Agregar al inicio
	def agregarInicio(self, data):
		nuevo_nodo = Nodo(data)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		else:
			nuevo_nodo.siguiente = self.cabeza
			self.cabeza = nuevo_nodo

	# Agregar en cualquier lugar indicado por index
	def agregarIndex(self, data, index):
		nuevo_nodo = Nodo(data)
		nodo_actual = self.cabeza
		posicion = 0
		if posicion == index:
			self.agregarInicio(data)
		else:
			while(nodo_actual != None and posicion+1 != index):
				posicion = posicion+1
				nodo_actual = nodo_actual.siguiente

			if nodo_actual != None:
				nuevo_nodo.siguiente = nodo_actual.siguiente
				nodo_actual.siguiente = nuevo_nodo
			else:
				print("Index no encontrado")

	# Agregar al Final
	def agregarFinal(self, data):
		nuevo_nodo = Nodo(data)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return

		nodo_actual = self.cabeza
		while(nodo_actual.siguiente):
			nodo_actual = nodo_actual.siguiente

		nodo_actual.siguiente = nuevo_nodo

	# Actualizar nodo
	def actualizarNodo(self, val, index):
		nodo_actual = self.cabeza
		posicion = 0
		if posicion == index:
			nodo_actual.data = val
		else:
			while(nodo_actual != None and posicion != index):
				posicion = posicion+1
				nodo_actual = nodo_actual.siguiente

			if nodo_actual != None:
				nodo_actual.data = val
			else:
				print("Elemento no encontrado")

	# Eliminar nodo inicio

	def eliminarInicio(self):
		if(self.cabeza == None):
			return

		self.cabeza = self.cabeza.siguiente

	# Eliminar último
	def eliminar_ultimo(self):

		if self.cabeza is None:
			return

		nodo_actual = self.cabeza
		while(nodo_actual.siguiente.siguiente):
			nodo_actual = nodo_actual.siguiente

		nodo_actual.siguiente = None

	# Eliminar nodo index
	def eliminar_index(self, index):
		if self.cabeza == None:
			return

		nodo_actual = self.cabeza
		posicion = 0
		if posicion == index:
			self.eliminarInicio()
		else:
			while(nodo_actual != None and posicion+1 != index):
				posicion = posicion+1
				nodo_actual = nodo_actual.siguiente

			if nodo_actual != None:
				nodo_actual.siguiente = nodo_actual.siguiente.siguiente
			else:
				print("Nodo no encontrado")

	# Tamaño de la lista
	def cantidadNodos(self):
		size = 0
		if(self.cabeza):
			nodo_actual = self.cabeza
			while(nodo_actual):
				size = size+1
				nodo_actual = nodo_actual.siguiente
			return size
		else:
			return 0

	# Imprimir Lista
	def imprimir(self):
		nodo_actual = self.cabeza
		while(nodo_actual):
			print(nodo_actual.data)
			nodo_actual = nodo_actual.siguiente
			
        