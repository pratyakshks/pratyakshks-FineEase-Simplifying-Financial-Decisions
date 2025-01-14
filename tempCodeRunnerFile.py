from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def calculate_emi(principal, rate, years):
    monthly_rate = rate / 12 / 100
    months = years * 12
    emi = (principal * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    total_payment = emi * months
    interest_paid = total_payment - principal
    
    return emi, total_payment, interest_paid, months

def plot_repayment_schedule(principal, emi, total_payment, interest_paid, years):
    months = years * 12
    total_paid = [emi * month for month in range(0, months + 1)]
    interest_component = [interest_paid * (month / months) for month in range(0, months + 1)]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot([month / 12 for month in range(0, months + 1)], total_paid, label='Total')
    ax.plot([month / 12 for month in range(0, months + 1)], interest_component, label='Interest')
    ax.set_xlabel('Years Elapsed')
    ax.set_ylabel('Loan Paid (in ₹)')
    ax.set_title('Loan Repayment Schedule')
    ax.legend()
    ax.grid()

    # Convert plot to PNG image and then encode it to base64
    img_io = io.BytesIO()
    plt.savefig(img_io, format='png')
    img_io.seek(0)
    plot_url = base64.b64encode(img_io.getvalue()).decode('utf8')

    return plot_url

@app.route('/', methods=['GET', 'POST'])
def index():
    emi = total_payment = interest_paid = None
    plot_url = None
    error = None

    if request.method == 'POST':
        try:
            # Get form data
            principal_amount = float(request.form['principal_amount'])
            annual_interest_rate = float(request.form['annual_interest_rate'])
            loan_tenure_years = int(request.form['loan_tenure_years'])

            # Validate input
            if principal_amount <= 0 or annual_interest_rate <= 0 or loan_tenure_years <= 0:
                raise ValueError("Invalid input for principal, rate, or tenure")

            # Calculate EMI and other values
            emi, total_payment, interest_paid, months = calculate_emi(principal_amount, annual_interest_rate, loan_tenure_years)

            # Plot the repayment schedule
            plot_url = plot_repayment_schedule(principal_amount, emi, total_payment, interest_paid, loan_tenure_years)
            
        except ValueError as e:
            error = str(e)

    return render_template('indexEMI.html', emi=emi, total_payment=total_payment, interest_paid=interest_paid, plot_url=plot_url, error=error)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5002)  # This runs the app on port 5001

