# =========================================================
#   🔴  NEET_Pandas_300_Practice_Questions 
# =========================================================



"""
     🟢  Level 13: Pivot Tables, Crosstabs & MultiIndex
    
"""


import pandas as pd

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#  =====================================================================
#   🔵  241. Create a pivot table showing average Marks by state and city.
#  =====================================================================


result = df.groupby(['state', 'city'])['Marks'].mean().unstack()

print(result)


# %%

#  =====================================================================
#   🔵  242. Create a pivot table showing student count by state and city.
#  =====================================================================

# unstack() - City ko columns bana dega

result = df.groupby(['state','city'])['Marks'].count().unstack()

print(result)


# %%

#  =====================================================================
#   🔵  243. Create a pivot table showing total Marks by state and city.
#  =====================================================================

result = df.groupby(['state','city'])['Marks'].sum().unstack()

print(result)


# %%

#  =====================================================================
#   🔵  244. Create a pivot table showing maximum Marks by state and city.
#  =====================================================================

result = df.groupby(['state','city'])['Marks'].max().unstack()

print(result)


# %%

#  =====================================================================
#   🔵  245. Create a pivot table showing minimum Marks by state and city.
#  =====================================================================

result = df.groupby(['state','city'])['Marks'].min().unstack()

print(result)


# %%

#  =====================================================================
#   🔵  246. Create a pivot table showing average Marks by state and centre.
#  =====================================================================

result = df.groupby(['state','center_name'])['Marks'].mean().unstack()

print(result)


# %%

#  =====================================================================
#   🔵  247. Create a pivot table showing student counts by city and centre.
#  =====================================================================

result = df.groupby(['city','center_name'])['Marks'].count().unstack()

print(result)


# %%

#  =====================================================================
#   🔵  248. Create a pivot table of Score_Band against state.
#  =====================================================================


df['Score_Band'] = pd.cut(
    df['Marks'],
    bins=[-181, 100, 200, 300, 400, 500, 600, 700, 720],
    labels=['0-100', '101-200', '201-300', '301-400',
            '401-500', '501-600', '601-700', '701-720']
)

result = df.groupby(['Score_Band', 'state'], observed=False)['Marks'].count().unstack(fill_value=0)

print(result)


# %%

#  =====================================================================
#   🔵  249. Create a crosstab of state and score categories.
#  =====================================================================


result = pd.crosstab(df['state'], df['Score_Band'])

print(result)


# %%

#  =====================================================================
#   🔵  250. Create a crosstab of city and Pass_Fail.
#  =====================================================================


df['Pass_Fail'] = df['Marks'].apply(lambda x: 'Pass' if x >= 300 else 'Fail')

result = pd.crosstab(df['city'], df['Pass_Fail'])

print(result)


# %%

#  =====================================================================
#   🔵  251. Create a crosstab of state and Pass_Fail.
#  =====================================================================


result = pd.crosstab(df['state'], df['Pass_Fail'])

print(result)


# %%

#  =====================================================================
#   🔵  252. Create a crosstab of state and High_Medium_Low.
#  =====================================================================


df['High_Medium_Low'] = pd.cut(
    df['Marks'],
    bins=[-181, 299, 499, 720],
    labels=['Low', 'Medium', 'High']
)

result = pd.crosstab(df['state'], df['High_Medium_Low'])

print(result)


# %%

#  =====================================================================
#   🔵  253. Create a pivot table with state as rows and Score_Band as columns.
#  =====================================================================


result = df.groupby(['state', 'Score_Band'])['Marks'].count().unstack(fill_value=0)

print(result)


# %%

#  =====================================================================
#   🔵  254. Create a pivot table with city as rows and Score_Band as columns.
#  =====================================================================


result = df.groupby(['city', 'Score_Band'])['Marks'].count().unstack(fill_value=0)

print(result)


# %%


#  =====================================================================
#   🔵  255. Add margins/totals to a suitable pivot table.
#  =====================================================================


result = pd.pivot_table(
    df,
    index='state',
    columns='Score_Band',
    values='Marks',
    aggfunc='count',
    fill_value=0,
    margins=True
)

print(result)


# %%


#  =====================================================================
#   🔵  256. Normalize a state-by-score-band crosstab to percentages by row.
#  =====================================================================


result = pd.crosstab(
    df['state'],
    df['Score_Band'],
    normalize='index'
) * 100

print(result)


# %%

#  =====================================================================
#   🔵  257. Normalize a state-by-score-band crosstab to percentages by column.
#  =====================================================================


result = pd.crosstab(
    df['state'],
    df['Score_Band'],
    normalize='columns'
) * 100

print(result)


# %%


#  =====================================================================
#   🔵  258. Create a MultiIndex DataFrame using state and city.
#  =====================================================================


result = df.set_index(['state', 'city'])

print(result)


# %%

#  =====================================================================
#   🔵  259. Select data from a MultiIndex using .loc.
#  =====================================================================


result = df.set_index(['state', 'city'])

print(result.loc[('CHHATTISGARH', 'RAIPUR')])


# %%

#  =====================================================================
#   🔵  260. Sort a MultiIndex by state and city.
#  =====================================================================

result = df.set_index(['state', 'city'])

result = result.sort_index()

print(result)