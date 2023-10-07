import pandas as pd

alunosmedias = [['Isaac', '7'],
                ['Taty', '10'],
                ['Well', '4,5']]
df = pd.DataFrame(alunosmedias,columns=['Nome', 'Nota'])

print(df)