from os import system
from lista import Lista
from evento import Evento

def crearEvento():
    while True:
        system("cls")
        print("-----        CREACION DE EVENTO         -----\n")
        print("1) Tarea")
        print("2) Proyecto")
        print("3) Pasa tiempo")
        print("4) Personalizado (puede nombrar su evento)")
        print("5) Retornar al Menu principal\n")
        try:
            opcion=int(input("Seleccione el tipo de evento que es: "))
            if opcion==4:
                tipo=str(input("Ingrese tipo: "))
                break
            elif opcion>0 and opcion<6:
                if opcion==1:tipo="Tarea"
                elif opcion==2:tipo="Proyecto"
                elif opcion==3:tipo="Pasa tiempo"
                if opcion==5:
                    menu()
                break
            else:
                print("valor fuera de rango")
        except:
            print("valor no valido")
            continue
    system("cls")
    print("-----        CREACION DE EVENTO         -----\n")
    descripcion=input("Ingrese una pequeña descripcion del evento: ")
    while True:
        system("cls")
        print("-----        CREACION DE EVENTO         -----\n")
        print("1) Ninguna")
        print("2) Alta")
        print("3) Alta/Media")
        print("4) Media")
        print("5) Media/Baja")
        print("6) Baja\n")
        try:
            opcion=int(input("Ingrese el valor de la priorida de la tarea: "))
            if opcion==1:prioridad="Ninguna"
            elif opcion==2:prioridad="Alta"
            elif opcion==3:prioridad="Alta/Media"
            elif opcion==4:prioridad="Media"
            elif opcion==5:prioridad="Media/Baja"
            elif opcion==6:prioridad="Baja"
            break
        except: 
            print("valor no valido")
            continue
    while True:
        system("cls")
        print("-----        CREACION DE EVENTO         -----\n")
        print("1) Si")
        print("2) No")
        try:
            opcion=int(input("Seleccione si desea agregar hora limite: "))
            if opcion==2:
                horaLimite=None
            else:
                while True:
                    hora=int(input("ingrese la hora (valores validos de 0-23): "))
                    if hora>=0 and hora<24:
                        break
                while True:
                    minutos=int(input("ingrese los minutos (valores validos de 0-59): "))
                    if minutos>=0 and minutos<60:
                        break
                horaLimite=str(hora)+":"+str(minutos)
            global misEventos
            misEventos.agregar(Evento(tipo,descripcion,prioridad,horaLimite))
            system("cls")
            print("-----        EVENTO CREADO CORRECTAMENTE         -----\n")
            print("Tipo: ",tipo)
            print("Descripcion: ",descripcion)
            print("Prioridad: ",prioridad)
            if horaLimite==None:
                print("Hora limite: No tiene")
            else:
                print("Hora limite: ",horaLimite)
            op=input("ingrese cualquier tecla para continuar: ")
            break
        except: 
            print("valor no valido")
            continue

def mostarEventos():
    global misEventos
    system("cls")
    misEventos.mostrarContenido()
    opcion=input("ingrese cualquier tecla para continuar: ")

def eliminarEvento():
    while True:
        system("cls")
        global misEventos
        misEventos.mostrarContenido()
        try:
            numOpciones=misEventos.lenLista()
            opcion=int(input("Ingrese el numero del evento que desea eliminar o ingrese ("+str(numOpciones+1)+") para salir: "))
            if opcion>0 and opcion<numOpciones+2:
                if opcion==numOpciones+1:
                    break
                misEventos.eliminar(opcion-1)
                system("cls")
                mostarEventos()
                break
        except:
            print("valor no valido")

def informacion():
    system("cls")
    print("-----        INFORMACION        -----\n")
    print("Esta es una aplicacion para llevar el control de los eventos del dia, en el menu principal se muestra las opciones que se pueden realiza:\n")
    print("Crear un evento: Te permite crear o agendar un evento, primero se selecciona el tipo de evento, luego una breve descripcion, seguido de su prioridad, por ultimo y opcional hora limite de la actividad (este programa no tiene un alarma, simplementen mostrara toda esa informacion de eventos en pantalla.)")
    print("Mostar eventos: En este apartado se mostraran todos los eventos que se crearon anteriormente, y si no los hay te mostrar un mensaje.")
    print("Eliminar un evento: Aqui puedes seleccionar el evento que hayas finalizado o desees eliminar de la lista.")
    print("Informacion del programa y el desarrollador: es la seccion actual de la cual puedes salir presionando cualquier tecla.")
    print("Terminar el programa: Permite que el programa se detenga por completo, Nota: al cerrarse se eliminara todos los datos guardados en la aplicacion.\n\n")
    print("-----        INFORMACION DEL DESARROLLADOR       -----\n")
    print("Nombre: Pablo Sosa")
    print("Cursando: Cuarto semestre de Ingenieria en Ciencias y Sistemas en la Universidad de San Carlos de Guatemala")
    print("Correo: pablojosues98@gmail.com\n")
    op=input("Ingresa cualquier tecla para retornar la menu principal: ")

def menu():
    while True:
        system("cls")
        print("-----        MENU        -----\n")
        print("1) Crear un evento")
        print("2) Mostar eventos")
        print("3) Eliminar un evento")
        print("4) Informacion del programa y el desarrollador")
        print("5) Terminar el programa\n")
        try:
            opcion=int(input("Ingrese el numero para realizar la accion: "))
            if opcion==1:
                crearEvento()
            elif opcion==2:
                mostarEventos()
            elif opcion==3:
                eliminarEvento()
            elif opcion==4:
                informacion()
            elif opcion==5:
                break
        except:
            continue
        
if __name__=="__main__":
    misEventos=Lista()
    menu()