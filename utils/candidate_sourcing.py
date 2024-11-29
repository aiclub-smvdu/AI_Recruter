import pandas as pd

def source_candidates(resumes_df):
    candidates = resumes_df[
        (resumes_df['experience'] > 3) & 
        (resumes_df['skills'].str.contains('Python|Java')) & 
        (resumes_df['location'] == 'Remote')
    ]
    if candidates.empty:
        raise ValueError("No candidates match the given criteria")
    return candidates
