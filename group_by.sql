SELECT sex, count(*)
FROM tips
GROUP BY sex;

/*
Resultado:
Female     87
Male      157
*/