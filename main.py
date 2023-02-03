import pandas as pd
from matplotlib import pyplot as plt

# Einlesen des Datensatzes
df = pd.read_csv('ESS8e02.1_F1.csv', sep=",")

# print(df.describe())
print("Columns:", df.columns.values)
print("Nr. Entries:", len(df))

print(df.gndr.value_counts)  # 1...Male 2...Female, 9...No Answer

# Umkodieren der Zahlenwerte zu Kategorien
df['gndr'] = pd.cut(df['gndr'], [0, 1, 2, 9], labels=['Male', 'Female', 'No Answer'])
# Zur Überprüfung checken ob die gleiche Anzahl rauskommt wie oben
print(df.gndr.value_counts())

# Grafische Darstellung davon
df['gndr'].value_counts().plot(kind='bar')
plt.show()

# Auswahl von einer Gruppe
df_f = df.loc[df['gndr'] == 'Female']
print(df_f.head().gndr)

# Darstellung von Häufigkeiten
gndr_cntry = pd.crosstab(df['gndr'], df['cntry'])
# in Pycharm: Variablenansicht. Rechte Maustaste auf Variable => Vie as DataFrame liefert eine bessere Anzeige
print(gndr_cntry)

# 1.1
df_at = df.loc[df['cntry'] == 'AT']
df_at_it = df.loc[df['cntry'].isin(['AT', 'IT'])]

# 1.2
""" 
2 Variablen gegen ̈ubergestellt mit Messniveau
– Nominalskala: X2
– Ordinalskala: Korrelation (Spearman)
– Intervall/Ratioskala: Korrelation (Pearson)
"""
# X2
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html
from scipy.stats import chi2_contingency

chi2, p, dof, expected = chi2_contingency(gndr_cntry)
print("Chi2:", chi2)
print("p:", p)
print("dof:", dof)
# print("expected:", expected)

# Pearson
from scipy.stats import pearsonr

corr, p = pearsonr(df['sclact'], df['sclmeet'])
print("Pearson Correlation:", corr)
print("p:", p)

# Spearman
from scipy.stats import spearmanr

corr, p = spearmanr(df['sclact'], df['sclmeet'])
print("Spearman Correlation:", corr)
print("p:", p)

""" 
2 unabh ̈angige Gruppen (z.B. M ̈annlich/Weiblich) gegen ̈ubergestellt Variablen mit Messniveau
– Ordinalskala: Mann-Whitney-U-Test
– Intervall/Ratioskala: t-Test (haben wir nicht besprochen, kommt in diesem Fragebogen nicht
vor)
"""

# Mann-Whitney-U-Test
from scipy.stats import mannwhitneyu

stat, p = mannwhitneyu(df['sclact'], df['sclmeet'])
print("Mann-Whitney-U-Test Statistic:", stat)
print("p:", p)

gndr_cntry_at = pd.crosstab(df_at['gndr'], df_at['cntry'])
chi2, p, dof, expected = chi2_contingency(gndr_cntry_at)
print("Chi2:", chi2)
print("p:", p)
print("dof:", dof)
print("expected:", expected)
print("\n")

gndr_cntry_at_it = pd.crosstab(df_at_it['gndr'], df_at_it['cntry'])
chi2, p, dof, expected = chi2_contingency(gndr_cntry_at_it)
print("Chi2:", chi2)
print("p:", p)
print("dof:", dof)
print("expected:", expected)
print("\n")

