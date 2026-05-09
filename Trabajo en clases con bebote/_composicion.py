class Capitulo:
    def __init__(self, titulo, numero, paginas):
        self.titulo = titulo
        self.numero = numero
        self.paginas = paginas
    
    def mostrar_info(self):
        print(f"Capitulo {self.numero}: {self.titulo} - {self.paginas} pag.")

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        #Forma A
        self.capitulos = [
            Capitulo("Introduccion a la POO",1,20),
            Capitulo("Clases y Objetos", 2, 25)
        ]
        
        #Forma B
        self.capitulos = []
        
    def agregar_capitulos(self, titulo, numero, paginas):
        nuevo_capitulo = Capitulo(titulo, numero, paginas)
        self.capitulos.append(nuevo_capitulo)
    
    def mostrar_info(self):
        print(f"Libro: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")
        
    def mostrar_capitulo(self):
        print("Capitulos")
        for capitulos in self.capitulos:
            capitulos.mostrar_info()
            
libro = Libro( "POO", "Flavio", 2920)

libro.agregar_capitulos("Capitulo 1",1, 25 )
libro.agregar_capitulos("Capitulo 2",2, 26 )


libro.mostrar_capitulo()


del libro
#libro.mostrar_capitulos()

#.....