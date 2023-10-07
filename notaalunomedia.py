import pandas as pd

alunosmedias = [['Isaac', '7', '4'],
                ['Taty', '10', '9'],
                ['Well', '4,5','10']]
df = pd.DataFrame(alunosmedias,columns=['Nome', 'Nota1', 'Nota2'])

df['Soma'] = df[['Nota1' + 'Nota2']]

df['Media'] = df.mean(soma)

print(df)