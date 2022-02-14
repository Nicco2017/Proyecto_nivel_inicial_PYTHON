print('Sistema de gestion de produccion')

from ast import Return
from asyncore import write
import csv
from datetime import datetime
from distutils.fancy_getopt import wrap_text
from email import header
from operator import truediv
from pickle import TRUE
from tkinter.tix import COLUMN
from wsgiref import headers
from xmlrpc.client import DateTime

def agregar_item():
    header = ['codigo_busqueda','codigo','orden_compra','cant_orden_compra','fecha_emision','fecha_pactada','nombre_reporte','fecha_reporte','hora_reporte','cant_reporte','material','destino','fecha_corte','hora_corte','cant_corte','fecha_pliegue','hora_pliegue','cant_pliegue','fecha_almacen','hora_almacen','cant_almacen']
    
    codi = str(input('Ingrese el codigo de pieza:\n')).upper()
    orden = str(input('Ingrese el numero de orden de compra:\n'))
    cantidad = int(input('Ingrese la cantidad solicitada:\n'))
    fecha_emision = input('Ingrese la fecha de emision de la orden de compra:\n')
    fecha_pactada = input('Ingrese la fecha de entrega estimada:\n')

    with open('BASE_DE_DATOS.csv', 'a', newline = '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames= header)
       
        fila_agregar = {}
        fila_agregar['codigo_busqueda'] = codi + '-' + orden
        fila_agregar['codigo'] = codi 
        fila_agregar['orden_compra'] = orden
        fila_agregar['cant_orden_compra'] = cantidad
        fila_agregar['fecha_emision'] = fecha_emision
        fila_agregar['fecha_pactada'] = fecha_pactada

        #writer.writeheader()
        writer.writerow(fila_agregar)

        csvfile.close

    seguir_cargando = input('Ingresar ''SI'', si desea continuar cargando items, o ingrese ''NO'' para volver al inicio:\n')
    if seguir_cargando == 'si':
        return agregar_item()
    elif seguir_cargando == 'no':
        return selecciona_usuario()

def crear_reporte():
    def carga_datos_reporte():
        piezas_incl = str(input('Ingrese el codigo de pieza:\n')).upper()
        cant_incl = int(input('Ingrese la cantidad programada:\n'))
        fecha_emite_reporte = datetime.now()
        fecha_emite_reporte = fecha_emite_reporte.strftime('%d/%m/%Y')
        hora_emite_reporte = datetime.now()
        hora_emite_reporte = hora_emite_reporte.strftime('%H:%M:%S')

        while True:
            print('Ingrese el espesor de material:\n\
        Digite "0" para "AI AISI 430 BA 1mm":\n\
        Digite "1" para "AI AISI 430 BA 1/8":\n\
        Digite "2" para "AI AISI 430 BA 2,5mm":\n\
        Digite "3" para "AI AISI 430 BA 3mm":\n\
        Digite "4" para "CHAPA SAE 1010 - N°18":\n\
        Digite "5" para "CHAPA SAE 1010 - N°16":\n\
        Digite "6" para "CHAPA SAE 1010 - N°14":\n\
        Digite "7" para "CHAPA SAE 1010 - N°12":\n\
        Digite "8" para "CHAPA SAE 1010 - 1/8":\n\
        Digite "9" para "CHAPA SAE 1010 - 1/8" SM":\n\
        Digite "10" para "CHAPA SAE 1010 - 3/16":\n\
        Digite "11" para "CHAPA SAE 1010 - 1/4":\n\
        Digite "12" para "CHAPA SAE 1010 - 5/16":\n\
        Digite "13" para "CHAPA SAE 1010 - 3/8":\n\
        Digite "14" para "CHAPA SAE 1010 - 1/2":\n\
        Digite "15" para "CHAPA SAE 1010 - 5/8":\n\
        Digite "16" para "CHAPA SAE 1010 - 3/4":\n')

            material_pieza = input()    
            if material_pieza == '0':
                material_pieza = 'AI AISI 430 BA 1mm'
                break
            elif material_pieza == '1':
                material_pieza = 'AI AISI 430 BA 1/8'
                break
            elif material_pieza == '2':
                material_pieza = 'AI AISI 430 BA 2,5mm'
                break
            elif material_pieza == '3':
                material_pieza = 'AI AISI 430 BA 3mm'
                break
            elif material_pieza == '4':
                material_pieza = 'CHAPA SAE 1010 - N°18'
                break
            elif material_pieza == '5':
                material_pieza = 'CHAPA SAE 1010 - N°16'
                break
            elif material_pieza == '6':
                material_pieza = 'CHAPA SAE 1010 - N°14'
                break
            elif material_pieza == '7':
                material_pieza = 'CHAPA SAE 1010 - N°12'
                break
            elif material_pieza == '8':
                material_pieza = 'CHAPA SAE 1010 - 1/8'
                break
            elif material_pieza == '9':
                material_pieza = 'CHAPA SAE 1010 - 1/8'' SM'
                break
            elif material_pieza == '10':
                material_pieza = 'CHAPA SAE 1010 - 3/16'''
                break
            elif material_pieza == '11':
                material_pieza = 'CHAPA SAE 1010 - 1/4'''
                break
            elif material_pieza == '12':
                material_pieza = 'CHAPA SAE 1010 - 5/16'''
                break
            elif material_pieza == '13':
                material_pieza = 'CHAPA SAE 1010 - 3/8'''
                break
            elif material_pieza == '14':
                material_pieza = 'CHAPA SAE 1010 - 1/2'''
                break
            elif material_pieza == '15':
                material_pieza = 'CHAPA SAE 1010 - 5/8'''
                break
            elif material_pieza == '16':
                material_pieza = 'CHAPA SAE 1010 - 3/4'''
                break
            else:
                print('Opcion incorrecta, ingrese la opcion nuevamente')

        while True:
            print('Seleccione el destino del puesto de procesamiento de la pieza seleccionada')
            destino_pieza = str(input('Digite "P" para "PLEGADORA o "A" para "ALMACEN":\n')).upper()
            if destino_pieza == 'P':
                destino_pieza = 'PLEGADORA'
                break
            elif destino_pieza == 'A':
                destino_pieza = 'ALMACEN'
                break
            else:
                print('Entrada incorrecta, digite nuevamente')

        with open('BASE_DE_DATOS.csv', 'r') as archivo:
            data = list(csv.DictReader(archivo))
            
            for fila in data:
                for titulo, valor_celda in fila.items():
                    if titulo == 'codigo' and valor_celda == piezas_incl:
                        fila['nombre_reporte'] = reporte
                        fila['fecha_reporte'] = fecha_emite_reporte
                        fila['hora_reporte'] = hora_emite_reporte
                        fila['cant_reporte'] = cant_incl
                        fila['material'] = material_pieza
                        fila['destino'] = destino_pieza
                        
            archivo.close()

        csvfile = open('BASE_DE_DATOS.csv', 'w', newline = '') 
        header = ['codigo_busqueda','codigo','orden_compra','cant_orden_compra','fecha_emision','fecha_pactada','nombre_reporte','fecha_reporte','hora_reporte','cant_reporte','material','destino','fecha_corte','hora_corte','cant_corte','fecha_pliegue','hora_pliegue','cant_pliegue','fecha_almacen','hora_almacen','cant_almacen']
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)   
        csvfile.close()    

    reporte = str(input('Ingrese el nombre de reporte generado:\n')).upper()
    return carga_datos_reporte()
    
