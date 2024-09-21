import pandas as pd

# list of student data
student_name = ['Abhishek', 'Jayesh', 'Harish', 'Sammak',
                'Gagan', 'Harsh', 'Yash', 'Vivek', 'Mayuresh']
student_id = [1, 2, 3, 4, 5, 6, 7, 8, 9]
student_age = [23, 24, 25, 21, 23, 21, 45, None, 25]
gender = ['M', 'M', 'M', "F", 'M', 'C', 'M', 'M', 'G']
score = [89, 87, 56, 87, 34, 68, 54, 78, None]

df_basic_data = pd.DataFrame({
    "Student_id": student_id,
    "Student_name": student_name,
    "Student_age": student_age,
    "Student_gender": gender,
    "Student_score": score
})

Student_extra_score = [98, 76, 87, 97, 56, 57, 65, 78, 80]
df_extra_data = pd.DataFrame({
    "Student_id": student_id,
    "Student_name": student_name,
    "Student_age": student_age,
    "Student_gender": gender,
    "Student_score": score,
    "Student_extra_score": Student_extra_score
})

df_basic_data.to_csv('Data.csv', index=False)
df_extra_data.to_csv('AdvData.csv', index=False)

#--------------------------------------------------------------

student_df = pd.read_csv('Data.csv')
student_df.dropna(subset=['Student_age'])

#--------------------------------------------------------------

meanVal = student_df['Student_score'].mean()
student_df['Student_score'].fillna(
    meanVal, inplace=True)  # update the original df
student_df  # if false then it will create new df

#--------------------------------------------------------------

filtered_df = student_df[(student_df['Student_age'] > 23)
                         & (student_df['Student_score'] > 70)]
filtered_df

#--------------------------------------------------------------

# adding new column to the df by adding the value 10 to the score column
student_df['Final_Score'] = student_df['Student_score']+10
student_df

#--------------------------------------------------------------

student_df.drop(['Student_gender'], axis='columns')

#--------------------------------------------------------------

student_df.sort_values('Final_Score')

#--------------------------------------------------------------

df_merge = student_df.merge(df_extra_data)
df_merge

#-------------------------------------------------------------

df_merge.fillna(s['Final_Score'])

#-------------------------------------------------------------

df_merge[['Student_id', 'Student_age']]

# ------------------------------------------------------------

df_merge.loc[:, 'Student_age']