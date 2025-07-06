from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy spam detection logic
def is_spam(email_text):
    spam_keywords = ['win', 'lottery', 'money', 'prize', 'free', 'click', 'urgent', 'account suspended']
    return 1 if any(word in email_text.lower() for word in spam_keywords) else 0

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', label=None, email_text='')

@app.route('/predict', methods=['POST'])
def predict():
    email = request.form['email']
    label = is_spam(email)
    return render_template('index.html', label=label, email_text=email)

if __name__ == '__main__':
    app.run(debug=True)
