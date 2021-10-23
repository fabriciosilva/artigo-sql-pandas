-- mostra todos os registros de df1
SELECT *
FROM df1
LEFT OUTER JOIN df2
  ON df1.key = df2.key;