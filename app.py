from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    net_salary = None
    if request.method == 'POST':
        try:
            base_salary = float(request.form['base_salary'])
            bonus = float(request.form['bonus'])
            deductions = float(request.form['deductions'])
            # Calculate the net salary
            net_salary = base_salary + bonus - deductions
        except ValueError:
            net_salary = "Invalid input. Please enter numerical values."
    
    return render_template('index.html', net_salary=net_salary)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)


