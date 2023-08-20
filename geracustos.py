import pandas as pd
import random
from datetime import datetime

# Número de itens e meses
num_items = 100
end_year = 2023
end_month = 7

# Função para gerar um valor aleatório dentro de um intervalo
def generate_random_value(min_value, max_value):
    return round(random.uniform(min_value, max_value), 2)

data = []

for item in range(1, num_items + 2):
    for year in range(2021, end_year + 1):  # De 2021 a 2023
        end_month_current_year = end_month if year == end_year else 12
        for month in range(1, end_month_current_year + 1):
            date = datetime(year, month, 1).strftime('%m/%Y')
            mao_de_obra = generate_random_value(1, 1000)
            materia_prima = generate_random_value(1, 1500)
            gasto_geral = generate_random_value(1,500)
            data.append([item+100, date, mao_de_obra, materia_prima,gasto_geral])

df = pd.DataFrame(data, columns=['cod_item', 'periodo', 'mao_de_obra', 'materia_prima','gasto_geral'])
df.to_csv('tabela_custos.csv', index=False)