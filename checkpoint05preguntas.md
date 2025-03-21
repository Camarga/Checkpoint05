# **Carolina Martínez García, Checkpoint 5**
---

## **¿Qué es un condicional?
 Los condicionales en Python son estructuras de control que permiten que un programa tome decisiones basadas en ciertas condiciones, según sean verdaderas (True) o falsas (False).
 
 Los condicionales se implementan a traves de las siguientes sentencias:

 1. **if**, que ejecuta el código si la condición es verdadera.
 2. **else**, que ejecuta el bloque de código si la condición es falsa.
 3. **elif**, que permite agregar más condicionales antes de **else** 

 | Operadores |  |
 | --- | ---                    |
 | \== | comparador de igualdad |
  | != | comparador de no igualdad |
 | <> | comparador de no igualdad (este comparador está en desuso, pero lo puedes encontrar en algún código antiguo) |
 | \> |  mayor que |
 | \>= | mayor o igual que |
 | \< | menor que |
 | \<= | menor o igual que |

### **Ejemplo de sentencia _if_**

**if** se utiliza para saber si la condición es verdadera, como por ejemplo, si queremos que deje entrar a una web a un usuario si es mayor de edad 
```python
age = 18
    if age >= 18:
        print('Welcome, you can register')
```

### **Ejemplo de sentencia _else_**

**else** se utiliza para cuando la condición es falsa, como por ejemplo si para el caso anterior quisiéramos dar un mensaje a los menores de edad, que no se pueden registrar
```python
age = 12
    if age >= 18:
        print('Welcome, you can register')
    else:
        print('Sorry, you are underage')
```

### **Ejemplo de sentencia _elif_**

**elif** viene de contraer **else if**, y se usa para poder añadir más condicionales antes de **else**, por ejemplo si en nuestra página queremos que se registren mayores de 18 pero que no sean mayores de 70
```python
age = 80
    if age >= 18:
        print('Welcome, you can register')
    elif age >= 70:
        print("Sorry, you can't register")
    else:
        print('Sorry, you are underage')
```

### **_Operadores ternarios_

Un operador ternario permite crear una sentencia condicional **_if else_**. Con ellos hay que tener más cuidado al usarlos porque son más difíciles de leer si no se implementan de una forma correcta y clara.

Vamos a verlo con el primer ejemplo, queremos que le de paso a registrarse si es mayor de 18, pero que le de el mensaje de que no puede si es menor de 18 años. La sintaxis sería la siguiente:
```python
age = 20

auth = 'Welcome, you can register' if age >= 18 else 'Sorry, you are underage'

print(auth)
```
No obstante, para una mayor claridad del código sería mejor implementarlo con el bloque de código que hemos visto en el _ejemplo de sentencia **else**_

### **Condicionales para _buscar valores_ en nuestro código**

También podemos usar los **condicionales** para saber, por ejemplo, si un valor está dentro de una frase o una lista de números, como por ejemplo:
```python
nums = [20, 40, 60, 80, 100]

if 40 in nums:
    print('The number was found')
else:
    print('The number was not found')
```
Para saber si una palabra está dentro de una frase, por ejemplo:
```python
sentence = 'I love the Medieterranean Sea'
word = 'Mediterranean'

if word in sentence:
    print('The word is in the sentence')
else:
    print('The word is not in the sentence')
```
Si por ejemplo queremos que la busque sin distinción de mayúsculas o minúsculas, usaremos la variable **.lower()**. Por ejemplo:
```python
sentence = 'I love the Medieterranean Sea'
word = 'Mediterranean'

if word.lower() in sentence.lower():
    print('The word is in the sentence')
else:
    print('The word is not in the sentence')
```
### **Condicionales compuestos**

