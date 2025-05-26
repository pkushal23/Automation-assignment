import pandas as pd
df1 = pd.read_csv('input.csv')

#Reomving duplicates

df1 = df1.drop_duplicates()

# Normalize has_joined_event to True/False

df1['has_joined_event'] = df1['has_joined_event'].astype(str).str.strip().str.lower()
df1['has_joined_event'] = df1['has_joined_event'].map({
    'yes' : True, 'no': False
})
#Checking for missing or incomplete LinkedIn profiles
def is_valid_linkedin(profile):
    if isinstance(profile, str):
        profile = profile.strip().lower()
        return profile != "" and "linkedin.com/in/" in profile
    return False

df1['Valid_LinkedIn'] = df1['What is your LinkedIn profile?'].apply(is_valid_linkedin)

#checking for blank values of job title
df1['missing_Job'] = df1['Job Title'].isna() | (df1['Job Title'] == '')

# Save to a new CSV file
df1.to_csv('cleaned_output.csv', index=False)
