# Evaluación de capacidades de una IA generativa

**IA bajo análisis:** Google Gemini


## 1. Razonamiento lógico
### Prompt utilizado: Acertijo de RRSS.

Cuatro personas tienen que cruzar un puente de noche. Solo disponen de una linterna y el puente soporta como máximo a dos personas al mismo tiempo. Cada persona tarda 1, 2, 7 y 10 minutos en cruzar, respectivamente. Cuando cruzan dos personas juntas, avanzan a la velocidad de la más lenta. La linterna siempre debe acompañar a quienes cruzan.
¿Cuál es el tiempo mínimo necesario para que las cuatro personas crucen el puente? Explica los pasos y justifica por qué tu solución es óptima.

### Respuesta de Google Gemini:
**Tiempo mínimo necesario: 17 minutos.**

Gemini propone los siguientes movimientos:

1. Las personas de 1 y 2 minutos cruzan juntas. Tiempo acumulado: 2 minutos.
2. La persona de 1 minuto regresa con la linterna. Tiempo acumulado: 3 minutos.
3. Las personas de 7 y 10 minutos cruzan juntas. Tiempo acumulado: 13 minutos.
4. La persona de 2 minutos regresa con la linterna. Tiempo acumulado: 15 minutos.
5. Las personas de 1 y 2 minutos cruzan juntas por última vez. Tiempo total: 17 minutos.

Gemini justifica que las dos personas más lentas deben cruzar juntas para evitar que sus tiempos se sumen por separado y que las personas más rápidas deben encargarse de los viajes de regreso.

### Análisis de la respuesta:
La respuesta es correcta. La secuencia propuesta permite que las cuatro personas crucen respetando todas las restricciones del problema y el tiempo total de 17 minutos es el mínimo posible. Gemini explica los movimientos de la linterna y muestra el tiempo acumulado después de cada paso, lo que facilita comprobar sus operaciones y seguir su lógica.
Como limitación, la justificación de que la solución es óptima es breve. Aunque la secuencia es válida, la explicación podría demostrar de forma más rigurosa por qué otras estrategias, como hacer regresar siempre a la persona más rápida, no mejoran el resultado.

**Conclusión:** Gemini demuestra una buena capacidad para resolver un problema de razonamiento y organizar una solución paso a paso que, además, es correcta (Entendiendo correcta como la respuesta a un acertijo, en este caso.)



## 2. Cálculo matemático
### Prompt utilizado:

Una persona compra un ordenador por 849,90 €, unos auriculares por 59,95 € y un teclado por 74,50 €. La tienda aplica un descuento del 12 % sobre el precio total y, después, añade unos gastos de envío de 8,99 €. Todos los precios indicados antes del descuento incluyen el IVA.

¿Cuánto debe pagar finalmente? Muestra todas las operaciones y redondea a dos decimales al final.

### Respuesta de Google Gemini:
**1. Cálculo del subtotal**

- Ordenador: 849,90 €.
- Auriculares: 59,95 €.
- Teclado: 74,50 €.

Subtotal:

849,90 + 59,95 + 74,50 = 984,35 €.

**2. Aplicación del descuento del 12 %**

Descuento:

984,35 × 0,12 = 118,122 €.

Importe con descuento:

984,35 − 118,122 = 866,228 €.

**3. Gastos de envío**

Gemini señala que no es necesario volver a calcular el IVA, ya que los precios indicados ya lo incluyen.

Importe final:

866,228 + 8,99 = 875,218 €.

Redondeando a dos decimales, el resultado es **875,22 €**.

### Análisis de la respuesta:
Gemini identifica correctamente las operaciones necesarias y aplica el descuento al subtotal de los tres productos. También entiende que los gastos de envío se añaden después del descuento y que no debe volver a aplicar el IVA.
El resultado final es correcto. Sin embargo, en su respuesta original redondea el descuento a 118,12 € antes de continuar con una de las operaciones. Esto contradice parcialmente la instrucción de redondear únicamente al final, aunque obtiene el mismo resultado en este caso.
Para respetar estrictamente la instrucción, es preferible conservar los decimales durante todos los cálculos y redondear solo el importe final. (El "examinador" en este caso podría, quizá, haber sido más estricto en su prompt.)

