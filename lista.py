from nodoLista import NodoLista
from evento import Evento
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
            nuevoNodo.anterior=self.ultimo
        self.ultimo=nuevoNodo

    def eliminar(self,pos):
        tmp=NodoLista("")
        tmp=self.primero
        cont=0
        while cont<pos and tmp!=None:
            tmp=tmp.siguiente
            cont+=1
        if pos==cont:
            if tmp.siguiente!=None and tmp.anterior!=None:
                tmp.anterior.siguiente=tmp.siguiente
                tmp.siguiente.anterio=tmp.anterior
            elif tmp.siguiente!=None:
                self.primero=tmp.siguiente
                tmp.siguiente.anterior=None
            elif tmp.anterior!=None:
                self.ultimo=tmp.anterior
                tmp.anterior.siguiente=None
            else:
                self.primero=None
                self.ultimo=None
            tmp.dato=None
            tmp=None

    def lenLista(self):
        if self.primero==None:
            return 0
        nodotmp=NodoLista("")
        nodotmp=self.primero
        cont=0
        while nodotmp!=None:
            cont+=1
            nodotmp=nodotmp.siguiente
        return cont

    def estaVacio(self):
        if self.lenLista()==0:
            return True
        return False

    def mostrarContenido(self):
        nodotmp=NodoLista("")
        nodotmp=self.primero
        cont=0
        if self.estaVacio():
            print("No hay eventos por mostar")
        else:
            print("-----        EVENTOS        -----\n")
            while nodotmp!=None:
                cont+=1
                print("Evento #",cont)
                print("\t Tipo: ",Evento.getTipo(nodotmp.dato))
                print("\t Descripcion: ",Evento.getDescripcion(nodotmp.dato))
                print("\t Prioridad: ",Evento.getPrioridad(nodotmp.dato))
                print("\t Hora limite: ",Evento.getHoraLimite(nodotmp.dato),"\n") 
                nodotmp=nodotmp.siguiente  