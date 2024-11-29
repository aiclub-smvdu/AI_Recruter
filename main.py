import pandas as pd
from utils.candidate_sourcing import source_candidates
from utils.email_automation import send_email

def main():
    # Load resumes
    resumes = pd.read_csv('data/resumes.csv')
    
    # Source candidates
    try:
        candidates = source_candidates(resumes)
        print("Filtered Candidates:")
        print(candidates)
        
        # Send email notifications to filtered candidates
        for _, row in candidates.iterrows():
            subject = "Exciting Job Opportunity at Electronics Inc."
            body = f'''
            Dear {row['name']},

            We are thrilled to inform you about a fantastic job opportunity at Electronics Inc.

            **Position:** Software Engineer
            **Location:** Remote
            **Date:** September 15, 2024
            **Time:** 10:00 AM (PST)
            **Location:** Zoom (link will be provided in a follow-up email)

            **About Electronics Inc.:**
            Electronics Inc. is a leading innovator in the electronics industry, specializing in cutting-edge technology solutions and consumer electronics. Our mission is to drive progress through technology and deliver high-quality products to our customers worldwide.

            We would love to discuss this opportunity with you in detail.

            Best regards,
            Harsh Raj
            HR Manager
            InovoAI.
            '''

            send_email(row['email'], subject, body)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
