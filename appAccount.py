from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load data
hdfc_bank = pd.read_csv("HDFC Accounts.csv", encoding='ISO-8859-1')
icici_bank = pd.read_csv("ICICI Accounts.csv")
axis_bank = pd.read_csv("Axis Bank Accounts.csv")
sbi_bank = pd.read_csv("SBI Accounts.csv")

# Combine data
hdfc_bank['Bank'] = "HDFC Bank"
icici_bank['Bank'] = "ICICI Bank"
axis_bank['Bank'] = "Axis Bank"
sbi_bank['Bank'] = "SBI Bank"
combined_df = pd.concat([axis_bank, sbi_bank, icici_bank, hdfc_bank])

@app.route("/", methods=["GET", "POST"])
def index():
    accounts = None

    # Prepare dropdown options
    saving_accounts = combined_df[combined_df['Account Type'].str.contains('Saving', case=False, na=False)]
    current_accounts = combined_df[combined_df['Account Type'].str.contains('Current', case=False, na=False)]
    options = saving_accounts if request.form.get("account_type") == "Saving" else current_accounts

    type = {i + 1: acc for i, acc in enumerate(options['Account Type'].unique())}
    age_cr = {i + 1: age for i, age in enumerate(options['Age Criteria'].unique())}
    eleg = options['Eligibility'].dropna().str.split(",").sum()
    Accele = {i + 1: crit.strip() for i, crit in enumerate(set(eleg))}
    features = options['Key Features'].dropna().str.split(",").sum()
    AccFeatures = {i + 1: feat.strip() for i, feat in enumerate(set(features))}

    if request.method == "POST":
        # Extract user inputs
        form_data = request.form
        account_type = form_data['account_type']
        specific_type = form_data['specific_type']
        age_criteria = form_data['age_criteria']
        eligibility1 = form_data['eligibility1']
        eligibility2 = form_data['eligibility2']
        feature1 = form_data['feature1']
        feature2 = form_data['feature2']

        # Filter data
        Account = combined_df[combined_df['Account Type'].str.contains(account_type, case=False, na=False)]
        Account = Account[Account['Account Type'] == specific_type]
        Account = Account[Account['Age Criteria'] == age_criteria]
        Acc1 = Account[Account['Eligibility'].str.contains(eligibility1, case=False, na=False)]
        Acc2 = Account[Account['Eligibility'].str.contains(eligibility2, case=False, na=False)]
        Account = pd.concat([Acc1, Acc2]).drop_duplicates()
        feat1 = Account[Account['Key Features'].str.contains(feature1, case=False, na=False)]
        feat2 = Account[Account['Key Features'].str.contains(feature2, case=False, na=False)]
        accounts = pd.concat([feat1, feat2]).drop_duplicates()

    return render_template("indexAccount.html", type=type, age_cr=age_cr, Accele=Accele, AccFeatures=AccFeatures, accounts=accounts)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5001)  # This runs the app on port 5001

