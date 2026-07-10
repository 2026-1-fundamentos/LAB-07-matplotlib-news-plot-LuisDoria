"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.
    """

    import os

    import matplotlib

    # Permite generar la imagen sin abrir una ventana gráfica.
    matplotlib.use("Agg")

    import matplotlib.pyplot as plt
    import pandas as pd

    # Lee el archivo CSV.
    # La primera columna contiene los años y se usa como índice.
    data = pd.read_csv(
        "files/input/news.csv",
        index_col=0,
    )

    # Convierte los años a números enteros.
    data.index = data.index.astype(int)

    # El test elimina esta carpeta antes de ejecutar la función,
    # por lo que debe crearse nuevamente.
    os.makedirs(
        "files/plots",
        exist_ok=True,
    )

    # Colores para cada medio de comunicación.
    colors = {
        "Television": "#1f77b4",
        "Newspaper": "#ff7f0e",
        "Internet": "#2ca02c",
        "Radio": "#d62728",
    }

    # Crea la figura y el área de la gráfica.
    fig, ax = plt.subplots(
        figsize=(10, 6),
    )

    # Dibuja una línea para cada columna.
    for column in data.columns:
        ax.plot(
            data.index,
            data[column],
            color=colors[column],
            linewidth=2.5,
            marker="o",
            markersize=5,
            label=column,
        )

    # Título y nombres de los ejes.
    ax.set_title(
        "How people get their news",
        fontsize=18,
        fontweight="bold",
        loc="left",
        pad=15,
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Percentage")

    # Muestra todos los años en el eje horizontal.
    ax.set_xticks(data.index)

    # Define el rango del eje vertical.
    ax.set_ylim(0, 90)

    # Agrega líneas horizontales de referencia.
    ax.grid(
        axis="y",
        linestyle="--",
        linewidth=0.8,
        alpha=0.35,
    )

    # Agrega la leyenda.
    ax.legend(
        frameon=False,
        ncol=4,
        loc="upper center",
    )

    # Oculta bordes innecesarios.
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Ajusta los elementos dentro de la figura.
    fig.tight_layout()

    # Guarda la imagen en la ruta exigida por el test.
    fig.savefig(
        "files/plots/news.png",
        dpi=300,
        bbox_inches="tight",
    )

    # Cierra la figura para liberar memoria.
    plt.close(fig)
