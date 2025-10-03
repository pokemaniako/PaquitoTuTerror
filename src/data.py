"""Simple in-memory store for players and bets."""
jugadores = []
apuestas = []

def add_jugador(jugador):
    jugadores.append(jugador)

def find_player_by_credentials(usuario, contraseña):
    for j in jugadores:
        if j.get("usuario") == usuario and j.get("contraseña") == contraseña:
            return j
    return None

def add_apuesta(apuesta):
    apuestas.append(apuesta)
