# Constructor de clase. Superclase catálogo donde estarán los productos audiovisuales
# además de las funciones de agregar, eliminar, mostrar, mostrar_por_genero
class Catalogo:

    def __init__(self, peliculas=[]):
        self.peliculas = []

    # Mostrar películas
    def mostrar(self):
        for posicion, peli in enumerate(self.peliculas, 1):
            print("{}.- {}".format(posicion, peli))
    
    # Mostrar películas por género
    def mostrar_por_genero(self, genero):
        for peli in self.peliculas:
            if peli.genero == genero:
                print(peli.titulo)
        if genero not in peli.genero:
            print("Error. Selecciona un género correcto. ¡Cuidado con las mayúsculas!")


    # Agregar película
    def agregar(self, peli):
        self.peliculas.append(peli)
        print("Se ha agregado la película {} al catálogo".format(peli.titulo))

    # Eliminar película
    def eliminar(self, peli_eliminada = None):
        # self.peliculas.pop(peli)
        # # print("Se ha eliminado {}".format(self.peli.titulo))
        # print("Se ha eliminado la película", self.peliculas.pop(peli))
        for indice, peli in enumerate(self.peliculas, 1):
            if indice == peli_eliminada:
                del(self.peliculas[indice - 1])
                print("Se ha eliminado la película", str(peli))