**Conclusión:** Gemini obtiene el resultado correcto y explica adecuadamente el procedimiento, aunque podría seguir las instrucciones de redondeo con mayor rigor.


## 3. Interpretación de imágenes
### Prompt utilizado:

Analiza la imagen adjunta. Identifica los objetos que aparecen, describe sus características visibles y cuenta cuántos hay de cada tipo. Indica también su posición aproximada dentro de la imagen.
Después, intenta determinar de qué material están hechos y cuánto pesa cada objeto. Distingue claramente entre lo que puedes observar directamente, lo que puedes inferir y lo que no puedes determinar únicamente a partir de la imagen. No inventes datos para completar la respuesta.

### Respuesta de Google Gemini:
Gemini identifica la imagen como una ilustración digital de estilo "Concept art", realizada en escala de grises, que representa un paisaje monumental de aspecto fantástico o futurista.

**Elementos identificados:**

- **Figuras humanas:** identifica dos personajes situados en la zona inferior central de la imagen, vistos de espaldas y observando el paisaje. Describe su vestimenta como capas, prendas de exploración o posibles protecciones.
- **Estructuras monumentales:** identifica entre tres y cuatro formaciones principales, entre ellas un gran pilar en el lado izquierdo, una estructura diagonal que atraviesa la parte superior y una formación rocosa o muro en el lado derecho.
- **Terreno y fragmentos:** observa numerosos bloques y superficies angulares distribuidos por el suelo, aunque reconoce que no es posible establecer su cantidad exacta.

**Características visuales:**

Gemini describe correctamente la escala de grises, el contraste entre zonas claras y oscuras, las formas angulares y la composición general del paisaje. También señala que las figuras están de espaldas y que no se distinguen sus rostros.

**Inferencias realizadas:**

La IA plantea que las estructuras podrían representar piedra, hormigón o metal futurista, mientras que la vestimenta podría estar compuesta por telas gruesas o elementos de protección. Asimismo, interpreta el entorno como un escenario fantástico, alienígena o distópico.
Gemini aclara que estas interpretaciones son inferencias y no hechos que puedan confirmarse únicamente a partir de la imagen.

**Limitaciones reconocidas:**

- No es posible determinar el peso exacto de los personajes, las rocas o las estructuras.
- No se pueden confirmar los materiales representados, puesto que la imagen es una ilustración y no una fotografía de objetos físicos.
- No es posible conocer los colores originales de un hipotético escenario en color.
- No se pueden identificar rasgos faciales concretos de los personajes, ya que aparecen de espaldas.

### Análisis de la respuesta
La respuesta de Gemini es detallada y está bien organizada. La IA identifica correctamente los dos personajes principales y describe de forma coherente el entorno, las estructuras monumentales y los fragmentos del terreno.
Uno de los aspectos más positivos es que distingue entre observaciones directas e inferencias. Por ejemplo, describe las formas angulares y la escala de grises como características visibles, mientras que presenta los materiales y la naturaleza del escenario como interpretaciones posibles.
También reconoce correctamente que no puede determinar el peso exacto de los elementos a partir de una ilustración bidimensional. Esta cautela evita que proporcione cifras inventadas para completar la respuesta.
Sin embargo, hay algunas limitaciones. La cantidad de estructuras principales se expresa como una estimación de tres o cuatro elementos, lo que muestra que la clasificación depende de cómo se interpreten las formaciones del paisaje. Además, las referencias a materiales como el hormigón o el metal futurista son especulativas y no pueden verificarse visualmente.
La afirmación de que la imagen no permite conocer los colores originales es razonable: la ilustración mostrada está en escala de grises, por lo que no ofrece información suficiente para reconstruir una hipotética versión en color.

