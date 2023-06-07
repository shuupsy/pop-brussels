#%% 
import json
import pandas as pd
import matplotlib.pyplot as plt

xls = pd.ExcelFile("2021_pop_classe_age.xlsx")

#%% 
age_columns = pd.read_excel(xls, usecols="C:H, J:L", names=["12-17", "18-29", "30-44", "3-5", "45-64", "6-11", "65-79", "80+", "< 3"])

# re-arange
age_columns = age_columns.drop(labels=[0,1,2,4,5,25,26,27,28,29,30], axis=0)
age_columns = age_columns.iloc[:,[8,3,5,0,1,2,4,6,7]]

#%% 
communes = ["Région de Bruxelles Capitale", "Anderlecht", "Auderghem", "Berchem-Sainte-Agathe", "Bruxelles", "Etterbeek", "Evere", "Forest", "Ganshoren", "Ixelles",  "Jette", "Koekelberg", "Molenbeek-Saint-Jean", "Saint-Gilles", "Saint-Josse-ten-Noode", "Schaerbeek", "Uccle", "Watermael-Boitsfort", "Woluwe-Saint-Lambert", "Woluwe-Saint-Pierre"]

#%%

pop_df = pd.DataFrame(age_columns)
pop_df.index = communes

population_df = pop_df.transpose()

# population_df.plot.bar()


# %%
