import validadores as vt
import data

def registrar_jugador():
    print("\t Has seleccionado REGISTRAR")
    nombre = vt.validador(input("\t Ingrese su nombre -> "), "texto", "\t Nombre inválido, solo letras y espacios permitidos.")
    apellido_paterno = vt.validador(input("\t Ingrese su apellido paterno -> "), "texto", "\t Apellido paterno inválido, solo letras y espacios permitidos.")
    apellido_materno = vt.validador(input("\t Ingrese su apellido materno -> "), "texto", "\t Apellido materno inválido, solo letras y espacios permitidos.")
    sexo = vt.validador(input("\t Ingrese su genero (M: masculino, F: Femenino) -> "), "genero", "\t Género inválido, solo M o F.")
    edad = vt.validador(input("\t Ingrese su edad -> "), "numero", "\t Edad inválida, debe ser un número mayor a 18.", lambda x: x >= 18)
    usuario = input("\t Cree un nombre de usuario -> ")
    contraseña = input("\t Cree una contraseña -> ")
    saldo = vt.validador(input("\t Ingrese su saldo en soles -> "), "decimal", "\t Saldo inválido, debe ser un número no negativo.", lambda x: x >= 0)

    jugador = {
        "nombre": nombre,
        "apellido_paterno": apellido_paterno,
        "apellido_materno": apellido_materno,
        "genero": sexo,
        "edad": edad,
        "usuario": usuario,
        "contraseña": contraseña,
        "saldo": saldo
    }
    data.add_jugador(jugador)
    print(f"\t Usuario {usuario} registrado con exito. Saldo inicial: {saldo:.2f} solsitos")
    return jugador

def iniciar_sesion():
    print("\t Has seleccionado INICIAR SESIÓN")
    usuario = input("\t Usuario -> ")
    contraseña = input("\t Contraseña -> ")
    jugador = data.find_player_by_credentials(usuario, contraseña)
    if jugador:
        print(f"\t Bienvenido de nuevo, {jugador['nombre']}!")
        if jugador != 0:
            return jugador
    print("\t Usuario o contraseña incorrecto")
    return 0
