# mostra todos os registros de df1
pd.merge(df1, df2, on='key', how='left')

'''
#Resultado
  key   value_x   value_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059       NaN
3   D -1.135632 -0.173215
4   D -1.135632  0.119209
'''