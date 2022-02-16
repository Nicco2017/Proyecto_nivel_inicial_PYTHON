Este programa esta confeccionado para el control de trazabilidad de una pieza nombrada por un codigo, donde el inicio de su cadena 
se obtienen desde una orden de compra donde en ese mismo se representan todos los pedidos de piezas con sus cantidades, 
ademas tambien se registran las fechas de emision del documento y la fecha de entrega estimada para cada item.
El programa tiene de nombre "PROYECTO.py", donde al inicio del mismo despues del mensaje de bienvenida te pide que digites el
usuario, (PROGRAMADOR, CORTE, PLEGADORA Y ALMACEN). 
Al iniciar como programador tiene las opciones de cargar item nuevos, a partir de la orden de compra que le han enviado, o de 
cargar los reportes de corte y enlazar la o las piezas que comprenden en ese reporte, donde se introduce la cantidad emitida a corte
junto con la hora y fecha que se emitio ese reporte.
Si ingresamos como CORTE, PLEGADORA o ALMACEN, te pide el programa que escanees el codigo QR para leer el codigo de busqueda de la pieza, que en este
caso es la union del codigo propio de la pieza junto con el numero de orden de compra donde esta registrado separado por un guion (-), 
una vez escaneado recorre la base de datos, ubica la fila y ahi nos pide cargar la cantidad de piezas que se han procesado, junto
con la hora y fecha del momento de la carga.
Una vez finalizada la carga nos permite cerrar el mismo.
