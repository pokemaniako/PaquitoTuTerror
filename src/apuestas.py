from random import choice
import validadores as vt
import data

def apostar_rojo_negro(jugador):
    print("\t Has seleccionado REALIZAR APUESTA ADICTO DE MRD")
    monto = vt.validador(input("\t Ingrese monto de la apuesta -> "), "decimal", "\t Monto inválido, debe ser un número positivo.", lambda x: x > 0)
    if monto > jugador["saldo"]:
        print("\t No hay sencillo hijo")
        return

    eleccion = input("\t Elija 'rojo' o 'negro' -> ").lower()
    if eleccion not in ["rojo", "negro"]:
        print("\t Eleccion no valida")
        return

    resultado = choice(["rojo", "negro"])
    if eleccion == resultado:
        jugador["saldo"] += monto
        print(f"\t Ganaste! El resultado fue {resultado}. \n\t Nuevo saldo: {jugador['saldo']:.2f}")
    else:
        jugador["saldo"] -= monto
        print(f"\t Perdiste! El resultado fue {resultado}. \n\t Nuevo saldo: {jugador['saldo']:.2f}")

    apuesta = {
        "jugador": jugador["usuario"],
        "monto": monto,
        "eleccion": eleccion,
        "resultado": resultado,
        "saldo_restante": jugador["saldo"]
    }
    data.add_apuesta(apuesta)

def ruleta(jugador):
    print("\t Has seleccionado RULETA ADICTO DE MRD")
    monto = vt.validador(input("\t Ingrese monto de la apuesta -> "), "decimal", "\t Monto inválido, debe ser un número positivo.", lambda x: x > 0)
    if monto > jugador["saldo"]:
        print("\t No hay sencillo hijo")
        return

    eleccion = vt.validador(input("\t Elija un numero del '1' al '36' -> "), "numero", "\t Eleccion no valida.", lambda x: 1 <= x <= 36)
    resultado = choice(range(1, 37))
    if eleccion == resultado:
        jugador["saldo"] += monto
        print(f"\t Ganaste el resultado fue {resultado}. \n\t Nuevo saldo: {jugador['saldo']:.2f}")
    else:
        jugador["saldo"] -= monto
        print(f"\t Perdiste el resultado fue {resultado}. \n\t Nuevo saldo: {jugador['saldo']:.2f}")

    apuesta = {
        "jugador": jugador["usuario"], 
        "monto": monto,
        "eleccion": eleccion,
        "resultado": resultado,
        "saldo_restante": jugador["saldo"]
    }
    data.add_apuesta(apuesta)

def ver_historial(jugador):
    print(f"\t Historial de apuestas para {jugador['usuario']}")
    historial_encontrado = False
    for apuesta in data.apuestas:
        if apuesta["jugador"] == jugador["usuario"]:
            historial_encontrado = True
            print(f"\t Apostó {apuesta['monto']:.2f} a {apuesta['eleccion']} - Resultado: {apuesta['resultado']} - Saldo: {apuesta['saldo_restante']:.2f}")
    if not historial_encontrado:
        print("\t No existe historial de apuestas.")
