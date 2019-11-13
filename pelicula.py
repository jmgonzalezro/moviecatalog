# aquí estará la superclase película donde se definen los valores de la misma
class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento, director, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        self.director = director
        self.genero = genero

    def __str__(self):
        return """\
{} ({}, {} - {})""".format(self.titulo, self.lanzamiento, self.director, self.genero)

# c = []


# p1=Pelicula("El caballero oscuro", 152, 2008, "Christopher Nolan", "Thriller")
# p2=Pelicula("¡Olvidate de mi!", 108, 2004, "Michel Gondry","Drama")
# p3=Pelicula("American beauty",  122, 1999, "Sam Mendes", "Drama")
# p4=Pelicula("El club de la lucha",139, 1999, "David Fincher", "Thriller")
# p5=Pelicula("Pulp Fiction",  153, 1994, "Quentin Tarantino", "Thriller")

# c.append(p1)
# c.append(p2)
# c.append(p3)
# c.append(p4)
# c.append(p5)

# print(c(p.director)