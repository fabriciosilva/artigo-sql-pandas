SELECT city, rank
FROM df1
UNION
SELECT city, rank
FROM df2;

-- notice that there is only one Chicago record this time
/*
         city  rank
      Chicago     1
San Francisco     2
New York City     3
       Boston     4
  Los Angeles     5
*/