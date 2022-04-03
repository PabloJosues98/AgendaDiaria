from nodoLista import NodoLista
class Lista:
    def __init__(self):
        self.primero=None
        self.ultimo=None
    
    def agregar(self,dato):
        nuevoNodo=NodoLista(dato)
        if self.ultimo==None:
            self.primero=nuevoNodo
        else:
            self.ultimo.siguiente=nuevoNodo
            nuevoNodo.anterio=self.ultimo
        self.ultimo=nuevoNodo

    def eliminar(self,pos):
        tmp=NodoLista("")
        cont=0
        while pos<cont and tmp.siguiente!=None:
            tmp=tmp.siguiente
            cont+=1
        if pos==cont:
            if tmp.siguiente and tmp.anterio:
                tmp.anterio.siguiente=tmp.siguiente
                tmp.siguiente.anterior=tmp.anterio
                tmp=None
