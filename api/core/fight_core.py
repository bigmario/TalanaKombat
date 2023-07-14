import json

def ejecutar_golpe(personaje, movimiento, golpe):
    energia = 0
    narracion = ""

    if personaje == "Tonyn Stallone":
        if movimiento == "DSD" and golpe == "P":
            narracion = f"{personaje} usa Taladoken"
            energia = 3
        elif movimiento == "SD" and golpe == "K":
            narracion = f"{personaje} usa Remuyuken"
            energia = 2
        elif (
            movimiento == "W"
            or movimiento == "S"
            or movimiento == "A"
            or movimiento == "D"
        ):
            narracion = f"{personaje} se mueve {movimiento}"
        elif golpe == "P":
            narracion = f"{personaje} da un puñetazo"
            energia = 1
        elif golpe == "K":
            narracion = f"{personaje} da una patada"
            energia = 1
    elif personaje == "Arnaldor Shuatseneguer":
        if movimiento == "SA" and golpe == "K":
            narracion = f"{personaje} usa Remuyuken"
            energia = 3
        elif movimiento == "ASA" and golpe == "P":
            narracion = f"{personaje} usa Taladoken"
            energia = 2
        elif (
            movimiento == "W"
            or movimiento == "S"
            or movimiento == "A"
            or movimiento == "D"
        ):
            narracion = f"{personaje} se mueve {movimiento}"
        elif golpe == "K":
            narracion = f"{personaje} da una patada"
            energia = 1
        elif golpe == "P":
            narracion = f"{personaje} da un puñetazo"
            energia = 1

    return narracion, energia


def determinar_ganador(energia_p1, energia_p2):
    if energia_p1 <= 0:
        return "Arnaldor Shuatseneguer gana la pelea."
    elif energia_p2 <= 0:
        return "Tonyn Stallone gana la pelea."
    else:
        return "La pelea termina en empate."


def narrar_pelea(pelea_json_pydantic):
    pelea_json = json.loads(pelea_json_pydantic.json())
    acciones_p1 = pelea_json["player1"]
    acciones_p2 = pelea_json["player2"]

    narracion = ""
    energia_p1 = 6
    energia_p2 = 6
    p1 = "Tonyn Stallone"
    p2 = "Arnaldor Shuatseneguer"

    max_turnos = max(len(acciones_p1["movimientos"]), len(acciones_p2["movimientos"]))

    for i in range(max_turnos):
        movimiento_p1 = (
            acciones_p1["movimientos"][i] if i < len(acciones_p1["movimientos"]) else ""
        )
        golpe_p1 = acciones_p1["golpes"][i] if i < len(acciones_p1["golpes"]) else ""

        movimiento_p2 = (
            acciones_p2["movimientos"][i] if i < len(acciones_p2["movimientos"]) else ""
        )
        golpe_p2 = acciones_p2["golpes"][i] if i < len(acciones_p2["golpes"]) else ""

        narracion_p1, energia_golpe_p1 = ejecutar_golpe(p1, movimiento_p1, golpe_p1)
        narracion_p2, energia_golpe_p2 = ejecutar_golpe(p2, movimiento_p2, golpe_p2)

        if narracion_p1:
            narracion += f"- {narracion_p1}\n"
        if narracion_p2:
            narracion += f"- {narracion_p2}\n"

        energia_p2 -= energia_golpe_p1

        if energia_p2 <= 0:
            break

        energia_p1 -= energia_golpe_p2

        if energia_p1 <= 0:
            break

    narracion += determinar_ganador(energia_p1, energia_p2)
    return narracion



if __name__ == "__main__":
    # Pelea 1
    pelea_json = {
        "player1": {
            "movimientos": ["D", "DSD", "S", "DSD", "SD"],
            "golpes": ["K", "P", "", "K", "P"],
        },
        "player2": {
            "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
            "golpes": ["K", "", "K", "P", "P"],
        },
    }

    narracion_pelea = narrar_pelea(pelea_json)
    print("Pelea 1:")
    print(narracion_pelea)
    print()

    # Pelea 2
    pelea2 = {
        "player1": {
            "movimientos": ["SDD", "DSD", "SA", "DSD"],
            "golpes": ["K", "P", "K", "P"],
        },
        "player2": {
            "movimientos": ["DSD", "WSAW", "ASA", "", "ASA", "SA"],
            "golpes": ["P", "K", "K", "K", "P", "k"],
        },
    }

    narracion_pelea = narrar_pelea(pelea2)
    print("Pelea 2:")
    print(narracion_pelea)
    print()

    # Pelea 3
    pelea3 = {
        "player1": {
            "movimientos": ["DSD", "S"],
            "golpes": ["P", ""],
        },
        "player2": {
            "movimientos": ["", "ASA", "DA", "AAA", "", "SA"],
            "golpes": ["P", "", "P", "K", "K", "K"],
        },
    }

    narracion_pelea = narrar_pelea(pelea3)
    print("Pelea 3:")
    print(narracion_pelea)
