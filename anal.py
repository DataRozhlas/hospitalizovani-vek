# %%
import pandas as pd
# %%
d = pd.read_excel('./IS_COVID19_EPIDEMIOLOGIE_2021leden14.xlsx', sheet_name='celkovy prehled', skiprows=6)
d65 = pd.read_excel('./IS_COVID19_EPIDEMIOLOGIE_2021leden14.xlsx', sheet_name='prehled vek 65+', skiprows=6)
d75 = pd.read_excel('./IS_COVID19_EPIDEMIOLOGIE_2021leden14.xlsx', sheet_name='prehled vek 75+', skiprows=6)
# %%
d = d[['Datum', 'Aktuální počet hospitalizovaných osob']]
d.columns = ['datum', 'hosp']
# %%
d65 = d65[['Datum', 'Aktuální počet hospitalizovaných osob']]
d65.columns = ['datum', 'hosp_65']
# %%
d75 = d75[['Datum', 'Aktuální počet hospitalizovaných osob']]
d75.columns = ['datum', 'hosp_75']
# %%
d = d.merge(d65, on='datum').merge(d75, on='datum')
# %%
# vekova kateorie exkluzivne
d['hosp_mladsi'] = d.hosp - d.hosp_65
d.hosp_65 = d.hosp_65 - d.hosp_75

# %%
d['hosp_65_pct'] = d.hosp_65 / d.hosp
# %%
d['hosp_75_pct'] = d.hosp_75 / d.hosp
# %%
# %%
d['hosp_mladsi_pct'] = d.hosp_mladsi / d.hosp
# %%
#d.to_excel('hosp_vek.xlsx', index=False)
# %%
