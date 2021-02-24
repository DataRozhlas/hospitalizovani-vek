# %%
import pandas as pd
import numpy as np
# %%
d = pd.read_excel('./04_IS_COVID19_EPIDEMIOLOGIE.xlsx', sheet_name='celkovy_prehled', skiprows=9)
d65 = pd.read_excel('./04_IS_COVID19_EPIDEMIOLOGIE.xlsx', sheet_name='prehled_vek_65', skiprows=9)
d75 = pd.read_excel('./04_IS_COVID19_EPIDEMIOLOGIE.xlsx', sheet_name='prehled_vek_75', skiprows=9)

# %%
d
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
d.datum = pd.to_datetime(d.datum, format='%d. %m. %Y')
# %%
d['ts'] = d.datum.values.astype(np.int64) // 10 ** 9
# %%
d[['ts', 'hosp_mladsi', 'hosp_65', 'hosp_75']].to_csv('./dump.csv', encoding='utf-8', index=False, sep='\t')
# %%
d.columns
# %%
