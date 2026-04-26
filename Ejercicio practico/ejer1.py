# promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7 
otros_cursos_promeio = 4
dalto = 1.5


# Duracion de crudos

crudo_promedio = 5
crudo_dalto = 3.5

# diferencias de duracion 

diferencia_con_min = 100 - (dalto / otros_cursos_min * 100, 2)
diferencia_con_max = round(100 - dalto  / otros_cursos_max * 100, 2)
diferencia_con_promedio = 100 -  (dalto / otros_cursos_promeio * 100)

# Calculando el porcentaje de tiempo vacio remove
tiempo_vacio_promedio = 100 - otros_cursos_promeio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto * 1000 // crudo_dalto / 10

print("------------------")
# Mostrando las diferencia de duracion del ejercio1
print('El curso de dalto dura: ')
print(f' - un  {diferencia_con_min}% menos que el mas rapido')
print(f' - un  {diferencia_con_max}% menos que el mas lento')
print(f' - un {diferencia_con_promedio}% menos que el mas promedio')
print("------------------")

# Mostrando la cantidad de espacio vacio que se remove ejercio2
print(f'Un curso promedio elimina un  {tiempo_vacio_promedio}% de tiempo vacio ')
print(f'Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio ')
print("------------------")



# Mostrando diferencia si los cursos duran 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promeio * 100 // dalto / 10} horas de otros cursos')
print(f'Ver 10 horas de otros curso equivale a ver {dalto * 100 // otros_cursos_promeio / 10} horas de este cursos')
