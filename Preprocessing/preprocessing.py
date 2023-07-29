import pandas as pd

# colonne da eliminare
columns_to_delete = ['work_year', 'employment_type', 'salary', 'salary_currency', 'remote_ratio']

# leggi il file CSV e crea il DataFrame
df = pd.read_csv("..\Datasets\ds_salaries.csv")

# ricerca ed eliminazione degli stipendi min e max dalla feature 'salary'
max_value = df['salary_in_usd'].max()
min_value = df['salary_in_usd'].min()
filtered_data = df[(df['salary_in_usd'] != max_value) & (df['salary_in_usd'] != min_value)]

# creo un nuovo file csv con il dataset pulito contenente salari in valuta usd
new_data_2 = filtered_data.drop(columns=columns_to_delete)
new_data_2.to_csv("..\Datasets\ds_salaries_usd.csv", index=False)