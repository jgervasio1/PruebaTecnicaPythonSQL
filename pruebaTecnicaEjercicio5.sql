--punto5
--En esta consulta hacemos un join de la tabla ventas y la tabla stock, y en el select usamos el metodo COALESCE que cumple la funcion de que si el primer valor es NULL lo remplaza por 0
SELECT V.dia,
	   V.articulo,
	   V.local,
       COALESCE(V.unidades_vendidas, 0) AS unidades_vendidas,
       COALESCE(S.unidades_stock, 0) AS unidades_stock
FROM Ventas V
LEFT JOIN Stock S
ON V.dia = S.dia
AND V.articulo = S.articulo
AND V.local = S.local;




