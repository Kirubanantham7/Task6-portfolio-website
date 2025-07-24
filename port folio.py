from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form.get('phone', '')
        message = request.form['message']

        # Save data to CSV
        save_to_csv([name, email, phone, message])

        print("Data saved to CSV.")
        return render_template('contact.html', success=True)
    return render_template('contact.html', success=False)

def save_to_csv(data):
    file_exists = os.path.isfile('messages.csv')
    with open('messages.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'Email', 'Phone', 'Message'])  # Add header
        writer.writerow(data)

if __name__ == '__main__':
    app.run(debug=True)
