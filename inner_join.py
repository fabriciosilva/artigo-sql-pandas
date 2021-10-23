# Merge realiza um INNER JOIN por padrão
pd.merge(df1, df2, on='key')

'''
#Resultado
key   value_x   value_y
0   B -0.282863  1.212112
1   D -1.135632 -0.173215
2   D -1.135632  0.119209
'''
  