def agregar_corte():

    header = ['codigo_busqueda','codigo','orden_compra','cant_orden_compra','fecha_emision','fecha_pactada','nombre_reporte','fecha_reporte','hora_reporte','cant_reporte','material','destino','fecha_corte','hora_corte','cant_corte','fecha_pliegue','hora_pliegue','cant_pliegue','fecha_almacen','hora_almacen','cant_almacen']
    codi_escan = str(input('Escanee el codigo QR que figura en la etiqueta:\n')).upper()
    cant_cortada = int(input('Ingrese la cantidad procesada:\n'))
    fecha_corte = datetime.now()
    fecha_corte = fecha_corte.strftime('%d/%m/%Y')
    hora_corte = datetime.now()
    hora_corte = hora_corte.strftime('%H:%M:%S')

    with open('BASE_DE_DATOS.csv', 'r') as archivo:
            data = list(csv.DictReader(archivo))
            
            for fila in data:
                for titulo, valor_celda in fila.items():
                    if titulo == 'codigo_busqueda' and valor_celda == codi_escan:
                        fila['fecha_corte'] = fecha_corte
                        fila['hora_corte'] = hora_corte
                        fila['cant_corte'] = cant_cortada
                        
            archivo.close()

    csvfile = open('BASE_DE_DATOS.csv', 'w', newline = '') 
    header = ['codigo_busqueda','codigo','orden_compra','cant_orden_compra','fecha_emision','fecha_pactada','nombre_reporte','fecha_reporte','hora_reporte','cant_reporte','material','destino','fecha_corte','hora_corte','cant_corte','fecha_pliegue','hora_pliegue','cant_pliegue','fecha_almacen','hora_almacen','cant_almacen']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)   
    csvfile.close()    

def agregar_plegadora():

    header = ['codigo_busqueda','codigo','orden_compra','cant_orden_compra','fecha_emision','fecha_pactada','nombre_reporte','fecha_reporte','hora_reporte','cant_reporte','material','destino','fecha_corte','hora_corte','cant_corte','fecha_pliegue','hora_pliegue','cant_pliegue','fecha_almacen','hora_almacen','cant_almacen']
    codi_escan = str(input('Escanee el codigo QR que figura en la etiqueta:\n')).upper()
    cant_plegada = int(input('Ingrese la cantidad procesada:\n'))
    fecha_pliegue = datetime.now()
    fecha_pliegue = fecha_pliegue.strftime('%d/%m/%Y')
    hora_pliegue = datetime.now()
    hora_pliegue = hora_pliegue.strftime('%H:%M:%S')

    with open('BASE_DE_DATOS.csv', 'r') as archivo:
            data = list(csv.DictReader(archivo))
            
            for fila in data:
                for titulo, valor_celda in fila.items():
                    if titulo == 'codigo_busqueda' and valor_celda == codi_escan:
                        fila['fecha_pliegue'] = fecha_pliegue
                        fila['hora_pliegue'] = hora_pliegue
                        fila['cant_pliegue'] = cant_plegada
                        
            archivo.close()

    csvfile = open('BASE_DE_DATOS.csv', 'w', newline = '') 
    header = ['codigo_busqueda','codigo','orden_compra','cant_orden_compra','fecha_emision','fecha_pactada','nombre_reporte','fecha_reporte','hora_reporte','cant_reporte','material','destino','fecha_corte','hora_corte','cant_corte','fecha_pliegue','hora_pliegue','cant_pliegue','fecha_almacen','hora_almacen','cant_almacen']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)   
    csvfile.close()    

