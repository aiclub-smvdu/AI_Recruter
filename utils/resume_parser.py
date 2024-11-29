import os
import pandas as pd

def parse_resumes(resume_directory):
    resumes = []
    for filename in os.listdir(resume_directory):
        if filename.endswith(".csv"):  # Example file type
            file_path = os.path.join(resume_directory, filename)
            df = pd.read_csv(file_path)
            # Standardize column names
            df.rename(columns={
                'years_of_experience': 'experience',
                'experience_years': 'experience'
            }, inplace=True)
            resumes.append(df)
    if resumes:
        resumes_df = pd.concat(resumes, ignore_index=True)
    else:
        resumes_df = pd.DataFrame()  # Return an empty DataFrame if no resumes found
    print("Columns in DataFrame:", resumes_df.columns)  # Print DataFrame columns
    return resumes_df
