from flask import Flask, render_template, url_for, request, redirect, session, flash
import os

app = Flask(__name__, static_folder='static')
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/commissions')
def commissions():
    return render_template('commissions.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/potraits')
def category():
    return render_template('potraits.html')

@app.route('/sold')
def sold():
    return render_template('sold.html')

@app.route('/landscape')
def landscape():
    return render_template('landscape.html')

@app.route('/zendaism_art')
def zendaism_art():
    return render_template('zendaism_art.html')

@app.route('/egg')
def egg():
    return render_template('egg.html')

@app.route('/scrap')
def scrap():
    return render_template('scrap.html')

@app.route('/social')
def social():
    return render_template('social.html')


@app.route('/view')
def view():
    return render_template('view.html')
    @app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/process_payment', methods=['POST'])
def process_payment():
    name = request.form['name']
    email = request.form['email']
    amount = request.form['amount']
    payment_method = request.form['payment_method']
    account_number = request.form['account_number']

    if payment_method == "ecocash":
        # Create a payment request for EcoCash
        payment = paynow.create_payment(f"Payment by {name}", email)
        payment.add("Art Purchase", amount)

        # Send the payment request
        response = paynow.send_mobile(payment, account_number, "ecocash")

        if response.success:
            return f"A payment request of ${amount} has been sent to your EcoCash account ({account_number}). Please authorize the payment on your device."
        else:
            return f"Payment failed: {response.error}"

    elif payment_method == "bank":
        # Create a payment request for Bank
        payment = paynow.create_payment(f"Payment by {name}", email)
        payment.add("Art Purchase", amount)

        # Send the payment request
        response = paynow.send_mobile(payment, account_number, "bank")

        if response.success:
            return f"A payment request of ${amount} has been sent to your bank account ({account_number}). Please authorize the payment on your device."
        else:
            return f"Payment failed: {response.error}"

    else:
        return "Invalid payment method selected."

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    print_option = request.form['print_option']
    # Add the selected print option to the cart (implement cart logic here)
    flash(f"{print_option} print has been added to your cart!", "success")
    return redirect('/category')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
