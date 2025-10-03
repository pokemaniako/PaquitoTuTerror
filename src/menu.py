import auth
import apuestas as ap

def menu_de_inicio():
    while True:
        print("\n\t|" + "-" * 50 + "|")
        print("\t|           Bienvenido Adicto al gambling            |")
        print("\t|           ¿Que desea realizar?                    |")
        print("\t|           (1) Registrarme                          |")
        print("\t|           (2) Iniciar sesion                       |")
        print("\t|           (3) Irse a la mrd                        |")
        print("\t|" + "-" * 50 + "|")
        rpta = input("\t| Ingrese su rpta. -> ")
        if rpta == "1":
            jugador = auth.registrar_jugador()
            if jugador:
                menu_jugador(jugador)
        elif rpta == "2":
            jugador = auth.iniciar_sesion()
            if jugador:
                menu_jugador(jugador)
        elif rpta == "3":
            print("\t Vuelve cuando tengas plata bab:bear:son")
            break
        else:
            print("\t Ingresa bien tu rpta hermanito lindo :v ")


def menu_jugador(jugador):
    while True:
        print("\n\t|" + "*" * 50 + "|")
        print(f"\t|           Jugador: {jugador['nombre']}                      ")
        print(f"\t|           Saldo actual: {jugador['saldo']:.2f} soles                ")
        print("\t|           ¿DONDE donde quieres apostar adicto?                         ")
        print("\t|           (1) ROJO O NEGRO")
        print("\t|           (2) Ruletita MANO")
        print("\t|           (3) Ver historial           ")
        print("\t|           (4) Consultar saldo           ")
        print("\t|           (5) Largarse a la magno mrd                         |")
        print("\t|" + "_" * 50 + "|")
        opcion = input("\t| Seleccione una opcion -> ")
        if opcion == "1":
            ap.apostar_rojo_negro(jugador)
        elif opcion == "2":
            ap.ruleta(jugador)
        elif opcion == "3":
            ap.ver_historial(jugador)
        elif opcion == "4":
            print(f"\t Jugador: {jugador['nombre']} {jugador['apellido_paterno']}")
            print(f"\t Saldo actual: {jugador['saldo']:.2f} soles")
        elif opcion == "5":
            print("\t Sesion cerrada")
            break
        else:
            print("\t Opcion incorrecta hermanito lindo")