**Conclusión:** Gemini demuestra una buena capacidad para describir e interpretar una imagen compleja. Destaca especialmente por organizar la información visual y reconocer sus limitaciones, aunque algunas de sus interpretaciones sobre los materiales y el entorno son inferencias que no deben confundirse con hechos confirmados.



## 4. Instrucciones ambiguas
### Prompt utilizado:
Necesito una aplicación para gestionar las notas de mis alumnos. Quiero que sea sencilla de utilizar y que me ayude a organizar la información. Prepara una propuesta de programa para resolver este problema.

### Respuesta de Google Gemini
Gemini propone desarrollar un modelo inicial de aplicación, denominado versión 0.1, partiendo de algunos supuestos razonables.

**Supuestos iniciales:**
- La herramienta debe ser ligera y sencilla.
- Estará orientada a un profesor individual.
- Podría desarrollarse como una aplicación web con Python y Streamlit o como un programa estructurado.

**Estructura de datos propuesta:**
- Alumnos: identificador, nombre, apellidos y grupo.
- Asignaturas y evaluaciones: materia y peso de exámenes, prácticas y participación.
- Calificaciones: notas vinculadas a cada alumno y actividad.

**Funciones básicas:**
1. Cargar y consultar la lista de alumnos.
2. Introducir y modificar notas por trimestre o evaluación.
3. Calcular automáticamente la media ponderada.
4. Exportar los datos a CSV o Excel.

Finalmente, Gemini pregunta si se prefiere una interfaz web, una hoja de cálculo automatizada o un programa de escritorio.

### Análisis de la respuesta:
La respuesta es adecuada porque Gemini identifica las necesidades más habituales de una aplicación de gestión académica y propone una solución inicial organizada.
También reconoce que faltan requisitos importantes y termina formulando una pregunta para concretar el tipo de aplicación deseada.
Sin embargo, toma algunas decisiones sin consultar previamente al usuario, como sugerir Python y Streamlit o asumir que el programa estará destinado a un único profesor. Son hipótesis razonables, pero no requisitos confirmados. Esto podría deberse a que esta IA ya ha trabajado con el usuario (El "examinador") con Pythin y, en cierto modo, son respuestas sesgadas por su historial.
Además, podría haber preguntado por aspectos como la escala de las notas, el número de alumnos, la necesidad de guardar datos de forma permanente y los requisitos de privacidad.

**Conclusión:** Gemini gestiona correctamente una instrucción ambigua, propone una solución útil y explicita algunos de sus supuestos, aunque podría aclarar más requisitos antes de recomendar una tecnología concreta, teniendo en cuenta, de nuevo, que estas sugerencias podrían deberse al historial de peticiones del usuario previas a este examen.

## 5. Conocimiento de hechos
### Prompt utilizado:

En 1969 se produjo un acontecimiento importante en la historia de la informática: el envío del primer mensaje entre dos ordenadores de ARPANET.
¿Qué dos instituciones estaban conectadas cuando se envió ese primer mensaje, qué palabra se pretendía transmitir y qué ocurrió realmente durante el intento? Explica brevemente la importancia de este acontecimiento para el desarrollo de Internet.

### Respuesta de Google Gemini:
Gemini proporciona los siguientes datos:

- **Instituciones:** la Universidad de California en Los Ángeles (UCLA) y el Stanford Research Institute (SRI).
- **Mensaje previsto:** la palabra «LOGIN».
- **Fallo:** el sistema dejó de funcionar después de transmitir las dos primeras letras, «LO».
- **Fecha:** 29 de octubre de 1969.
- **Importancia:** el acontecimiento marcó un hito en las comunicaciones entre ordenadores mediante conmutación de paquetes y en la evolución posterior de ARPANET e Internet.

### Análisis de la respuesta:
La respuesta es correcta en sus aspectos principales. Gemini identifica las instituciones implicadas, la palabra que se intentó transmitir, el fallo ocurrido y la fecha del acontecimiento.
También explica de forma comprensible la relevancia histórica del experimento, relacionándolo con el desarrollo de las redes informáticas.
Como mejora, podría distinguir con mayor precisión entre ARPANET e Internet. ARPANET fue una red pionera que contribuyó a la evolución de Internet, pero no era exactamente lo mismo que la Internet moderna.

