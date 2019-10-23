

from os import system
import time

def opcion_1(lista_compradores, lista_vendidos, lista_ganancia, lista_piso, lista_tipo):

    valid = True
    contador = 2

    while True:
        try:
            rut = int(
                input("Ingrese su rut(SIN PUNTOS Y SIN DIGITO VERIFICADOR): "))
            lista_compradores.append(rut)
            break

        except:
            print("ha ingresado un rut incorrecto")

    system("cls")



    while valid == True:
        
        print("******   DEPARTAMENTOS   ******")
        print("")
        print("TIPO |  A  |  B  |  C  |  D  |")
        print("PISO")
        for p in (lista_piso):
            print(p,  end="")
            for t in (lista_tipo):
                comparacion = (str(p) + t)
                if comparacion in lista_vendidos:
                    print("    [X]", end="")
                else:
                    print(f"    [D]", end="")
            print()
        print()


        piso = int(input("Ingrese piso: "))
        while piso not in lista_piso:
            piso = int(input("Ingreso datos erroneos, Ingrese el piso otra vez: "))
        tipo = input("Ingrese tipo: ").upper() #Aun que se ingrese una letra minuscula quedara automaticamente en mayuscula.

        while tipo not in lista_tipo:
            tipo = input("Ingreso datos erroneos, Ingrese el tipo otra vez: ").upper()
        system("cls")
        depto = str(piso)+tipo



        if depto in lista_vendidos:
            print("el departamento ingresado ya esta vendido")
            time.sleep(2)
            system("cls")
            continue


        else:
            lista_vendidos.append(depto)
            valid = False


        if tipo == "A":
            precio = 3800
            if piso >= 3:
                while contador != piso:
                    precio += 100
                    contador += 1

        elif tipo == "B":
            precio = 3000
            if piso >= 3:
                while contador != piso:
                    precio += 100
                    contador += 1

        elif tipo == "C":
            precio = 2800
            if piso >= 3:
                while contador != piso:
                    precio += 100
                    contador += 1

        elif tipo == "D":
            precio = 3500
            if piso >= 3:
                while contador != piso:
                    precio += 100
                    contador += 1

        lista_ganancia.append(precio)
        print(
            f"LA COMPRA DEL DEPARTAMENTO {depto} HA SIDO REALIZADA EXITOSAMENTE")
        print()
        input("PRESIONE ENTER PARA CONTINUAR")
        system("cls")
        break


def opcion_2(lista_piso, lista_tipo, lista_vendidos):
    print("******   DEPARTAMENTOS   ******")
    print("")
    print("TIPO |  A  |  B  |  C  |  D  |")

    print("PISO")
    for p in (lista_piso):
        print(p,  end="")
        for t in (lista_tipo): 
            comparacion = (str(p) + t)
            if comparacion in lista_vendidos:
                print("    [X]", end="")
            else:
                print(f"    [D]", end="")
        print()

    print("")
    input("PRESIONE ENTER PARA CONTINUAR")
    system("cls")


def opcion_3(lista_compradores):

    if len(lista_compradores) == 0:
        print("NO SE A EFECTUADO NINGUNA VENTA DE DEPARTAMENTOS")
    else:

        contador = 0
        lista_ok = []
        temp_list = lista_compradores
        temp_list.sort()
        print("RUT")
        print("")
        while contador < len(temp_list):
            if temp_list[contador] not in lista_ok:
                print(temp_list[contador])
                lista_ok.append(temp_list[contador])
            contador = contador + 1
    print("")
    input("PRESIONE ENTER PARA CONTINUAR")
    system("cls")


def opcion_4(lista_compradores):
    if len(lista_compradores) != 0:
        print("INGRESE RUT : ")
        busca_rut = int(input())
        if busca_rut in lista_compradores:
            print("El rut ingresado pertenece a un cliente de nuestra inmobiliaria")
            print()
        else:
            print("El rut ingresado no existe en nuestro sistema")
            print()
    else:
        print("NO SE A EFECTUADO NINGUNA VENTA DE DEPARTAMENTOS")
    input("PRESIONE ENTER PARA CONTINUAR")
    system("cls")


def opcion_5(lista_compradores, lista_vendidos):
    if len(lista_compradores) != 0:
        contador = 0
        while True:
            system("cls")
            print("LISTA DE DEPARTAMENTOS VENDIDOS")
            for dep in (lista_vendidos):
                print(dep)

            print("QUE DEPARTAMENTO REASIGNARA?")
            departamento = input().upper()
            system("cls")
            if departamento in lista_vendidos:
                while contador < len(lista_compradores):
                    if departamento == lista_vendidos[contador]:
                        del lista_compradores[contador]
                        print("Favor ingrese el rut del nuevo cliente : ")
                        nuevo_rut = int(input())
                        system("cls")
                        lista_compradores.insert(contador, nuevo_rut)
                        print("El rut del nuevo cliente ha sido ingresado")
                    contador = contador + 1
            else:
                print("ESTE DEPARTAMENTO NO ESTA EN LA LISTA")
            input("PRESIONE ENTER PARA CONTINUAR")
            system("cls")
            break
    else:
        print("NO SE A EFECTUADO NINGUNA VENTA DE DEPARTAMENTOS")
    input("PRESIONE ENTER PARA CONTINUAR")
    system("cls")


