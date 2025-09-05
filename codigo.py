# Sistema de control de parqueadero Parking Center S.A.S.



# 1. Importación de librerías

from datetime import datetime  
# datetime nos permite trabajar con fechas y horas exactas.
# datetime.now() devuelve la fecha y hora actuales.
# Se usa para registrar hora de ingreso y salida de vehículos.


# 2. Declaración de listas,etc

vehiculos = []  
# Lista que almacenará los vehículos actualmente en el parqueadero.
# Cada elemento es una tupla: (placa, tipo, hora_entrada)

historial = []  
# Lista que almacenará los vehículos que ya salieron del parqueadero.
# Cada elemento es una tupla: (placa, tipo, hora_entrada, hora_salida, valor_pagado)

tarifas = {     
    "moto": 1000,     # Valor por hora para motos
    "carro": 2000,    # Valor por hora para carros
    "camioneta": 2500 # Valor por hora para camionetas
}#ademas cabe aclarar que si el vehiculos se queda 30 minutos, se le cobrara una hora completa
# Diccionario que permite calcular el valor a pagar según el tipo de vehículo.

opc = 0  
# Variable para almacenar la opción elegida por el usuario en el menú principal.


# 3. Bucle principal del sistema

while opc != 5:  
    # Este bucle se ejecuta mientras el usuario NO seleccione la opción 5 (Salir) si presiona el 5 el bucle se repitira
    
    print("----------Parking Center S.A.S.----------")
    # Imprime el encabezado del sistema

    print("""
1. Registrar ingreso
2. Registrar salida
3. Consultar parqueadero actual
4. Ver total recaudado
5. Salir
""")
    # Muestra el menú de opciones numeradas para que el usuario elija
    
    opc = int(input("Ingresa el número de la opción deseada: "))
    # Solicitamos al usuario que ingrese un número.
    # int() convierte la entrada (str) a entero para poder usarla en condicionales.


    # OPCIÓN 1 - Registrar ingreso de vehículo

    if opc == 1:
        placa = input("Ingresar placa: ")  
        # Solicitamos la placa del vehículo que desea ingresar
        
        # Verificamos que la placa no esté ya registrada con este bucle:
        j = 0  # Inicializamos un contador para recorrer la lista de vehículos,donde J es el indice que cambiara de tupla
        while j < len(vehiculos):  
            # Recorremos la lista de vehículos activos usando un índice j,mientras que j sea menor a la cantidad de vehiculos,ya que si j es mayor a la lista de vehiculos,estara reccoriendo tuplas de vehiculos que no existen
            if vehiculos[j][0] == placa:  
                # Si la placa ya existe (vehiculos[j][0] accede a la placa) imprimira: 
                print("Error: Un vehículo con esta placa ya está en el parqueadero.")
                placa = input("Ingresar otra placa: ")  
                # Solicitamos nuevamente la placa
                j = -1  
                # Reiniciamos j a -1 porque al final del ciclo se hace j += 1 para que no recorra la misma placa
                # Esto permite volver a recorrer toda la lista desde el inicio
            j += 1  
            # Incrementamos j en 1 para pasar al siguiente vehículo en la lista
            # Si no hacemos esto, el bucle se quedaría infinito

        # Selección del tipo de vehículo
        print("""
Tipos de vehículos:
1. Moto
2. Carro
3. Camioneta
""")
        tipo_num = int(input("Ingresa el número del tipo de vehículo: "))
        # Solicitamos al usuario elegir un tipo mediante un número

        if tipo_num == 1:
            tipo = "moto"
        elif tipo_num == 2:
            tipo = "carro"
        elif tipo_num == 3:
            tipo = "camioneta"
        else:
            tipo = "carro"  
            # Si el número ingresado es inválido, se asigna carro por defecto

        hora_entrada = datetime.now()  
        # Guardamos la hora exacta de ingreso usando datetime.now()

        vehiculos.append((placa, tipo, hora_entrada))  
        # Añadimos una tupla con la información del vehículo a la lista de vehículos activos
        # append() agrega el elemento al final de la lista

        # Mostramos un mensaje de confirmación
        # strftime('%H:%M:%S') convierte el objeto datetime a formato de hora legible HH:MM:SS
        print(f"Vehículo {placa} tipo {tipo} registrado a las {hora_entrada.strftime('%H:%M:%S')}\n")


    # OPCIÓN 2 - Registrar salida de vehículo

    elif opc == 2:
        placa_salida = input("Ingresar placa para retirar: ")  
        # Solicitamos la placa del vehículo que desea salir

        j = 0  # Inicializamos un contador para recorrer la lista de vehículos
        encontrado = False  
        # Bandera que nos indica si encontramos la placa en la lista de vehículos,en este caso False,para que lo confirme y tengamos esa señalizacion

        while j < len(vehiculos):
            if vehiculos[j][0] == placa_salida:  
                # Comprobamos si la placa ingresada coincide con la placa del vehículo en la posición j (el indice de la tupla que accede al valor de la placa)
                encontrado = True # Si es verdadera,la bandera sera True
                placa, tipo, hora_entrada = vehiculos[j]  
                # Desempaquetamos la tupla para obtener placa, tipo y hora de entrada
                # Donde el primer valor lo desempaquetamos como placa,tipo como tipo,hora de entrada como hora entrada de la tupla del carro indice(j)

                hora_salida = datetime.now()  
                # Obtenemos la hora exacta de salida con la funcion now que agarra la hora exacta

                duracion = hora_salida - hora_entrada  
                # Calculamos el tiempo que el vehículo estuvo estacionado
                # El resultado es un objeto timedelta

                horas = duracion.total_seconds() / 3600  
                # Convertimos la duración de segundos a horas decimales con el metodo total.seconds que convierte a decimales,las horas minutos segundos

                horas = int(horas) + 1  
                # Redondeamos hacia arriba al siguiente número entero
                # Esto asegura que cualquier fracción de hora se cobre como hora completa

                valor = horas * tarifas[tipo]  
                # Calculamos el valor a pagar multiplicando las horas por la tarifa correspondiente

                # Mostramos el recibo de pago
                print(f"\n--- Recibo de Pago ---")
                print(f"Placa: {placa}")
                print(f"Tipo: {tipo}")
                print(f"Horas estacionado: {horas}")
                print(f"Tarifa por hora: ${tarifas[tipo]}")
                print(f"Total a pagar: ${valor}")
                print(f"Hora entrada: {hora_entrada.strftime('%H:%M:%S')}") # strftime convierte valores de hora,minuto y segundo a strings
                print(f"Hora salida: {hora_salida.strftime('%H:%M:%S')}\n") # strftime convierte valores de hora,minuto y segundo a strings

                historial.append((placa, tipo, hora_entrada, hora_salida, valor))  
                # Guardamos la información completa en la lista historial
                # append() agrega la tupla al final de la lista

                vehiculos.pop(j)  
                # Eliminamos el vehículo de la lista de vehículos activos
                # pop(j) elimina el elemento en la posición j para mantener la lista actualizada

                break  # Salimos del bucle porque ya encontramos y procesamos la placa
            j += 1  
            # Incrementamos j para pasar al siguiente vehículo en la lista

        if not encontrado:  
            # Si la bandera sigue en False, significa que la placa no estaba registrada
            print("Error: La placa no se encuentra registrada en el parqueadero.\n")


    # OPCIÓN 3 - Consultar parqueadero actual

    elif opc == 3:
        if vehiculos != []:  # Si la lista no esta vacia se hace el la condicion e inicia el bucle
            # Verificamos si hay vehículos en el parqueadero
            print("\n--- Vehículos en el parqueadero ---")
            j = 0
            while j < len(vehiculos):  
                # Recorremos la lista de vehículos activos
                placa, tipo, hora_entrada = vehiculos[j]  
                # Desempaquetamos cada tupla
                print(f"Placa: {placa} | Tipo: {tipo} | Hora entrada: {hora_entrada.strftime('%H:%M:%S')}")
                j += 1  # Incrementamos j para pasar al siguiente vehículo en la lista
            print()
        else: # Si no se cumple,y esta vacia,ose muestra:
            # Si no hay vehículos, mostramos un mensaje
            print("No hay vehículos en el parqueadero.\n")


    # OPCIÓN 4 - Ver total recaudado

    elif opc == 4:
        total = 0  # Inicializamos la variable acumuladora
        j = 0 # Inicializamos el contador del indice para pasar a los vehiculos
        while j < len(historial):  # Mientras el indice j sea menor a todas las tuplas de vehiculos se recorre,ya que si es mayor a la lista,estaria buscando tuplas inexistentes
            # Recorremos toda la lista historial
            total += historial[j][4]  
            # Sumamos el valor pagado (índice 4 de cada tupla que es valor que lo hicimos y agregamos a cada tupla en la opcion 4)
            j += 1  # Incrementamos j para pasar al siguiente elemento osea vehiculo
        print(f"\nTotal recaudado: ${total}\n")  # Mostramos el total acumulado


    # OPCIÓN 5 - Salir del sistema

    elif opc == 5:
        print("Saliendo del sistema...")
     # Rompemos el bucle principal y terminamos el programa

    # Opción inválida

    else:
        print("Opción no válida. Intente de nuevo.\n") 


 