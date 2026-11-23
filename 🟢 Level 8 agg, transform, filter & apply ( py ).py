# =========================================================
#   🔴  NEET_Pandas_300_Practice_Questions 
# =========================================================


"""

    🟢 Level 8: agg, transform, filter & apply
        
"""



import pandas as pd        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



# ======================================================================
#    🔵 141. Use groupby().agg() to calculate count, mean, maximum, 
#           and minimum Marks by state
# ======================================================================


print(df.groupby('state').agg({'Marks':['count','mean','max','min']}))


#_______________________________________________________________________________________________


# ======================================================================
#  🔵 142. Use groupby().agg() to calculate count, mean, and 
#              standard deviation by city.
# ======================================================================


print(df.groupby('city').agg({'Marks':['count','mean','std']}))


#___________________________________________________________________________________________


# ======================================================================
#    🔵 143. Use groupby().agg() to calculate total and average Marks
#           by centre.
# ======================================================================


print(df.groupby('center_name').agg({'Marks':['sum','mean']}))


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 144. Give meaningful names to aggregated columns for
#           state-level statistics.
# ======================================================================



state_stats = df.groupby('state').agg(
    student_count=('Marks', 'count'),
    average_marks=('Marks', 'mean'),
    maximum_marks=('Marks', 'max'),
    minimum_marks=('Marks', 'min')
).reset_index()

print(state_stats)


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 145. Calculate multiple aggregations for Marks by state
#           in one operation.
# ======================================================================


state = df.groupby('state')['Marks'].agg(
    ['count','mean','max','min'])

print(state)


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 146. Calculate the number of students and average Marks
#           for each city.
# ======================================================================


city = df.groupby('city').agg(
    student_count = ('Marks','count'),
    average_Marks = ('Marks','mean'))

print(city)


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 147. Calculate the number of students, total Marks, and
#           average Marks for each centre.
# ======================================================================


center = df.groupby('center_name').agg(
    student_count = ('Marks','count'),
    average_Marks = ('Marks','mean'),
    total_Marks = ('Marks','sum'))

print(center)

#_______________________________________________________________________________________________


# ======================================================================
#    🔵 148. Filter states having more than 10,000 students using
#           groupby().filter().
# ======================================================================


result = df.groupby('state').filter(lambda x: x['Marks'].count() > 10000)

print(result)         # lambda = Chhota function banata hai x 


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 149. Filter cities having more than 5,000 students using
#           groupby().filter().
# ======================================================================


result = df.groupby('city').filter(lambda x: x['Marks'].count() > 5000)

print(result)


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 150. Filter centres having more than 300 students using
#           groupby().filter().
# ======================================================================


result = df.groupby('center_name').filter(lambda x: x['Marks'].count() > 300)

print(result)


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 151. Filter states whose average Marks exceed 450.
# ======================================================================


result = df.groupby('state').filter(lambda x: x['Marks'].mean() > 450)

print(result)


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 152. Filter cities whose average Marks exceed 500.
# ======================================================================


result = df.groupby('city').filter(lambda x: x['Marks'].mean() > 500)

print(result)


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 153. Filter centres whose average Marks exceed 550.
# ======================================================================


result = df.groupby('center_name').filter(lambda x: x['Marks'].mean() > 550)

print(result)


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 154. Filter states where the maximum Marks exceed 700.
# ======================================================================


result = df.groupby('state').filter(lambda x: x['Marks'].max() > 700)

print(result)


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 155. Filter cities having at least 20 students scoring
#           above 650.
# ======================================================================


result = df.groupby('city').filter(lambda x: (x['Marks'] > 650).sum() >= 20)

print(result)


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 156. Use transform() to add each student's state average Marks.
# ======================================================================


df['State_Average'] = df.groupby('state')['Marks'].transform('mean')

print(df[['state', 'Marks', 'State_Average']])


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 157. Use transform() to add each student's city average Marks.
# ======================================================================


df['City_Average'] = df.groupby('city')['Marks'].transform('mean')

print(df[['city', 'Marks', 'City_Average']])


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 158. Use transform() to add each student's centre average Marks.
# ======================================================================


df['Centre_Average'] = df.groupby('center_name')['Marks'].transform('mean')

print(df[['center_name', 'Marks', 'Centre_Average']])


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 159. Use transform() to add the number of students in each
#           state to every row.
# ======================================================================


df['State_Student_Count'] = df.groupby('state')['Marks'].transform('count')

print(df[['state', 'Marks', 'State_Student_Count']])


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 160. Use transform() to calculate each student's percentage
#           of their state's total Marks.
# ======================================================================


df['State_Total_Marks'] = df.groupby('state')['Marks'].transform('sum')

df['State_Marks_Percentage'] = ( df['Marks'] / df['State_Total_Marks'] * 100 )

print(df[['state', 'Marks', 'State_Total_Marks', 'State_Marks_Percentage']])
