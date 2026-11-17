// ============================================================
// TALLER CYPHER: DATASET PONIENTE (JUEGO DE TRONOS)
// 20 ejercicios prácticos - Soluciones
// ============================================================


// ------------------------------------------------------------
// EJERCICIO 01 - Censo por Género
// ------------------------------------------------------------
MATCH (c:Character)
RETURN c.gender AS Genero, COUNT(c) AS Total
ORDER BY Total DESC;


// ------------------------------------------------------------
// EJERCICIO 02 - Miembros de la Casa Stark
// ------------------------------------------------------------
MATCH (c:Character)-[:BELONGS_TO]->(h:House {name: "House Stark"})
RETURN c.name AS Personaje
ORDER BY Personaje ASC;


// ------------------------------------------------------------
// EJERCICIO 03 - Los Asesinos más Letales
// ------------------------------------------------------------
MATCH (c:Character)-[:KILLED]->(victima:Character)
RETURN c.name AS Asesino, COUNT(victima) AS Muertes
ORDER BY Muertes DESC
LIMIT 5;


// ------------------------------------------------------------
// EJERCICIO 04 - Episodios más Concurridos
// ------------------------------------------------------------
MATCH (c:Character)-[:APPEARED_IN]->(e:Episode)
RETURN e.title AS Episodio,
       e.season AS Temporada,
       COUNT(DISTINCT c) AS Personajes
ORDER BY Personajes DESC
LIMIT 5;


// ------------------------------------------------------------
// EJERCICIO 05 - Asentamiento Geográfico de las Casas
// ------------------------------------------------------------
MATCH (h:House)-[:LOCATED_IN]->(l:Location)
RETURN h.name AS Casa, l.name AS Ubicacion
ORDER BY Casa;


// ------------------------------------------------------------
// EJERCICIO 06 - Descendencia Directa de Tywin Lannister
// ------------------------------------------------------------
MATCH (t:Character {name: "Tywin Lannister"})-[:PARENT_OF]->(h:Character)
RETURN h.name AS Hijo;


// ------------------------------------------------------------
// EJERCICIO 07 - Conteo de Casas por Ubicación
// ------------------------------------------------------------
MATCH (h:House)-[:LOCATED_IN]->(l:Location)
RETURN l.name AS Ubicacion, COUNT(DISTINCT h) AS TotalCasas
ORDER BY TotalCasas DESC;


// ------------------------------------------------------------
// EJERCICIO 08 - Personajes sin Afiliación Nobiliaria
// ------------------------------------------------------------
MATCH (c:Character)
WHERE NOT (c)-[:BELONGS_TO]->(:House)
RETURN c.name AS Personaje
ORDER BY Personaje;


// ------------------------------------------------------------
// EJERCICIO 09 - Episodios de la Temporada 1
// ------------------------------------------------------------
MATCH (e:Episode)
WHERE e.season = 1
RETURN e.title AS Episodio, e.episode_number AS Numero
ORDER BY Numero ASC;


// ------------------------------------------------------------
// EJERCICIO 10 - Vínculos Matrimoniales Registrados
// ------------------------------------------------------------
MATCH (a:Character)-[:MARRIED_TO]-(b:Character)
WHERE a.name < b.name
RETURN a.name AS Conyuge1, b.name AS Conyuge2;


// ------------------------------------------------------------
// EJERCICIO 11 - Traición Familiar / Fricción Interna
// ------------------------------------------------------------
MATCH (asesino:Character)-[:KILLED]->(victima:Character),
      (asesino)-[:BELONGS_TO]->(h:House),
      (victima)-[:BELONGS_TO]->(h)
RETURN asesino.name AS Ejecutor,
       victima.name AS Victima,
       h.name AS Casa;


// ------------------------------------------------------------
// EJERCICIO 12 - Cambio de Fidelidad (Transfuguismo)
// ------------------------------------------------------------
MATCH (c:Character)-[:PREVIOUSLY_BELONGED_TO]->(anterior:House),
      (c)-[:BELONGS_TO]->(actual:House)
RETURN c.name AS Personaje,
       anterior.name AS CasaAnterior,
       actual.name AS CasaActual;


// ------------------------------------------------------------
// EJERCICIO 13 - Búsqueda de Sobrinos Directos de Tyrion
// ------------------------------------------------------------
MATCH (tyrion:Character {name: "Tyrion Lannister"})
      -[:SIBLING_OF]-(hermano:Character)
      -[:PARENT_OF]->(sobrino:Character)
RETURN DISTINCT sobrino.name AS Sobrino;


// ------------------------------------------------------------
// EJERCICIO 14 - Letalidad Agregada por Casa Nobiliaria
// ------------------------------------------------------------
MATCH (c:Character)-[:BELONGS_TO]->(h:House),
      (c)-[:KILLED]->(victima:Character)
WITH h, COUNT(DISTINCT victima) AS Muertes
WHERE Muertes >= 5
RETURN h.name AS Casa, Muertes
ORDER BY Muertes DESC;


// ------------------------------------------------------------
// EJERCICIO 15 - Supervivientes Multitemporada
// ------------------------------------------------------------
MATCH (c:Character)-[:APPEARED_IN]->(e:Episode)
WITH c, COUNT(DISTINCT e.season) AS Temporadas
WHERE Temporadas >= 6
RETURN c.name AS Personaje, Temporadas
ORDER BY Temporadas DESC;


// ------------------------------------------------------------
// EJERCICIO 16 - Camino más Corto entre Linajes
// ------------------------------------------------------------
MATCH (d:Character {name: "Daenerys Targaryen"}),
      (a:Character {name: "Arya Stark"})
MATCH p = shortestPath((d)-[*]-(a))
RETURN p;


// ------------------------------------------------------------
// EJERCICIO 17 - Relaciones de Abuelos y Nietos
// ------------------------------------------------------------
MATCH (abuelo:Character)-[:PARENT_OF]->(padre:Character)
      -[:PARENT_OF]->(nieto:Character)
RETURN abuelo.name AS Abuelo,
       nieto.name AS Nieto;


// ------------------------------------------------------------
// EJERCICIO 18 - Capítulos Letales (Recuento por Episodio)
// ------------------------------------------------------------
MATCH (asesino:Character)-[:KILLED]->(victima:Character),
      (victima)-[:APPEARED_IN]->(e:Episode)
WITH e, COUNT(DISTINCT victima) AS Muertes
RETURN e.title AS Episodio,
       e.season AS Temporada,
       Muertes
ORDER BY Muertes DESC
LIMIT 3;


// ------------------------------------------------------------
// EJERCICIO 19 - Casas Huérfanas de Miembros Vivos
// ------------------------------------------------------------
MATCH (c:Character)-[:BELONGS_TO]->(h:House)
WITH h, COLLECT(DISTINCT c) AS Miembros
WHERE ALL(miembro IN Miembros
          WHERE EXISTS {
              MATCH ()-[:KILLED]->(miembro)
          })
RETURN h.name AS Casa;


// ------------------------------------------------------------
// EJERCICIO 20 - Grado de Interconexión Social (Centralidad)
// ------------------------------------------------------------
MATCH (c:Character)
OPTIONAL MATCH (c)-[:PARENT_OF|SIBLING_OF|MARRIED_TO|BELONGS_TO|PREVIOUSLY_BELONGED_TO]-(otro:Character)
WITH c, COUNT(DISTINCT otro) AS Conexiones
RETURN c.name AS Personaje, Conexiones
ORDER BY Conexiones DESC
LIMIT 10;
