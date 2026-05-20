
temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

sala_maior_risco = None
max_criticos = -1

for i, sala in enumerate(temperaturas):
    numero_sala = i + 1
    media = sum(sala) / len(sala)
    registros_criticos = sum(1 for t in sala if t >= 33)

    print(f"Sala {numero_sala}")
    print(f"Média: {media}")
    print(f"Registros críticos: {registros_criticos}")

    if registros_criticos > max_criticos:
        max_criticos = registros_criticos
        sala_maior_risco = numero_sala

print(f"\nSala com maior risco: Sala {sala_maior_risco}")