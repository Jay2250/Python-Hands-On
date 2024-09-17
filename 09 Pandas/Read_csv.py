import pandas as pd

df = pd.read_csv('country_vaccinations.csv')
# print(df.head())
df['vaccination_rate'] = (
    ((df['total_vaccinations']-df['people_fully_vaccinated'])*100)/(df['total_vaccinations']))
# print(df)
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(
    df['daily_vaccinations'].mean())
# print(df)
df = df.drop('source_name', axis=1)
# df = df.dropna()
# print(df)
df['total_vaccinations'] = df['total_vaccinations'].fillna(
    df['total_vaccinations'].mean())
df_sorted = df.sort_values(by='total_vaccinations', ascending=True)
# print(df_sorted.head(20))
df = df_sorted.rename(columns={'iso_code': 'country_code'})
df.index = range(1, len(df)+1)
# print(df.head())
count_na = df.isna().sum()
print(count_na)
df['people_fully_vaccinated'] = df['people_fully_vaccinated'].fillna(0)
df = df.dropna(subset=['total_vaccinations'])
df['vaccines'].replace('Moderna, Pfizer/BioNTech', 'mRNA vaccines')
df.loc[df['daily_vaccinations'] < 0, 'daily_vaccinations'] = 0
print(df.head(20))
