# =========================================================
#   🔴  NEET_Pandas_300_Practice_Questions 
# =========================================================



"""
     🟢  Level 15: Window-Style Analysis, Ranking & Advanced Challenges
    
"""


import pandas as pd  

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#  =====================================================================
#   🔵  281. Calculate the overall rank of every student using rank().
#  =====================================================================

df['Rank'] = df['Marks'].rank(ascending=False)

print(df[['state', 'city', 'Marks', 'Rank']])



# %%


#  =====================================================================
#   🔵  282. Calculate dense rank of students based on Marks.
#  =====================================================================


df['Dense_Rank'] = df['Marks'].rank(ascending=False, method='dense') 

print(df[['state', 'city', 'Marks', 'Dense_Rank']])


# %%


#  =====================================================================
#   🔵  283. Calculate competition rank of students based on Marks.
#  =====================================================================


df['Competition_Rank'] = df['Marks'].rank(ascending=False, method='min')

print(df[['state', 'city', 'Marks', 'Competition_Rank']])


# %%


#  =====================================================================
#   🔵  284. Calculate percentile rank of every student.
#  =====================================================================


df['Percentile_Rank'] = df['Marks'].rank(pct=True) * 100 

print(df[['state', 'city', 'Marks', 'Percentile_Rank']])


# %%


#  =====================================================================
#   🔵  285. Calculate rank within each state.
#  =====================================================================


df['State_Rank'] = df.groupby('state')['Marks'].rank(ascending=False) 

print(df[['state', 'city', 'Marks', 'State_Rank']])


# %%


#  =====================================================================
#   🔵  286. Calculate rank within each city.
#  =====================================================================


df['City_Rank'] = df.groupby('city')['Marks'].rank(ascending=False)

print(df[['city', 'Marks', 'City_Rank']])


# %%


#  =====================================================================
#   🔵  287. Calculate rank within each centre.
#  =====================================================================

df['Centre_Rank'] = df.groupby('center_name')['Marks'].rank(ascending=False)

print(df[['center_name', 'Marks', 'Centre_Rank']])


# %%


#  =====================================================================
#   🔵  288. Identify the top scorer in every state.
#  =====================================================================


df['State_Rank'] = df.groupby('state')['Marks'].rank(ascending=False)

print(df[df['State_Rank'] == 1][['state', 'city', 'center_name', 'Marks']])


# %%


#  =====================================================================
#   🔵  289. Identify the top scorer in every city.
#  =====================================================================

df['City_Rank'] = df.groupby('city')['Marks'].rank(ascending=False)

print(df[df['City_Rank'] == 1][['state', 'city', 'center_name', 'Marks']])


# %%


#  =====================================================================
#   🔵  290. Identify the top scorer in every centre.
#  =====================================================================

df['Centre_Rank'] = df.groupby('center_name')['Marks'].rank(ascending=False)

print(df[df['Centre_Rank'] == 1][['state', 'city', 'center_name', 'Marks']])

#  df['Centre_Rank'] == 1 → har centre ke top scorer ko select karega.


# %%


#  =====================================================================
#   🔵  291. Identify the top 3 scorers in every state.
#  =====================================================================

df['State_Rank'] = df.groupby('state')['Marks'].rank(ascending=False)

print(df[df['State_Rank'] <= 3][['state', 'city', 'center_name', 'Marks', 'State_Rank']])


# %%


#  =====================================================================
#   🔵  292. Identify the top 3 scorers in every city.
#  =====================================================================

df['City_Rank'] = df.groupby('city')['Marks'].rank(ascending=False)

print(df[df['City_Rank'] <= 3][['state', 'city', 'center_name', 'Marks', 'City_Rank']])


# %%


#  =====================================================================
#   🔵  293. Identify the top 3 scorers in every centre.
#  =====================================================================

df['Centre_Rank'] = df.groupby('center_name')['Marks'].rank(ascending=False)

print(df[df['Centre_Rank'] <= 3][['state', 'city', 'center_name', 'Marks', 'Centre_Rank']])


# %%


#  =====================================================================================================
#   🔵  294. Find the difference between each student's Marks and the highest Marks in their state.
#  =====================================================================================================


df['State_Highest_Marks'] = df.groupby('state')['Marks'].transform('max')

df['Marks_Difference'] = df['State_Highest_Marks'] - df['Marks']

print(df[['state', 'city', 'Marks', 'State_Highest_Marks', 'Marks_Difference']])


# %%


#  =================================================================================================
#   🔵  295. Find the difference between each student's Marks and the average Marks of their state.
#  =================================================================================================


df['State_Average_Marks'] = df.groupby('state')['Marks'].transform('mean')

df['Marks_Difference'] = df['Marks'] - df['State_Average_Marks']

print(df[['state', 'city', 'Marks', 'State_Average_Marks', 'Marks_Difference']])


# %%

#  =============================================================================
#   🔵  296. Find the percentage of the state maximum achieved by each student.
#  =============================================================================

df['State_Max_Marks'] = df.groupby('state')['Marks'].transform('max')

df['State_Max_Percentage'] = (df['Marks'] / df['State_Max_Marks']) * 100

print(df[['state', 'city', 'Marks', 'State_Max_Marks', 'State_Max_Percentage']])


# %%


#  =============================================================================
#   🔵  297. Find the percentage of the centre maximum achieved by each student.
#  =============================================================================

df['Centre_Max_Marks'] = df.groupby('center_name')['Marks'].transform('max')

df['Centre_Max_Percentage'] = (df['Marks'] / df['Centre_Max_Marks']) * 100

print(df[['center_name', 'Marks', 'Centre_Max_Marks', 'Centre_Max_Percentage']])


# %%


#  =====================================================================
#   🔵  298. Calculate each state's contribution to total candidates.
#  =====================================================================

df['State_Contribution'] = df.groupby('state')['Marks'].transform('count') / len(df) * 100

print(df[['state', 'State_Contribution']].drop_duplicates())


# %%


#  =====================================================================
#   🔵  299. Calculate each city's contribution to total candidates.
#  =====================================================================

df['City_Contribution'] = df.groupby('city')['Marks'].transform('count') / len(df) * 100

print(df[['city', 'City_Contribution']].drop_duplicates())


# %%


#  =====================================================================
#   🔵  300. Calculate each centre's contribution to total candidates.
#  =====================================================================

df['Centre_Contribution'] = df.groupby('center_name')['Marks'].transform('count') / len(df) * 100

print(df[['center_name', 'Centre_Contribution']].drop_duplicates())