**Conclusión:** Gemini demuestra un buen conocimiento de este acontecimiento histórico y proporciona una explicación coherente. Para una evaluación rigurosa, sus datos deben contrastarse con fuentes históricas fiables.

## 6. Conclusión general
Después de analizar las cinco pruebas, se pueden extraer las siguientes conclusiones sobre el comportamiento de Google Gemini.

### 6.1. Mejores resultados
Gemini ha obtenido buenos resultados en las pruebas de razonamiento lógico, cálculo matemático e interpretación de imágenes. Ha explicado los procedimientos utilizados y ha identificado correctamente los elementos principales de la ilustración.
En la prueba de conocimiento de hechos también ha proporcionado los datos fundamentales sobre el primer mensaje de ARPANET en 1969, sin entrar en demasiados detalles.

### 6.2. Limitaciones detectadas
En el cálculo matemático, el resultado final es correcto, aunque la respuesta no sigue de forma completamente estricta la instrucción de redondear únicamente al final.
En la interpretación de imágenes, Gemini ha descrito correctamente la escena, pero algunas de sus afirmaciones sobre los materiales y el tipo de entorno son inferencias. En la prueba de instrucciones ambiguas, ha propuesto una solución útil, aunque ha asumido algunas características de la aplicación sin confirmarlas previamente.

### 6.3. Explicación de los procedimientos
En general, Gemini explica sus respuestas en lugar de limitarse a proporcionar resultados. Esto permite comprobar los cálculos, revisar los movimientos del problema lógico y distinguir las observaciones visuales de las interpretaciones.
No obstante, explicar un procedimiento no garantiza que sea completamente correcto, por lo que conviene verificar sus resultados.

### 6.4. Reconocimiento de las limitaciones
La prueba visual muestra que Gemini reconoce que no puede determinar con exactitud el peso de los objetos ni confirmar sus materiales a partir de una ilustración. También diferencia los elementos visibles de las características que solo puede inferir.
Este comportamiento es positivo porque evita presentar todas sus interpretaciones como certezas.

### 6.5. Gestión de instrucciones ambiguas
Gemini ha elaborado una propuesta inicial para gestionar las notas de los alumnos y ha solicitado una aclaración sobre el tipo de aplicación deseada. Esto demuestra que puede ofrecer una solución provisional cuando faltan requisitos, aunque podría formular más preguntas antes de elegir una tecnología concreta.

### 6.6. Fiabilidad de las respuestas
Los resultados indican que Gemini puede ser útil para resolver problemas, realizar cálculos, interpretar imágenes y organizar información. Sin embargo, también muestra que algunas respuestas pueden contener pequeñas desviaciones respecto a las instrucciones o interpretaciones que no se pueden confirmar.
Por ello, es recomendable comprobar los resultados matemáticos, contrastar los hechos históricos y diferenciar las observaciones visuales de las inferencias.

### Valoración final
En conjunto, Google Gemini ha mostrado un rendimiento satisfactorio en las cinco pruebas realizadas. Sus principales fortalezas han sido la organización de las respuestas, la explicación de los procedimientos y el reconocimiento de algunas de sus limitaciones, lo que ha hecho notablemente más sencillo la redacción y edición de este documento y los datos exppuestos en este.
Las pruebas muestran que una IA puede proporcionar respuestas detalladas sin que todos sus elementos tengan el mismo grado de certeza. Por tanto, es importante analizar críticamente sus resultados y verificar la información antes de aceptarla como correcta.
Esta conclusión no es exclusiva de Google Gemini, pues es de gran importancia supervisar, revisar, valorar de forma crítica y analítica cuañquier fragmento de información proporcionado por una IA, al igual que hace no tantos años se sugería que toda la información obtenida mediante fuentes de internet, como wikipedia o foros.