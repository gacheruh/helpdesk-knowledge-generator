import pandas as pd

def load_tickets(filepath="data/sample_tickets.csv"):
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        return pd.DataFrame()

def get_category_counts(df):
    if df.empty:
        return pd.Series(dtype=int)
    return df['category'].value_counts()

def generate_kb_article(category, df):
    # Filter tickets for this category
    cat_df = df[df['category'] == category]
    sample_issues = cat_df['description'].tolist()
    
    # AI-assisted structured knowledge base drafting template
    article = f"""# Standard Operating Procedure / Knowledge Base Article: {category}

## Overview
This document addresses recurring support inquiries related to **{category}**, compiled from recent IT helpdesk tracking records across UAF-Africa's virtual organization.

## Common Symptoms & Reported Issues
"""
    for issue in sample_issues[:3]:
        article += f"- *'{issue}'*\n"
        
    article += f"""

## Step-by-Step Resolution Guide
1. **Initial Verification:** Verify user account status and network/M365 license assignment.
2. **Standard Troubleshooting:** 
   - Clear browser cache / restart Microsoft Teams or VPN client applications.
   - Confirm multi-factor authentication (MFA) sync or reset credentials securely via admin portal if required.
3. **Escalation Pathway:** If the issue persists after standard troubleshooting, escalate with detailed error logs to the ICT & Database Assistant.

## Prevention & Best Practices
- Ensure regular updates of M365 desktop client apps.
- Refer to internal security guidelines before requesting elevated permissions.
"""
    return article
