import matplotlib.pyplot as plt   #para generar una grafica matplotlib

def generate_pie_chart():
    labels = ["A", "B", "C"]
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie (values, labels=labels)
    plt.savefig('pie.png') #guarda una imagen de la grafica
    plt.close()