class Evento:
    def __init__(self,tipo,descripcion,prioridad,horaLimite):
        self.tipo=str(tipo)
        self.prioridad=str(prioridad)
        self.descripcion=str(descripcion)
        self.horaLimite=horaLimite

    def getTipo(self):
        return self.tipo

    def getPrioridad(self):
        return self.prioridad

    def getDescripcion(self):
        return self.descripcion

    def getHoraLimite(self):
        if self.horaLimite==None:
            return "No tiene"
        return self.horaLimite