# Datos de las ciudades y temperaturas
temperaturas = [
    [   # Ciudad LAGO AGRIO
        {"Ciudad": "LAGO AGRIO"},
        [
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 23}
        ],
        [
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 29}
        ],
        [
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 32}
        ]
    ],
    [   # Ciudad JOYA DE LOS SACHAS
        {"Ciudad": "JOYA DE LOS SACHAS"},
        [
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 33}
        ],
        [
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 36},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 48},
            {"day": "Domingo", "temp": 19}
        ],
        [
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 34}
        ]
    ],
    [   # Ciudad FRANCISCO DE ORELLANA
        {"Ciudad": "FRANCISCO DE ORELLANA"},
        [
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 29}
        ],
        [
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 81}
        ],
        [
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 15}
        ]
    ]
]


def calcular_promedio(divisor, dividendo):
    return round(divisor / dividendo)

# Calcular el promedio de temperaturas para cada ciudad y semana
no_ciudad = 0
for ciudad in temperaturas:
    no_ciudad = no_ciudad + 1
    print(f'CIUDAD No.{no_ciudad}')
    no_semana = 0
    suma_promedio = 0

    for semanas in ciudad[1:]:
        no_semana += 1
        suma = sum(dia['temp'] for dia in semanas)
        promedio_semana = calcular_promedio(suma, len(semanas))
        print(f'El promedio semana No.{no_semana} es: {promedio_semana}')
        suma_promedio += promedio_semana

    promedio_ciudad = calcular_promedio(suma_promedio, len(ciudad) - 1)
    print(f'El promedio mensual es: {promedio_ciudad}')