import pandas as pd
import random
from datetime import datetime

# Número de meses
num_months = 12
years = [2021, 2022, 2023]

def generate_positive_percentage_values(num_values):
    while True:
        values = [random.uniform(0.01, 1) for _ in range(num_values)]
        if sum(values) <= 1:
            break
    return [round(value / sum(values), 8) for value in values]

data = []

for year in years:
    for month in range(1, num_months + 1):
        date = datetime(year, month, 1).strftime('%m/%Y')
        values = generate_positive_percentage_values(4)  # 4 colunas (sem contar o período)
        data.append([date] + values)

df = pd.DataFrame(data, columns=['periodo', 'mao_de_obra_indireta', 'energia', 'manutencao', 'depreciacao'])

df.to_csv('tabela_taxas.csv', index=False)