from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load data
hdfc_loan = pd.read_csv("HDFC Loans.csv")
icici_loan = pd.read_csv("ICICI Loans.csv")
sbi_loan = pd.read_csv("SBI Loans.csv")
axis_loan = pd.read_csv("Axis Bank Loans.csv")

# Add a column indicating the bank
hdfc_loan['Bank'] = "HDFC Bank"
icici_loan['Bank'] = "ICICI Bank"
sbi_loan['Bank'] = 'SBI Bank'
axis_loan['Bank'] = 'Axis Bank'

# Combine the dataframes
combined_df = pd.concat([axis_loan, sbi_loan, icici_loan, hdfc_loan])
combined_df.reset_index(drop=True, inplace=True)

# Helper function to check age range
def age_in_range(row, user_age):
    try:
        age_range = row['Age Criteria'].replace('years', '').split('-')
        min_age = int(age_range[0].strip())
        max_age = int(age_range[1].strip())
        return min_age <= user_age <= max_age
    except Exception:
        return False

@app.route("/", methods=["GET", "POST"])
def index():
    loan_types = combined_df['Loan Type'].unique()
    user_age = None
    loan_needed = None
    eligibility_criteria = None
    features_criteria = None
    recommendations = None

    if request.method == "POST":
        loan_needed = request.form.get("loan_type")
        user_age = int(request.form.get("user_age", 0))
        ele1 = request.form.get("eligibility1")
        ele2 = request.form.get("eligibility2")
        feat1 = request.form.get("feature1")
        feat2 = request.form.get("feature2")

        # Filter by loan type
        loan_df = combined_df[combined_df["Loan Type"] == loan_needed]

        # Filter by age criteria
        loan_df = loan_df[loan_df.apply(lambda row: age_in_range(row, user_age), axis=1)]

        # Filter by eligibility
        loan_df = loan_df[loan_df["Eligibility"].str.contains(ele1, case=False, na=False) |
                          loan_df["Eligibility"].str.contains(ele2, case=False, na=False)]

        # Filter by features
        loan_df = loan_df[loan_df["Features"].str.contains(feat1, case=False, na=False) |
                          loan_df["Features"].str.contains(feat2, case=False, na=False)]

        recommendations = loan_df

    eligibility_list = sorted(set(
        item.strip()
        for sublist in combined_df['Eligibility'].dropna().str.split(",")
        for item in sublist
    ))

    features_list = sorted(set(
        item.strip()
        for sublist in combined_df['Features'].dropna().str.split(",")
        for item in sublist
    ))

    return render_template(
        "indexLoan.html",
        loan_types=loan_types,
        eligibility_list=eligibility_list,
        features_list=features_list,
        user_age=user_age,
        loan_needed=loan_needed,
        recommendations=recommendations,
    )

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5003)  # This runs the app on port 5001