def agregar_almacen():

    header = ['codigo_busqueda','codigo','orden_compra','cant_orden_compra','fecha_emision','fecha_pactada','nombre_reporte','fecha_reporte','hora_reporte','cant_reporte','material','destino','fecha_corte','hora_corte','cant_corte','fecha_pliegue','hora_pliegue','cant_pliegue','fecha_almacen','hora_almacen','cant_almacen']
    codi_escan = str(input('Escanee el codigo QR que figura en la etiqueta:\n')).upper()
    cant_recibida = int(input('Ingrese la cantidad recibida:\n'))
    fecha_almacen = datetime.now()
    fecha_almacen = fecha_almacen.strftime('%d/%m/%Y')
    hora_almacen = datetime.now()
    hora_almacen = hora_almacen.strftime('%H:%M:%S')

    with open('BASE_DE_DATOS.csv', 'r') as archivo:
            data = list(csv.DictReader(archivo))
            
            for fila in data:
                for titulo, valor_celda in fila.items():
                    if titulo == 'codigo_busqueda' and valor_celda == codi_escan:
                        fila['fecha_almacen'] = fecha_almacen
                        fila['hora_almacen'] = hora_almacen
                        fila['cant_almacen'] = cant_recibida
                        
            archivo.close()

    csvfile = open('BASE_DE_DATOS.csv', 'w', newline = '') 
    header = ['codigo_busqueda','codigo','orden_compra','cant_orden_compra','fecha_emision','fecha_pactada','nombre_reporte','fecha_reporte','hora_reporte','cant_reporte','material','destino','fecha_corte','hora_corte','cant_corte','fecha_pliegue','hora_pliegue','cant_pliegue','fecha_almacen','hora_almacen','cant_almacen']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)   
    csvfile.close()   

def selecciona_usuario():
    usuario = str(input('Ingresar nombre de USUARIO, o "EXIT" para cerrar el programa:\n'))
    while True:
        if usuario == 'programador':
            print('Seleccionar opcion para continuar')
            elegir = str(input('Ingrese "NUEVO" para INGRESAR NUEVOS PEDIDOS o "CREAR" para CREAR REPORTE DE CORTE:\n'))
            while True:
                if elegir == 'nuevo':
                    agregar_item()
                elif elegir == 'crear':
                    crear_reporte()
                    elegir_programa = str(input('Ingrese "R" para INGRESAR NUEVOS REPORTES o "M" para volver al MENU PRICIPAL:\n')).upper()
                    if elegir_programa == 'R':
                        return crear_reporte()
                    elif elegir_programa == 'M':
                        return selecciona_usuario()
        elif usuario == 'corte':
                    agregar_corte()
                    print('¿Continuar cargando datos? SI/NO:\n')
                    cont = input()
                    if cont == 'si':
                        return agregar_corte()
                    elif cont == 'no':
                        return selecciona_usuario()
        elif usuario == 'plegadora':
                    agregar_plegadora()
                    print('¿Continuar cargando datos? SI/NO:\n')
                    cont = input()
                    if cont == 'si':
                        return agregar_plegadora()
                    elif cont == 'no':
                        return selecciona_usuario()
        elif usuario == 'almacen':
                    agregar_almacen()
                    print('¿Continuar cargando datos? SI/NO:\n')
                    cont = input()
                    if cont == 'si':
                        return agregar_almacen()
                    elif cont == 'no':
                        return selecciona_usuario()
        elif usuario == 'exit':
            cerr = input('¿Esta seguro que desea cerrar el programa? SI/NO:\n')
            if cerr == 'si':
                pregunta_cerrar ()
            elif cerr == 'no':
                return selecciona_usuario()
        else:
            print('Usuario incorrecto, ingrese nuevamente:\n')
            return selecciona_usuario()
        
def pregunta_cerrar ():
    while True:
        print('¿Desea continuar? - SI/NO:\n')
        salir = input()
        if salir == 'si':
            return selecciona_usuario()
        elif salir == 'no':
            cerrar = str(input('Esta por salir del programa, ¿Esta seguro?, selecciona "S" para cerrar y "N" para volver al menu principal:\n'))
            if cerrar == 's':
                exit()
            elif cerrar == 'n':
                return  selecciona_usuario()

selecciona_usuario()