df1 = pd.DataFrame({'fruta': ['maçã', 'laranja', 'pera', 'pêssego'], 'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'alimento': ['maçã', 'pão', 'pera', 'pêssego'], 'value': [5, 6, 7, 8]})


df1.merge(df2, left_on='fruta', right_on='alimento', 
                        suffixes=('_fruta', '_alimento'))
  
'''
#Resultado: 
        fruta	value_fruta	alimento	value_alimento
0	maçã	1	        maçã	        5
1	pera	3	        pera	        7
2	pêssego	5	        pêssego	        8
'''
