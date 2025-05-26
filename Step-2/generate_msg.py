import pandas as pd
df = pd.read_csv('cleaned_output.csv')

#function to generate message
def generate_message(name, first_name, job_title, joined):
    if pd.notna(first_name) and str(first_name).strip():
        fname = first_name.strip()
    elif pd.notna(name) and str(name).strip():
        fname = name.strip().split()[0]
    else:
        fname = "there"

    job_title = job_title if pd.notna(job_title) and str(job_title).strip() else "professional"

    if joined:
        return (f"Hey {fname}, thanks for joining our session! As a {job_title.lower()}, "
                f"we think you'll love our upcoming AI workflow tools. Want early access?")
    else:
        return (f"Hi {fname}, sorry we missed you at the last event! We're preparing another session "
                f"that might better suit your interests as a {job_title.lower()}.")
    
#generate messages
df['message'] = df.apply(lambda row: generate_message(row['name'], row['first_name'],row['Job Title'], row['has_joined_event']), axis=1)

# Select and save only email and message columns
output_df = df[['email', 'message']]
output_df.to_csv('custom_messages.csv', index=False)
print("Messages saved to custom_messages.csv")




    
