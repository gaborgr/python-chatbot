import pandas as pd


def prepare_dataset(ruta_csv):
    # 1. Cargar el CSV
    df = pd.read_csv(ruta_csv)

    conversaciones = []

    # 2. Iterar sobre cada fila del dataset
    for _, fila in df.iterrows():
        chat_texto = fila["chat"]

        if not isinstance(chat_texto, str):
            continue  # saltar valores vacíos o NaN

        # 3. Separar las líneas (cada mensaje)
        lineas = [l.strip() for l in chat_texto.split("\n") if l.strip()]

        # 4. Asegurar que haya más de un mensaje (para formar pares)
        if len(lineas) > 1:
            conversaciones.append(lineas)

    return conversaciones
