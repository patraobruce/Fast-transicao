import pandas as pd

estadosnordeste = [['Alagoas', 'AL', '3,4 milhões', 'Maceió'],
                   ['Pernambuco', 'PE', '9,7 milhões', 'Recife'],
                   ['Rio Grande do Norte', 'RN', '3,5 milhões', 'Natal']]
df = pd.DataFrame(estadosnordeste,columns=['Estado', 'Sigla', 'População', 'Capital'])

print(df)