Imaginemos que estamos construyendo la página de inicio de nuestra web o aplicación y queremos permitir el acceso cuando coincida el email y la contraseña. La sintaxis sería la siguiente:
```python
username = 'Carol'
email = 'carol@gmail.com'
password = 'puppy'

if email == 'carol@gmail.com' and password == 'puppy':
    print('Access permitted)
else:
    print('Access denied')
```
Si por ejemplo sólo queremos que coindida uno de los dos datos:
```python
username = 'Carol'
email = 'carol@gmail.com'
password = 'puppy'

if email == 'carol@gmail.com' or password == 'puppy':
    print('Access permitted)
else:
    print('Access denied')
```
Puedes buscar más información sobre condicionales en la página web de [Luis Llamas](https://www.luisllamas.es/)

---
---

## **¿Cuales son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

Los bucles en Python son una herramienta que nos permite **repetir un bloque de código varias veces**, ya sea para un número fijo de veces **(_for_)** o mientras se cumpla una condición **(_while_)**.

### Bucle _for_

El bucle **for** se utiliza para iterar sobre una secuencia (una lista, una tupla, un diccionario, etc.), y ejecutar un bloque de código para cada elemento en esta secuencia.

**Ejemplo de iterar sobre una _colección_:

Podemos iterar el bucle **for** para que nos imprima cada elemento de una lista:
```python
vehicles = ['car', 'bus', 'train']

for vehicle in vehicles:
    print(vehicle)
```
El bucle for ha recorrido la lista **vehicles**, y en cada iteración asigna a cada elemento el valor actual a la variable **vehicle**. Y nos devolverá:
```python
car
bus
train
```

**Ejemplo de iterar en una _cadena_:

```python
word = 'house'
for letter in word:
    print(letter)
```
Aquí el bucle **for** itera sobre cada letra, cada carácter de la cadena de texto **'house'**. En cada iteración, el valor del caracter actual lo asigna a la variable **letter**. Y nos devolverá:
```python
h
o
u
s
e
```

**Ejemplos del bucle **for** en **rangos**

Podemos combinar la función **range()** para iterar sobre una secuencia de números y que ejecute un bloque de código una cantidad predeterminada de veces. 

```python
for num in range(1, 6):
    print(num)
```
En este ejemplo, **range()** genera los números del 1 al 5, el 6 lo excluye, y el bucle **for** recorre los valores y los imprime. Y nos devuelve:
```python
1
2
3
4
5
```
Si quisiéramos que nos los imprimiera en una sola linea, podríamos utilizar **end=" "**:
```python
for num in range(1, 6):
    print(num, end=" ")
```
Y nos devolvería:
```python
1 2 3 4 5
```
Si queremos que, en este mismo ejemplo, nos devuelva los números contando de dos en dos, utilizaremos tres elementos:
```python
for num in range(1, 6, 2):
    print(num, end=" ")
```
Generará los números aumentándolos en pasos de dos, y nos devolverá:
```python
1 3 5
```


Si por ejemplo queremos imprimir una lista numerada, podemos utilizar, además de la función range(), la función **len()**, de la siguiente manera:
```python
name = ['Raul', 'María', 'Sheila']

for name in range(len(names))
    print(f'Puesto {name}: {names[name]}')
```
len() devuelve la cantidad de elementos que hay en la lista, range(len()) genera los índices, del 0 al 2, permitiendo así acceder a los elementos de la lista por su posición. Y nos devolverá:
```python
Puesto 0: Raul
Puesto 1: María
Puesto 2: Sheila
```

Si quieres ver más sobre el bucle **for**, pincha [aquí](https://r.search.yahoo.com/_ylt=AwrNZG0A29tnnoMz5VK9.Qt.;_ylu=c2VjA2NkLWF0dHIEc2xrA3NvdXJjZQR2dGlkAwRydXJsA2h0dHBzOi8vd3d3LnlvdXR1YmUuY29tL3dhdGNoP3Y9eFpTdUQ5cWR6U00-/RV=2/RE=1742490496/RO=10/RU=https%3a%2f%2fwww.youtube.com%2fwatch%3fv%3dxZSuD9qdzSM/RK=2/RS=WR8f5ZzP8lqIclghYc5uxWAtaig-)

### **Bucle _while_**

Como decíamos anteriormente, el bucle **while** se utiliza para repetir un bloque de código mientras (while) una condición sea verdadera.
Es importante tener mucho cuidado al utilizar el bucle while, ya que si la condición nunca se devuelve falsa, el bucle se ejecutará indefinidamente. Tenemos que decirle siempre cuándo detenerse, de no ser así crearíamos un bucle infinito y se podría bloquear el programa.
Debemos otorgarle un **valor centinela**, que es donde parará.

Si quieres más información sobre el bucle **wile**, puedes ver un vídeo pinchando [aquí](https://r.search.yahoo.com/_ylt=AwrNZG2U2dtnlLUz_Aa9.Qt.;_ylu=c2VjA2NkLWF0dHIEc2xrA3NvdXJjZQR2dGlkAwRydXJsA2h0dHBzOi8vd3d3LnlvdXR1YmUuY29tL3dhdGNoP3Y9dHNzNVFwWnFBMUk-/RV=2/RE=1742490132/RO=10/RU=https%3a%2f%2fwww.youtube.com%2fwatch%3fv%3dtss5QpZqA1I/RK=2/RS=UmxC0zum94s4PYKuJPM88SRHqYE-)

Para controlar dónde tiene que parar, o donde puede continuar, tenemos **_break_** y **_continue_**.

**Ejemplo con _break_

```python
frutas = ['pera', 'melón', 'piña', 'manzana', 'platano']

for fruta in frutas:
    print(fruta)
    if fruta == 'manzana':
        break
```
En este ejemplo el bucle for imprimirá cada fruta hasta que llegue a **'manzana'**, porque en ese momento se ejecuta **_break_** y el bucle se interrumpe. Y nos devolverá:
```python
pera
melón
piña
manzana
```

**Ejemplo con _continue_
```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)
```
Aquí el bucle **for** itera sobre la lista **numbers**, y cuando encuentra un número par, divisible por 2, se ejecuta **_continue_**, y nos devuelve:
```python
2
4
```

Los bucles en Python son útiles porque evitan repetir código manualmente y trabajar muy rápido con grandes cantidades de datos de código. Otra razón de por qué son tan útiles es que se pueden combinar con condicionales para realizar tareas más avanzadas. Además son fundamentales en programación, son la base de estructuras como algoritmos de búsqueda, procesamiento de datos y aprendizaje automático.

---
---

## **¿Qué es una lista por comprensión en Python?

Las listas por comprensión en Python son una forma concisa de crear otras listas a partir de otros elementos iterables. Se considera una de las contracciones más elegantes del lenguaje.

Veamos la sintaxis que utiliza con un ejemplo, vamos a crear una lista de números que devuelve los números al cuadrado de la lista de una variable a la que llamaremos **_numbers_**

```python
numbers = [1, 2, 3, 4, 5]

result = [num**2 for num in numbers]
print(result)
```
Lo que nos devolvería:
```python
[1, 4, 9, 15, 25]
```

También podríamos utilizarla sobre un **rango** e incluso añadiéndole **condicionales**. 

Imaginemos que queremos que nos imprima una lista, del resultado de multiplicar al cuadrado un rango, pero sólo de los números pares:

```python
result = [num**2 for num in range(1, 6) if num % 2 == 0]
print(result)
```
Y nos devolvería
```python
[4, 16]
```

Las listas de comprensión son más **concisas** y **legibles**, y su rendimiento es **más eficiente** que un _for_ tradicional.

Evitan tener que utilizar **.append()**. 

Para ver la diferencia entre la lista de comprensión y un bloque de codigo, que devolvería el mismo resultado, pero sería más difícil de leer, veamos cómo sería el primer ejemplo utilizando **append**

```python
numbers = [1, 2, 3, 4, 5]
result = []

for num in numbers:
    result.append(num ** 2)

print(result)
```

Lo que nos devolvería, como en el primer ejemplo:
```python
[1, 4, 9, 15, 25]
```

Pero como se puede observar, es mucho más claro nuestro primer ejemplo que este último, es por esto que se dice que las listas de comprensión en Python son más **concisas** y **legibles**, además de elegantes.

También podemos utilizar las listas de comprensión para que nos cree una lista de los **elementos repetidos en dos listas**. Por ejemplo, si tenemos dos listas con nombres de usuarios y queremos que nos indique cuáles son los nombres que se repiten en las dos listas:

```python
names_one = ['Monica', 'Montse', 'Lorena', 'Elena', 'Alicia', 'Maribel']
names_two = ['Rosa', 'Susana', 'Monica', 'Maribel', 'Aroa']

repeated_names = [name for name in names_one for girl in names_two if name == girl]

print(repeated_names)
```
Nos devolvería
```python
['Monica', 'Maribel]
```

Imaginemos que ahora queremos que nos devuelva una lista, de una variable que tenemos llamada _names_, pero que los imprima en **MAYÚSCULA**, utilizaremos **.upper()**:

```python
names = ['Monica', 'Montse', 'Maribel']
capital_letters = [name.upper() for name in names]

print(capital_letters)
```
Imprimirá:
```pyton
['MONICA', 'MONTSE', 'MARIBEL']
```

Si por ejemplo quisieramos **combinar** dos listas:

```python
names_one = ['Montse', 'Lorena', 'Elena', 'Alicia']
names_two = ['Rosa', 'Monica', 'Maribel', 'Aroa']

girls = [name for name in names_one] + [girl for girl in names_two]

print(girls)
```
Y nos devolvería
```python
['Montse', 'Lorena', 'Elena', 'Alicia', 'Rosa', 'Monica', 'Maribel', 'Aroa']
```

Si quieres ver más ejemplos acerca de listas de comprensión, pincha [aquí](https://r.search.yahoo.com/_ylt=Awr.gBRV7ttn_wEAeupU04lQ;_ylu=Y29sbwNpcjIEcG9zAzEEdnRpZAMEc2VjA3Ny/RV=2/RE=1743676246/RO=10/RU=https%3a%2f%2fcodigospython.com%2flistas-por-comprension-en-python-explicacion-y-ejemplos%2f/RK=2/RS=RdSJiqQF1zwuxvLH66xtEa5oLMA-)

---
---
## **¿Qué es un argumento en Python?

Los argumentos son los valores que pasamos a una función, para que los utilice cuando se le llama. Los argumentos hacen que las funciones sean más flexibles y reutilizables.

Una función en Python se implementa con la palabra **_def_** seguida de un **parámetro definido**, osea el nombre con la que la queremos identificar, y a continuación **entre paréntesis** los **_argumentos_**, los parámetros.

```python
def nombre_de_la_funcion(parametro1, parametro2, ...):
    # bloque de código de la función que utiliza los parámetros
```

Veamos con un ejemplo por el cual queremos imprimir un saludo a un usario poniendo la edad que tiene. Tendríamos una función *def* a la que llamaríamos *greeting* y a la que le daríamos unos argumentos de nombre y edad, *name* y *age*:

```python
def greeting(name, age):
    print(f'Hello {name}, you are {age} years old')

greeting('Marta', 55)
```
Y nos imprimirá:
```python
Hello Marta, you are 55 years old
```

Acabamos de ver un ejemplo de **_argumentos posicionales_**, veamos más **tipos de argumentos**.

### Argumentos con *valores predeterminados*

En las definiciones de las funciones con este tipo de argumentos, éstos tienen un valor asignado por defecto. Vamos a ver un ejemplo muy básico:

```python
def greeting(name, greet = 'Hello'):
    print(f'{greet}, {name}')

greeting('Monica')
```
Y nos devolvería
```python
Hello, Monica
```
Es muy importante que, si ponemos un argumento con valores predeterminados, éste **vaya en la última posición** como en el ejemplo que hemos visto, si no, nos devolverá un error.

### Argumentos con valores predeterminados en elementos **mutables**

Esta forma de argumentos es un tanto peligrosa, de hecho Repl cuando la usas te advierte con una señal.

No conviene que un tipo de dato mutable como por ejemplo una lista o un diccionario, sea el argumento predeterminado. Vamos a verlo con un ejemplo. Crearemos una función que se llame *some_function* y le pasaremos como argumento predeterminado un valor predeterminado que sea una lista. Luego le diremos que queremos que añada el elemento 1 a la lista:

```python
def some_function(collection = []):
    collection.append(1)
    return collection

print(some_function())
```
Este bloque de código devolvería
```
[1]
```

Pero si por ejemplo tuviéramos que llamar a esta función desde cualquier otra parte del programa, creyendo que el valor que pase devuelto será el mismo, tendremos un problema.

Al ser nuestro argumento mutable, nuestra colección que ha quedado en la memoria es **[1]**. Al llamar a la función desde otra parte del programa, o incluso desde otro archivo diferente, la lista no se vuelve a inicializar a **[]**, mantendrá el valor **[1]** de la lista anterior

```python
def some_function(collection = []):
    collection.append(1)
    return collection

print(some_function())

# Desde otra parte del programa:
print(some_function())
```
Este *print* devolvería
```
[1]
[1, 1]
```

Por esto es por lo que se considera una **mala práctica en Python** utilizar una lista (o cualquier otro objeto mutable), porque todas las llamadas posteriores a dicha función compartirán la misma lista, lo que puede llevar a errores difíciles de detectar.

### Argumentos con nombre

Los argumentos con nombre, son los que se pasan a la función utilizando su nombre.

Esto permite cambiar el orden de los argumentos, o incluso cambiar alguno de ellos. 

Vamos a verlo con un ejemplo, donde también queremos imprimir un saludo.

```python
def saludar(nombre, saludo="Hola")
    print(saludo + ',', nombre)

saludar(nombre='Monica')
saludar(saludo='Buenos días', nombre='Jose')
```
En la segunda llamada a la función, hemos cambiado el nombre al saludo, lo que nos devolvería:

```python
Hola, Monica
Buenos días, Jose
```

### Argumentos posicionales de longitud variable, ***args**

Utilizamos la función ***args** cuando queremos pasar a una función cualquier cantidad de argumentos posicionales. Y todo esto lo almacenará como una *tupla*.

Por ejemplo, si tienes una función que debe ser metida en una colección de datos, seguramente no sabrás cuántos elementos tienes,  si tienes 20 o 500 elementos. No podríamos hacer simplemente una lista de elementos.

Vamos a ver un ejemplo en el que necesitamos varios argumentos, una función de saludo, greeting, la cual cuando llamemos, imprimirá un formato que le habremos dado con *print* más los argumentos que le hayamos pasado al llamar a la función, sean uno o diez:

```python
def greeting(*args):
    print('Hi ' + ' '.join(args))


greeting('Marta', 'Rodriguez')
```
Lo que nos devolverá:

```python
Hi Marta Rodriguez
```

***args** es una función de desmpaquetado. Después, al decirle **' '.join(args)**, llamará a la función y pasará los argumentos que le implementemos cuando la estemos llamando en nuestro código.

### Argumentos de palabra clave de longitud variable, ****kwargs**

Con la función *kwargs podemos pasar una cantidad variable de argumentos con nombre, argumentos de palabra clave (keyword arguments).

Se almacenará en un diccionario donde las claves son los nombres de los argumentos y los valores serán los que le pasemos al llamar a la función.

Veamos un ejemplo básico de cómo utilizarlo. 
```python
def greeting(**kwargs):
    print(kwargs)

greeting(name = 'Marta', last_name = 'Rodriguez')
```
Y nos devolverá un diccionario:

```python
{'name': 'Marta', 'last_name': 'Rodriguez'}
```
También podemos usar *args y **kwargs combinados para una misma función, por ejemplo:

```python
def combine(*args, **kwargs):
    print('numbers:', args)
    print('names:', kwargs)

combine(1, 2, 3, name = 'James', surname = 'Manchester')
```
Y nos devolverá:
```python
numbers: (1, 2, 3)
names: {'name': 'James', 'surname': 'Manchester'}
```

Si quieres ver más acerca de los argumentos ***args** y ***kwargs** visita este [video](https://r.search.yahoo.com/_ylt=AwrNZG1bMd1ncAcLEWW9.Qt.;_ylu=c2VjA2NkLWF0dHIEc2xrA3NvdXJjZQR2dGlkAwRydXJsA2h0dHBzOi8vd3d3LnlvdXR1YmUuY29tL3dhdGNoP3Y9X25BdW84SnNBY00-/RV=2/RE=1742578139/RO=10/RU=https%3a%2f%2fwww.youtube.com%2fwatch%3fv%3d_nAuo8JsAcM/RK=2/RS=RpRKf6K3lxb6fkE8ski1gdp8p3g-)

---
---

## **¿Qué es una función *Lambda* en Python?

La función **lambda** en Python, es una herramienta que te permite encapsular una función, para poder pasarla luego fácilmente a otras funciones.

Es una forma concisa y fácil de definir una función sin tener que utilizar **_def_**. Además te permite finalizar un proceso.

Vamos a verlo con un ejemplo en el que queremos hacer una operación matemática:

```python
suma = lambda x, y: x + y

resultado = suma(10, 25)

print(resultado)
```
Lo que nos devolverá el resultado de la operación:
```python
35
```

### Diferencias entre la función lambda y una función definida

- Las funciones **lambda** son muy útiles cuando queremos una función rápida para una operación simple. Se pueden utilizar con otras funciones como *map()*, *filter()* y *reduce()*.

- La sintaxis de una función **lambda** tiene que ser sencilla y no puede tener varias líneas de código.

- No hay que abusar de la función **lambda** porque pueden hacer que tu código no sea tan fácil de leer.

- Con la función **lambda** puede ser más difícil depurar funciones, en comparación con las funciones definidas con nombres explícitos.

En resumen, son muy prácticas para operaciones sencillas pero no combiene utilizarlas mucho para el buen funcionamiento y una fácil lectura del código.

---
---

## **¿Qué es un paquete *pip*?

Python puede hacer muchas cosas muy buenas por sí solo, pero como desarrollador vas a necesitar paquetes adicionales, bibliotecas, para hacerte la vida más fácil.

Pip es un instalador de paquetes para Python. Es una herramienta que te permite gestionar los muchos paquetes de Python con los que te vas a encontrar.

Voy a dar un ejemplo con el que es muy fácil entenderlo:

Imagina que has comprado una caja de herramientas (Python),  que viene con un montón de herramientas (paquetes, bibliotecas), si necesitas cualquiera de estas herramientas sólo tienes que abrir la caja y cogerla (importar una biblioteca).

Pero estás trabajando y necesitas una herramienta que no tienes en tu caja, tendrás que conseguirla de otra manera. Así que puedes estar trabajando con Python y encontrarte que necesitas más herramientas, más paquetes, osea más bibliotecas.

Afortunadamente en internet puedes encontrar muchísimos paquetes, para todo tipo de propósitos, que han sido desarrollados por desarrolladores profesionales que trabajan con Python.

Y el repositorio más grande, y aceptado por la comunidad de Python, donde muchos de estos desarrolladores han almacenado sus paquetes es el Indice de Paquetes de Pyton (PyPi). 

Teniendo instalado **_pip_**, gestionará todos estos paquetes.

Las últimas versiones de Python ya incluyen **pip** por defecto.

**Pip** utiliza como repositorio por defecto **PyPi** para obtener los paquetes, pero puede utilizar otras fuentes como 
GitHub o Mercurial.

Asegúrate de que tienes instalado **pip** poniendo en tu terminal
```PowerShell
C:\>pip --version
```




