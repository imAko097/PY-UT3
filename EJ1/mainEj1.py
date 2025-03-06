from libro import Libro # import the class Libro from the file libro.py

def main():
    libro1 = Libro("El Quijote", "Cervantes") # create an object of the class Libro
    print("El autor del libro es:", libro1.getAutor()) # call the method getAutor from the object libro1
    print("El titulo del libro es:", libro1.getTitulo()) # call the method getTitulo from the object libro1

    print('-----------------------------')

    libro2 = Libro("El Señor de los Anillos", "Tolkien")
    print("El autor del libro es:", libro2.getAutor())
    print("El titulo del libro es:", libro2.getTitulo())

    print('-----------------------------')


    libro3 = Libro("El código Da Vinci", "Dan Brown")
    libro3.printAutor()
    libro3.printTitulo()

    print('-----------------------------')


    libro4 = Libro("Harry Potter", "J.K. Rowling", 300)
    libro4.printDetails()

    print('-----------------------------')

    libro5 = Libro("Kamasutra", "Vatsyayana", 200)
    libro5.setNumeroReferencia("123")
    libro5.printDetails()
    libro5.prestar()
    libro5.prestar()
    libro5.prestar()
    libro5.printDetails()

if __name__ == "__main__":
    main() # call the main function