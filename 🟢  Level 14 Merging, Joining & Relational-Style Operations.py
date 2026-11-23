# =========================================================
#   🔴  NEET_Pandas_300_Practice_Questions 
# =========================================================



"""
     🟢  Level 14: Merging, Joining & Relational-Style Operations
    
"""


import pandas as pd    

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#  =============================================================================
#   🔵  261. Create a state-level summary DataFrame containing student count 
#             and average Marks.
#  =============================================================================

state_summary = df.groupby('state').agg(
    student_count = ('Marks','count'),
    average_Marks = ('Marks','mean')
    ).reset_index()

print(state_summary)


# %%

#  ===========================================================================
#   🔵  262. Create a city-level summary DataFrame containing student count 
#               and average Marks.
#  ===========================================================================

city_summary = df.groupby('city').agg(
    student_count = ('Marks','count'),
    avrage_Marks = ('Marks','mean')
    ).reset_index()

print(city_summary)


# %%

#  ==========================================================================
#   🔵  263. Merge the state-level summary back into the original DataFrame.
#  ==========================================================================

state_summary = df.groupby('state').agg(
    student_count = ('Marks','count'),
    avrage_Marks  = ('Marks','mean')
    ).reset_index()

df_merged = df.merge(
    state_summary,
    on = 'state',
    how = 'left'
    )

print(df_merged)


# %%

#  ==========================================================================
#   🔵  264. Merge the city-level summary back into the original DataFrame.
#  ==========================================================================

city_summary = df.groupby('city').agg(
    student_count = ('Marks','count'),
    avrage_Marks  = ('Marks','mean')
    ).reset_index()

df_merged = df.merge(
    city_summary,
    on = 'city',
    how = 'left'
    )

print(df_merged)


# %%

#  ==========================================================================
#   🔵  265. Merge a centre-level summary back into the original DataFrame.
#  ==========================================================================

center_summary = df.groupby('center_num').agg(
    student_count = ('Marks','count'),
    avrage_Marks = ('Marks','mean')
    ).reset_index()

df_merged = df.merge(
    center_summary,
    on = 'center_num',
    how = 'left'
    )

print(df_merged)


# %%

#  =====================================================================
#   🔵  266. Join state-level statistics to each student record.
#  =====================================================================

state_summary = df.groupby('state').agg(
    student_count = ('Marks','count'),
    avrage_Marks = ('Marks','mean')
    ).reset_index()

df_merged = df.merge(
    state_summary ,
    on = 'state',
    how = 'left'
    )

print(df_merged)


# %%

#  =====================================================================
#   🔵  267. Join city-level statistics to each student record.
#  =====================================================================

# City-level statistics

city_stats = df.groupby('city').agg(
    city_student_count=('Marks', 'count'),
    city_average_marks=('Marks', 'mean')
).reset_index()

# Original data ke saath merge

df2 = df.merge(city_stats, on='city', how='left')

print(df2)


# %%

#  =====================================================================
#   🔵  268. Create separate DataFrames for state totals and state 
#              averages, then merge them.
#  =====================================================================


state_totals = df.groupby('state')['Marks'].count().reset_index(name='Total_Students')

state_averages = df.groupby('state')['Marks'].mean().reset_index(name='Average_Marks')

result = pd.merge(state_totals, state_averages, on='state')

print(result)


# %%

#  =====================================================================
#   🔵  269. Create separate DataFrames for city totals and city averages
#            , then merge them.
#  =====================================================================


city_totals = df.groupby('city')['Marks'].count().reset_index(name='Total_Students')

city_averages = df.groupby('city')['Marks'].mean().reset_index(name='Average_Marks')

result = pd.merge(city_totals, city_averages, on='city')

print(result)


# %%


#  =====================================================================
#   🔵  270. Merge two summaries using state as the key.
#  =====================================================================


state_totals = df.groupby('state')['Marks'].count().reset_index(name='Total_Students')

state_averages = df.groupby('state')['Marks'].mean().reset_index(name='Average_Marks')

result = pd.merge(state_totals, state_averages, on='state')

print(result)


# %%


#  =====================================================================
#   🔵  271. Merge two summaries using city as the key.
#  =====================================================================


city_total = df.groupby('city')['Marks'].count().reset_index()

city_avg = df.groupby('city')['Marks'].mean().reset_index()

result = pd.merge(city_total, city_avg, on='city')

print(result)


# %%

#  =====================================================================
#   🔵  272. Create a centre-to-city mapping DataFrame and join it to student data.
#  =====================================================================


centre_city = df[['center_name', 'city']].drop_duplicates()

result = pd.merge(df, centre_city, on=['center_name', 'city'])

print(result)


# %%


#  =====================================================================
#   🔵  273. Identify records that do not match during a merge using an indicator column.
#  =====================================================================


df1 = df[['state', 'city']].drop_duplicates()

df2 = df[['state', 'center_name']].drop_duplicates()

result = pd.merge(df1, df2, on='state', how='outer', indicator=True)

print(result[result['_merge'] != 'both'])


# %%

#  =====================================================================
#   🔵  274. Perform a left merge between student data and state statistics.
#  =====================================================================


state_stats = df.groupby('state')['Marks'].mean().reset_index()

result = pd.merge(df, state_stats, on='state', how='left')

print(result)


# %%

#  =====================================================================
#   🔵  275. Perform an inner merge between student data and city statistics.
#  =====================================================================


city_stats = df.groupby('city')['Marks'].mean().reset_index()

result = pd.merge(df, city_stats, on='city', how='inner')

print(result)


# %%

#  =====================================================================
#   🔵  276. Perform an outer merge between two summary DataFrames.
#  =====================================================================


state_total = df.groupby('state')['Marks'].count().reset_index()

city_total = df.groupby('city')['Marks'].count().reset_index()

result = pd.merge(state_total, city_total, left_index=True, right_index=True, how='outer')

print(result)


# %%


#  =====================================================================
#   🔵  277. Use merge validation to check whether a state-level merge is one-to-many.
#  =====================================================================


state_total = df.groupby('state')['Marks'].count().reset_index()

result = pd.merge(df, state_total, on='state', how='left', validate='many_to_one')

print(result)


# %%


#  =====================================================================
#   🔵  278. Merge state and city summaries to create a combined location report.
#  =====================================================================


state_total = df.groupby('state')['Marks'].count().reset_index()

city_total = df.groupby(['state', 'city'])['Marks'].count().reset_index()

result = pd.merge(city_total, state_total, on='state')

print(result)


# %%


#  =====================================================================
#   🔵  279. Compare two summary DataFrames and identify states with changed averages.
#  =====================================================================


state_avg1 = df.groupby('state')['Marks'].mean().reset_index()

state_avg2 = df.groupby('state')['Marks'].mean().reset_index()

result = pd.merge(state_avg1, state_avg2, on='state')

result = result[result['Marks_x'] != result['Marks_y']]

print(result)


# %%

#  =====================================================================
#   🔵  280. Create a table containing each state, its average Marks, and national average.
#  =====================================================================

state_avg = df.groupby('state')['Marks'].mean().reset_index(name='Average_Marks')

national_avg = df['Marks'].mean()

state_avg['National_Average'] = national_avg

print(state_avg)