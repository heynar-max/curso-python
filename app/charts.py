import matplotlib.pyplot as plt #para leer

def generate_bar_chart(name, labels, values): #name para que salga el nombre de la garfica
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    #plt.show() #show hace es detener el programa
    plt.savefig(f'./imgs/{name}.png') #guarda una imagen de la grafica y name sale el nombre que se necesita
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    #plt.show() #show hace es detener el programa
    plt.savefig('pie.png') #guarda una imagen de la grafica
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]
    generate_bar_chart(labels, values)
    #generate_pie_chart(labels, values)