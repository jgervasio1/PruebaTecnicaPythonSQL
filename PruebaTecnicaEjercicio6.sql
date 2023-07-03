--punto 6
--En esta consulta lo que hago es hacer un primer where, que me devuelve la fecha pronostico mas grande, mientras que esta cumpla otras condiciones, como por ejemplo que la fecha pronostico sea menor al dia
--y que ademas coincida con los mismo datos de dia, articulo y local
SELECT p1.dia, p1.articulo, p1.local, p1.unidades_pronosticadas, p1.fecha_pronóstico
FROM  pronosticosVentas p1
WHERE p1.fecha_pronostico = (
    SELECT MAX(p2.fecha_pronostico)
    FROM pronosticosVentas p2
    WHERE p2.fecha_pronostico < p1.dia
    AND p2.dia = p1.dia
    AND p2.articulo = p1.articulo
    AND p2.local = p1.local
);