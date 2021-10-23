tips.groupby('day').agg({'tip': np.mean, 'day': np.size})

'''
# Resultado:
           tip  day
day                
Fri   2.734737   19
Sat   2.993103   87
Sun   3.255132   76
Thur  2.771452   62
'''