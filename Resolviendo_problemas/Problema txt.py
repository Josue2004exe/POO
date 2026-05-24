# 2 listas, una con nombres otra con apellidos
nombres = ["Flavio", "Gorge", "Julio", "Freddy", "Carla"]
apellidos = ["Morales", "Martin", "Vera", "Gonzales", "Monte"]


#Registrar esta info en un txt de forma optima 
with open("Resolviendo_problemas\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son: \n\n")
    [arch.writelines(f"Nombres: {n}\nApellido: {a}\n-------------\n") for n,a in zip(nombres, apellidos)]

