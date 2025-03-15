class Libro:
    # self always is the first parameter in the class
    def __init__(self, titulo, autor, numeroPaginas = 0): # constructor of the class
        self.titulo = titulo # self.titulo is an attribute of the class
        self.autor = autor # self.autor is an attribute of the class
        self.numeroPaginas = numeroPaginas # self.numeroPaginas is an attribute of the class
        self.numeroReferencia = "" # self.numeroReferencia is an attribute of the class
        self.vecesPrestado = 0 # self.vecesPrestado is an attribute of the class
    
    # accessor Autor
    def getAutor(self):
        return self.autor

    # accessor Titulo
    def getTitulo(self):
        return self.titulo
    
    # accessor numeroPaginas
    def getNumeroPaginas(self):
        return self.numeroPaginas

    # print Autor
    def printAutor(self):
        print("El autor del libro es:", self.autor)
    
    # print Titulo
    def printTitulo(self):
        print("El titulo del libro es:", self.titulo)

    # print Details
    def printDetails(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Número páginas:", self.numeroPaginas)
        if self.numeroReferencia != "":
            print("Número referencia:", self.numeroReferencia)
        else:
            print("Sin número de referencia")
        if self.vecesPrestado == 0:
            print("El libro no ha sido prestado")
        else:
            print("El libro ha sido prestado", self.vecesPrestado, "veces")
    
    # set Numero Referencia
    def setNumeroReferencia(self, referencia):
        if len(referencia) >= 3:
            self.numeroReferencia = referencia
        else:
            print("Error: La referencia debe tener al menos 3 caracteres")
    
    # get Numero Referencia
    def getNumeroReferencia(self):
        return self.numeroReferencia

    # prestar
    def prestar(self):
        self.vecesPrestado += 1
    
    # get Veces Prestado
    def getVecesPrestado(self):
        return self.vecesPrestado