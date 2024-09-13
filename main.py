from collections import Counter


def calculate_frequencies(message):
    # Calcular la frecuencia de cada símbolo en el mensaje
    frequency = Counter(message)
    return frequency


def sort_frequencies(frequency):
    # Ordenar la lista de símbolos según su frecuencia en orden decreciente
    sorted_frequencies = sorted(
        frequency.items(), key=lambda item: item[1], reverse=True
    )
    return sorted_frequencies


def split_frequencies(sorted_frequencies):
    # Dividir la lista en dos partes con la suma de frecuencias más cercana posible
    total_sum = sum(freq for _, freq in sorted_frequencies)
    cumulative_sum = 0
    group1 = []
    group2 = []

    # Recorremos la lista
    for symbol, freq in sorted_frequencies:
        if cumulative_sum + freq <= total_sum / 2:
            group1.append((symbol, freq))
            cumulative_sum += freq
        else:
            break

    # El resto de los elementos van al grupo 2
    group2 = sorted_frequencies[len(group1) :]

    return group1, group2


def shannon_fano_partition(message):
    # Calcular frecuencias
    frequencies = calculate_frequencies(message)
    # Ordenar frecuencias
    sorted_frequencies = sort_frequencies(frequencies)
    # Dividir en dos grupos
    group1, group2 = split_frequencies(sorted_frequencies)

    return sorted_frequencies, group1, group2


def print_table(header, rows):
    # Calcular el ancho de cada columna
    col_widths = [max(len(str(item)) for item in col) for col in zip(header, *rows)]

    # Crear una fila formateada
    def format_row(row):
        return " | ".join(
            f"{str(item).ljust(width)}" for item, width in zip(row, col_widths)
        )

    # Imprimir la tabla
    print(format_row(header))
    print("-+-".join("-" * width for width in col_widths))
    for row in rows:
        print(format_row(row))


# Input de ejemplo
message = input("Ingresa el mensaje: ")
sorted_frequencies, group1, group2 = shannon_fano_partition(message)

# Preparar datos para la tabla
header = ["Símbolo", "Frecuencia", "Grupo"]
rows = [(symbol, freq, "1") for symbol, freq in group1] + [
    (symbol, freq, "2") for symbol, freq in group2
]

# Imprimir la tabla
print_table(header, rows)
