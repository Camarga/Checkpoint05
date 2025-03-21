##Cree un bucle for
city = 'Valencia'

for letter in city:
  print(letter)

#Cree una función llamada suma que tome 3 argumentos y devuelva la suma de los 3
def suma(x, y, z):
  return x + y + z

print(suma(4, 22, 10))

#Cree una función lambda con la misma funcionalidad de la función suma que acaba de crear
suma = lambda x, y, z: x + y + z

print(suma(4, 22, 10))

#Utilizando una lista variable, determine si el valor de la variable coincide o no con un valor de la lista. Si es necesario, utilice un bucle for in y el operador in

#utilizando in
nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']
if nombre in lista_nombre:
  print(f'{nombre} está en la lista')
else:
  print(f'{nombre} no está en la lista')
  
#Utilizando for in
encontrado = False
nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']
for n in lista_nombre:
  if n == nombre:
    encontrado = True
    break

if encontrado:
  print(f'{nombre} está en la lista')
else:
  print(f'{nombre} no está en la lista')


  