def opcion_6(lista_vendidos, lista_ganancia):
    if len(lista_vendidos) != 0:
        precio_a = 3800
        precio_b = 3000
        precio_c = 2800
        precio_d = 3500
        contador = 0
        acumulador_a = 0
        acumulador_aa = 0
        contador_a = 0
        acumulador_b = 0
        acumulador_bb = 0
        contador_b = 0
        acumulador_c = 0
        acumulador_cc = 0
        contador_c = 0
        acumulador_d = 0
        acumulador_dd = 0
        contador_d = 0
        total_contador = 0
        total_acumulador = 0
        fido = 0
        total_ganancia = 0
        while contador != len(lista_vendidos):
            if("A" in lista_vendidos[contador]):
                acumulador_a += precio_a
                acumulador_aa += lista_ganancia[contador]
                contador_a += 1
            elif("B" in lista_vendidos[contador]):
                acumulador_b += precio_b
                acumulador_bb += lista_ganancia[contador]
                contador_b += 1
            elif("C" in lista_vendidos[contador]):
                acumulador_c += precio_c
                acumulador_cc += lista_ganancia[contador]
                contador_c += 1
            elif("D" in lista_vendidos[contador]):
                acumulador_d += precio_d
                acumulador_dd += lista_ganancia[contador]
                contador_d += 1
            contador += 1
            total_contador = contador_a + contador_b + contador_c + contador_d
            total_acumulador = acumulador_a + acumulador_b + acumulador_c + acumulador_d
            a = (acumulador_aa-(contador_a*3800))
            b = (acumulador_bb-(contador_b*3000))
            c = (acumulador_cc-(contador_c*2800))
            d = (acumulador_dd-(contador_d*3500))
            fido = a+b+c+d
            total_ganancia = total_acumulador+fido
        print("TIPO DEPARTAMENTO    CANTIDAD   TOTAL    RECARGO POR PISO")
        print("  TIPO A "+" 3800 UF    "+str(contador_a)+"          " +
              str(acumulador_a)+" UF     " + str(acumulador_aa-(contador_a*precio_a)))
        print("  TIPO B "+" 3000 UF    "+str(contador_b)+"          " +
              str(acumulador_b)+" UF     " + str(acumulador_bb-(contador_b*precio_b)))
        print("  TIPO C "+" 2800 UF    "+str(contador_c)+"          " +
              str(acumulador_c)+" UF     " + str(acumulador_cc-(contador_c*precio_c)))
        print("  TIPO D "+" 3500 UF    "+str(contador_d)+"          " +
              str(acumulador_d)+" UF     " + str(acumulador_dd-(contador_d*precio_d)))
        print()
        print("  TOTAL              "+str(total_contador)+"          "+str(total_acumulador) +
              " UF"+" + "+str(fido)+" UF"+"  "+"  =  "+str(total_ganancia)+" UF")
    else:
        print("NO SE A EFECTUADO NINGUNA VENTA DE DEPARTAMENTOS")
    input("PRESIONE ENTER PARA CONTINUAR")
    system("cls")

lista_compradores = []
lista_vendidos = []
lista_ganancia = []
lista_piso = [10,9,8,7,6,5,4,3,2,1]
lista_tipo = ["A","B","C","D"]
opcion = 0
print()
print("   * * * BIENVENIDO AL SISTEMA DE MURITO * * * ")
time.sleep(2)
system("cls")

while True:

    print("")
    print("      * * * MENÚ * * * ")
    print("[1] COMPRAR DEPARTAMENTO")
    print("[2] MOSTRAR DEPARTAMENTOS DISPONIBLES")
    print("[3] VER LISTADO DE COMPRADORES")
    print("[4] BUSCAR COMPRADOR")
    print("[5] REASIGNAR COMPRADOR")
    print("[6] MOSTRAR GANANCIAS TOTALES")
    print("[7] SALIR")
    print()
    try:
        opcion = int(input("Ingrese una opción :"))
    except ValueError:
        print("OPCION INGRESADA NO VALIDA")
        opcion = 0
        time.sleep(2)
        system("cls")

    if opcion == 1:
        print("INGRESANDO A: COMPRAR DEPARTAMENTO")
        time.sleep(2)
        system("cls")
        opcion_1(lista_compradores, lista_vendidos, lista_ganancia, lista_piso,lista_tipo)
    elif opcion == 2:
        print("INGRESANDO A: DEPARTAMENTOS DISPONIBLES")
        time.sleep(2)
        system("cls")
        opcion_2(lista_piso,lista_tipo,lista_vendidos)

    elif opcion == 3:
        print("INGRESANDO A: LISTA DE COMPRADORES")
        time.sleep(2)
        system("cls")
        opcion_3(lista_compradores)

    elif opcion == 4:
        print("INGRESANDO A: BUSQUEDA DE COMPRADOR")
        time.sleep(2)
        system("cls")
        opcion_4(lista_compradores)
    elif opcion == 5:
        print("INGRESANDO A: REASIGNAR COMPRADOR")
        time.sleep(2)
        system("cls")
        opcion_5(lista_compradores, lista_vendidos)
    elif opcion == 6:
        print("INGRESANDO A: GANANCIAS")
        time.sleep(2)
        system("cls")
        opcion_6(lista_vendidos, lista_ganancia)

    elif opcion == 7:
        print("SALIENDO DEL SISTEMA")
        time.sleep(2)
        system("cls")
        print("GRACIAS POR USAR EL SISTEMA")
        time.sleep(2)
        break
    else:
        print("SELECCIONE UNA OPCION VALIDA")
        time.sleep(2)
        system("cls")
