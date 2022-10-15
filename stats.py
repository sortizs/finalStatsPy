
import matplotlib.pyplot as plt
import data.file as f

def usersPerGender() -> None:
    """Dibuja una grafica de torta de porcentaje de usuarios por género
    """
    genders = ['Masculino', 'Femenino']
    male = 0
    female = 0
    users = f.getNames()
    for user in users:
        userData = f.getUserData(user)
        if 'genero' in userData:
                if userData['genero'] == 'M':
                    male += 1
                elif userData['genero'] == 'F':
                    female += 1
    fig, ax = plt.subplots()
    ax.set_title('Usuarios por género')
    ax.pie([male, female], autopct='%1.2f%%')
    ax.legend(genders, loc='best')
    plt.show()
