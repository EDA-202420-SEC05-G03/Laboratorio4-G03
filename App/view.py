"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones
 *
 * Dario Correal
 """

import sys
import App.logic as logic
from DataStructures.List import single_linked_list as lt


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_logic():
    """
    Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control


def print_menu():
    """
    Menu de usuario
    """
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar la información de un libro")
    print("3- Consultar los libros de un autor")
    print("4- Libros por género")
    print("5- Consultar los TOP n libros del catalogo")
    print("6- Consultar el libro con mayor rating promedio")
    print("0- Salir")


def load_data(control):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    books, authors, tags, book_tags = logic.load_data(control)
    return books, authors, tags, book_tags


def print_author_data(author):
    """
    Recorre la lista de libros de un autor, imprimiendo
    la informacin solicitada.
    """
    if author:
        print('Autor encontrado: ' + author['name'])
        print('Promedio: ' + str(author['average_rating']))
        print('Total de libros: ' + str(lt.size(author['books'])))
        for book_pos in range(0, lt.size(author['books'])):
            book = lt.get_element(author['books'], book_pos)
            print('Titulo: ' + book['title'] + '  ISBN: ' + book['isbn'])
    else:
        print('No se encontro el autor')

def print_book_info(book):
    """
    Imprime los mejores libros solicitados
    """
    if book:
        print('Titulo: ' + book['title'] + '  ISBN: ' +
                  book['isbn'] + ' Rating: ' + book['average_rating'] +
                    ' Work text reviews count : ' + book['work_text_reviews_count'])
    else:
        print('No se encontraron libros')

def print_first_and_last_books(first, last):
    """
    Imprime los TOP n libros solicitados en la impresión
    """
    print("\nLos primeros libros de la lista son: \n")
    for book in first:
        print('Titulo: ' + book['title'] + '  ISBN: ' +
                  book['isbn'] + ' Rating: ' + book['average_rating'] +
                    ' Work text reviews count : ' + book['work_text_reviews_count'])
        
    print("\nLos ultimos libros de la lista son: \n")
    for book in last:
        print('Titulo: ' + book['title'] + '  ISBN: ' +
                  book['isbn'] + ' Rating: ' + book['average_rating'] +
                    ' Work text reviews count : ' + book['work_text_reviews_count'])

def print_best_avg_rating_book(best_book):
    """
    Imprime la información del libro con el average rating más alto de los datos
    """
    print("\nEl libro con el mayor rating promedio es: \n")

    print('Titulo: ' + best_book['title'] + '  ISBN: ' +
                  best_book['isbn'] + ' Work text reviews count : ' + 
                  best_book['work_text_reviews_count'] + '\nCon un rating promedio de: ' + 
                  best_book['average_rating'] )
        

# Se crea el controlador asociado a la vista
control = new_logic()


# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 1:
            print("Cargando información de los archivos ....")
            bk, at, tg, bktg = load_data(control)
            print('Libros cargados: ' + str(bk))
            print('Autores cargados: ' + str(at))
            print('Géneros cargados: ' + str(tg))
            print('Asociación de Géneros a Libros cargados: ' +
                  str(bktg))

        elif int(inputs[0]) == 2:
            number = input("Ingrese el id del libro que desea buscar: ")
            book = logic.get_book_info_by_book_id(control, int(number))
            print_book_info(book)

        elif int(inputs[0]) == 3:
            authorname = input("Nombre del autor a buscar: ")
            author = logic.get_books_by_author(control, authorname)
            print_author_data(author)

        elif int(inputs[0]) == 4:
            label = input("Etiqueta a buscar: ")
            book_count = logic.count_books_by_tag(control, label)
            print('Se encontraron: ', book_count, ' Libros')
        
        elif int(inputs[0]) == 5:
            top = int(input("Ingrese el número de libros que desea imprimir: "))
            first, last = logic.get_first_last_books(control, top)
            print_first_and_last_books(first,last)

        elif int(inputs[0]) == 6:
            best_avg_rating = logic.get_best_avg_rating(control)
            print_best_avg_rating_book(best_avg_rating)

        elif int(inputs[0]) == 0:
            working = False
            print("\nGracias por utilizar el programa.")

        else:
            continue
    sys.exit(0)
