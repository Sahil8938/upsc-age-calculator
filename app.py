from flask import Flask, render_template, request
from calculate import calculate_age, calculate_remaining_time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    birth_year = int(request.form['birth_year'])
    birth_month = int(request.form['birth_month'])
    birth_day = int(request.form['birth_day'])
    category = request.form['category']

    age = calculate_age(birth_year, birth_month, birth_day)
    if age is None:
        return render_template('result.html', error=True)

    remaining_years, remaining_months, remaining_days = calculate_remaining_time(age, category)
    if remaining_years is None:
        return render_template('result.html', error=False)

    return render_template('result.html', age=age, remaining_years=remaining_years, remaining_months=remaining_months, remaining_days=remaining_days)

if __name__ == '__main__':
    app.run(debug=True)
