class Docente:
    def __init__(self, nombre, titulo, experiencia):
        self.nombre = nombre
        self.titulo = titulo
        self.experiencia = experiencia
        
    def enseñar(self):
        print(f"{self.nombre}esta dictando clases")
    
    def mostrar_info(self):
        print(f"{self.nombre} - {self.titulo} - {self.experiencia} exp.")

class Universidad:
    def __init__(self, nombre, ciudad, ranking):
        self.nombre = nombre
        self.ciudad = ciudad
        self.ranking = ranking
        self.docentes = []
        
    def agregar_docente(self, docente):
        self.docentes.append(docente)
        
    def listar_docente(self):
        print(f"Docente de la universidad: {self.nombre}")
        for docente in self.docentes:
            print("-", docente.nombre)


doc1 = Docente("Flavio", "Sistema", 5)
doc1.mostrar_info()

un1 = Universidad("Unemi", "Milagro", "B")
print(un1.nombre)

doc2 = Docente("Jessica", "Tips", "B")

un1.agregar_docente(doc1)
un1.agregar_docente(doc2)
un1.listar_docente()

del un1 #ELIMINAR UNIVERSIDAD
doc1.mostrar_info()
doc2.mostrar_info()
#un1.listar_docente()
#....