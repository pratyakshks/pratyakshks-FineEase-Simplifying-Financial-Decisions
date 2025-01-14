from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
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

def plot_repayment_schedule_with_bars(principal, emi, total_payment, interest_paid, years):
    months = years * 12
    total_paid = [emi * month for month in range(0, months + 1)]
    interest_component = [interest_paid * (month / months) for month in range(0, months + 1)]
    elapsed_years = [month / 12 for month in range(0, months + 1)]

    fig, ax1 = plt.subplots(figsize=(10, 6))
    bar_width = 0.3
    x_bar_positions = [year for year in range(0, years + 1)]  
    total_paid_per_year = [emi * year * 12 for year in range(0, years + 1)]
    interest_per_year = [interest_paid * (year / years) for year in range(0, years + 1)]

    ax1.bar([x - bar_width / 2 for x in x_bar_positions], total_paid_per_year, width=bar_width, 
            color='skyblue', label='Total Paid (Bar)')
    ax1.bar([x + bar_width / 2 for x in x_bar_positions], interest_per_year, width=bar_width, 
            color='orange', label='Interest Paid (Bar)')

    ax2 = ax1.twinx()
    ax2.plot(elapsed_years, total_paid, color='blue', label='Total Paid (Line)')
    ax2.plot(elapsed_years, interest_component, color='red', label='Interest Paid (Line)')

    ax1.set_xlabel('Years Elapsed', fontsize=12)
    ax1.set_ylabel('Loan Paid (in ₹)', fontsize=12)
    ax1.set_title('Loan Repayment Schedule', fontsize=16)

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    ax1.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()

    # Save plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            principal = float(request.form["principal"])
            rate = float(request.form["rate"])
            tenure = int(request.form["tenure"])
            if principal <= 0 or rate <= 0 or tenure <= 0:
                raise ValueError("Invalid input for principal, rate, or tenure")

            emi, total_payment, interest_paid, total_months = calculate_emi(principal, rate, tenure)
            plot_url = plot_repayment_schedule_with_bars(principal, emi, total_payment, interest_paid, tenure)

            summary = {
                "principal": principal,
                "rate": rate,
                "tenure": tenure,
                "emi": round(emi, 2),
                "total_payment": round(total_payment, 2),
                "interest_paid": round(interest_paid, 2),
            }
            return render_template("indexEMI.html", summary=summary, plot_url=plot_url)

        except ValueError as e:
            return render_template("indexEMI.html", error=str(e))
    return render_template("indexEMI.html")

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5002)  # This runs the app on port 5001

