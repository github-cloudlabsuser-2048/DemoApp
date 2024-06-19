from flask import Flask, render_template, request

app = Flask(__name__)
expenses = []
total_amount = 0

@app.route('/', methods=['GET', 'POST'])
def expense_tracker():
    global total_amount

    if request.method == 'POST':
        expense_name = request.form['expense_name']
        amount = float(request.form['amount'])
        expenses.append((expense_name, amount))
        total_amount += amount

    return render_template('expense_tracker.html', expenses=expenses, total_amount=total_amount)

if __name__ == '__main__':
    app.run(port=3000)