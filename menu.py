from catalogo import *
from pelicula import *

# instanciamos un objeto catálogo donde se cargarán todas las películas
c = Catalogo()

c.agregar(Pelicula("El caballero oscuro", 152, 2008, "Christopher Nolan", "Thriller"))
c.agregar(Pelicula("¡Olvidate de mi!", 108, 2004, "Michel Gondry", "Drama"))
c.agregar(Pelicula("American beauty", 122, 1999, "Sam Mendes", "Drama"))
c.agregar(Pelicula("El club de la lucha", 139, 1999, "David Fincher", "Thriller"))
c.agregar(Pelicula("Pulp Fiction", 153, 1994, "Quentin Tarantino", "Thriller"))
c.agregar(Pelicula("Persona", 81, 1966, "Ingmar Bergman", "Drama"))
c.agregar(Pelicula("La vida de Adelle", 180, 2013, "Abdellatif Kechiche", "Drama"))
c.agregar(Pelicula("La grande bellezza", 142, 2013, "Paolo Sorrentino", "Comedia"))
c.agregar(Pelicula("Como locos", 89, 2011, "Drake Doremus", "Romance"))
c.agregar(Pelicula("Nunca me abandones", 103, 2010, "Mark Romanek", "Romance"))
c.agregar(Pelicula("Al final de la escapada", 89, 1960, "Jean Luc-Godard", "Drama"))
c.agregar(Pelicula("Metropolis", 153, 1927, "Fritz Lang", "Drama"))

def menu():
    panel = str("""
                ¿Qué quieres hacer?

    ============== Menú Principal ====================
    _________________________________________________
    |   1 : Mostrar todo el catálogo de películas    |
    |________________________________________________|
    |   2 : Mostrar películas por género             |
    |________________________________________________|
    |   3 : Añadir una película                      |
    |________________________________________________|
    |   4 : Eliminar una película                    |
    |________________________________________________|
    |   5 : Salir                                    |
    |________________________________________________|
    """)
    # try:
    #     menu_principal = float(input("Selecciona una opción: "))
    # except:
    #     print("No está bien lo que haces")
    #     exit()

    try:
        while True:
            print(panel)
            menu_principal = float(input("Selecciona una opción: "))
            if menu_principal:
                if float(menu_principal) == 1:
                    c.mostrar()

                elif float(menu_principal) == 2:
                    mi_genero = input("¿Qué genero quieres filtrar? ")
                    c.mostrar_por_genero(mi_genero)
                    # menu()

                elif float(menu_principal) == 3:
                    ptitulo = input("Título de la película que quieres añadir: ")
                    pduracion = input("Duración: ")
                    paño = input("Año de lanzamiento: ")
                    pdirector = input("Director de la película: ")
                    pgenero = input("Género de la película: ")
                    c.agregar(Pelicula(ptitulo, pduracion, paño, pdirector, pgenero))
                    # print("Se ha añadido {} al catálogo".format(ptitulo))
                    # menu()

                elif float(menu_principal) == 4:
                    indice_de_peli = int(input("¿Qué película quieres eliminar? (introduce su índice) "))
                    c.eliminar(indice_de_peli)
                    # menu()


                elif float(menu_principal) == 5:
                    print("Saliendo del programa...")
                    exit()

                else:
                    print("\nERROR\n\nPresiona un número entre el 1 y el 5")
                    # menu()

        else:
            print("Por favor, introduce un número correcto")
        
    except ValueError:
        print("Por favor, no intentes buguear el sistema con números incorrectos o letras. Presiona números en base 10.")

    # except:
    #     print("Por favor, utiliza un número entre el 1 y el 5 para navegar en el menú")

menu()


























# print(""""
# Bienvenido al sistema de catálogo de películas de python para nTic 2019

#             ¿Qué quieres hacer?

# ======================================================
# _________________________________________________
# |   1 : Mostrar todo el catálogo de películas    |
# |________________________________________________|
# |   2 : Mostrar películas por género             |
# |________________________________________________|
# |   3 : Añadir una película                      |
# |________________________________________________|
# |   4 : Eliminar una película                    |
# |________________________________________________|
# |   5 : Salir                                    |
# |________________________________________________|
# """)


# # ------------ Super bucle para navegar por el menú principal ------------
# menu_principal = input("Selecciona una opción: ")

# while True:
#     if menu_principal > "0" and menu_principal < "6" :
#         if float(menu_principal) == 1:
#             c.mostrar()

#         elif float(menu_principal) == 2:
#             mi_genero = input("¿Qué genero quieres filtrar? (Drama / Thriller / Comedia / Romance): ")
#             c.mostrar_por_genero(mi_genero)

#         elif float(menu_principal) == 3:
#             ptitulo = input("Título de la película que quieres añadir: ")
#             pduracion = input("Duración: ")
#             paño = input("Año de lanzamiento: ")
#             pdirector = input("Director de la película: ")
#             pgenero = input("Género de la película: ")
#             c.agregar(Pelicula(ptitulo, pduracion, paño, pdirector, pgenero))
#             # print("Se ha añadido {} al catálogo".format(ptitulo))

#         elif float(menu_principal) == 4:
#             indice_de_peli = int(input("¿Qué película quieres eliminar? (introduce su índice) "))
#             c.eliminar(indice_de_peli)

#         elif float(menu_principal) == 5:
#             print("Saliendo del programa...")
#             exit()

#     else:
#         print("Presiona un número entre el 1 y el 5")

# else:
#     print("Por favor, introduce un número correcto")

