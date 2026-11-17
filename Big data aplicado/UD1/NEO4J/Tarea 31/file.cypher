
// =====================================================
// 1. CREAR LOS NODOS (CIUDADES)
// =====================================================

UNWIND [
    'Coruña', 'Vigo', 'Valladolid', 'Oviedo',
    'Bilbao', 'Madrid', 'Badajoz', 'Zaragoza',
    'Barcelona', 'Gerona', 'Valencia', 'Albacete',
    'Murcia', 'Jaén', 'Sevilla', 'Cádiz', 'Granada'
] AS ciudad

MERGE (:Ciudad {nombre: ciudad});


// =====================================================
// 2. CREAR LAS CARRETERAS Y SUS DISTANCIAS
// =====================================================

UNWIND [
    ['Coruña', 'Vigo', 171],
    ['Coruña', 'Valladolid', 455],
    ['Vigo', 'Valladolid', 356],
    ['Oviedo', 'Bilbao', 304],
    ['Valladolid', 'Bilbao', 280],
    ['Valladolid', 'Madrid', 193],
    ['Bilbao', 'Madrid', 395],
    ['Bilbao', 'Zaragoza', 324],
    ['Madrid', 'Zaragoza', 325],
    ['Zaragoza', 'Barcelona', 296],
    ['Barcelona', 'Gerona', 100],
    ['Barcelona', 'Valencia', 349],
    ['Madrid', 'Badajoz', 403],
    ['Madrid', 'Albacete', 251],
    ['Madrid', 'Jaén', 335],
    ['Albacete', 'Valencia', 191],
    ['Albacete', 'Murcia', 150],
    ['Valencia', 'Murcia', 241],
    ['Jaén', 'Granada', 98],
    ['Jaén', 'Sevilla', 242],
    ['Sevilla', 'Cádiz', 125],
    ['Sevilla', 'Granada', 256],
    ['Granada', 'Murcia', 278]
] AS carretera

MATCH (origen:Ciudad {nombre: carretera[0]})
MATCH (destino:Ciudad {nombre: carretera[1]})

MERGE (origen)-[r:CARRETERA]-(destino)
SET r.distancia = carretera[2];


// =====================================================
// 3. MOSTRAR TODAS LAS CIUDADES
// =====================================================

MATCH (c:Ciudad)
RETURN c.nombre AS Ciudad
ORDER BY Ciudad;


// =====================================================
// 4. CONTAR CUANTAS CIUDADES HAY
// =====================================================

MATCH (c:Ciudad)
RETURN COUNT(c) AS Total_Ciudades;


// =====================================================
// 5. MOSTRAR TODAS LAS CARRETERAS Y SUS DISTANCIAS
// =====================================================

MATCH (a:Ciudad)-[r:CARRETERA]->(b:Ciudad)
RETURN
    a.nombre AS Origen,
    b.nombre AS Destino,
    r.distancia AS Distancia_KM
ORDER BY Origen, Destino;


// =====================================================
// 6. CONTAR EL TOTAL DE CARRETERAS
// =====================================================

MATCH ()-[r:CARRETERA]-()
RETURN COUNT(DISTINCT r) AS Total_Carreteras;


// =====================================================
// RETO 1. CIUDAD CON MAYOR NUMERO DE CONEXIONES
// =====================================================

MATCH (c:Ciudad)-[r:CARRETERA]-()
RETURN
    c.nombre AS Ciudad,
    COUNT(DISTINCT r) AS Numero_Conexiones
ORDER BY Numero_Conexiones DESC;


// =====================================================
// RETO 2. CENTRALIDAD DE CERCANIA
// CALCULAR LA MEDIA DE SALTOS ENTRE CIUDADES
// =====================================================

MATCH (c:Ciudad)
MATCH (otra:Ciudad)
WHERE c <> otra

MATCH p = shortestPath(
    (c)-[:CARRETERA*]-(otra)
)

WITH c, AVG(LENGTH(p)) AS Media_Saltos

RETURN
    c.nombre AS Ciudad,
    ROUND(Media_Saltos, 2) AS Media_Saltos

ORDER BY Media_Saltos ASC;


// =====================================================
// RETO 3. EQUILIBRIO ENTRE NORTE Y SUR
// REQUIERE EL COMPLEMENTO APOC
// =====================================================

MATCH (c:Ciudad)

CALL {
    WITH c

    UNWIND [
        'Coruña', 'Vigo', 'Oviedo', 'Bilbao',
        'Valladolid', 'Zaragoza', 'Barcelona', 'Gerona'
    ] AS nombre

    MATCH (destino:Ciudad {nombre: nombre})
    WHERE destino <> c

    CALL apoc.algo.dijkstra(
        c, destino, 'CARRETERA', 'distancia'
    ) YIELD weight

    RETURN SUM(weight) / 8.0 AS Media_Norte
}

CALL {
    WITH c

    UNWIND [
        'Badajoz', 'Jaén', 'Sevilla',
        'Cádiz', 'Granada', 'Murcia'
    ] AS nombre

    MATCH (destino:Ciudad {nombre: nombre})
    WHERE destino <> c

    CALL apoc.algo.dijkstra(
        c, destino, 'CARRETERA', 'distancia'
    ) YIELD weight

    RETURN SUM(weight) / 6.0 AS Media_Sur
}

RETURN
    c.nombre AS Ciudad,
    ROUND(Media_Norte, 2) AS Media_Norte_KM,
    ROUND(Media_Sur, 2) AS Media_Sur_KM,
    ROUND(ABS(Media_Norte - Media_Sur), 2) AS Diferencia

ORDER BY Diferencia ASC;


// =====================================================
// Comando pata la visualización de datos.
// =====================================================


MATCH (c:Ciudad)-[r:CARRETERA]->(d:Ciudad)
RETURN c, r, d;