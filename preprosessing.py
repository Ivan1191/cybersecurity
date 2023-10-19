#Import Library
import pandas as pd

#Load Dataset
df = pd.read_csv('cve.csv')
print(df)

#Preprosessing
df = df.rename(columns={'Unnamed: 0': 'Name','summary':'Text'})
print(df)

left_df = df['Name']
right_df = df['Text']
print(left_df,right_df)

new_df = pd.merge(left=left_df, right=right_df, left_index=True, right_index=True)
print(new_df)

#Write to csv
new_df.to_csv('X_test.csv',index=0)