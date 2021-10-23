SELECT city, rank
FROM df1
UNION ALL
SELECT city, rank
FROM df2;

/*
Resultado:
         city  rank
      Chicago     1
San Francisco     2
New York City     3
      Chicago     1
       Boston     4
  Los Angeles     5
*/