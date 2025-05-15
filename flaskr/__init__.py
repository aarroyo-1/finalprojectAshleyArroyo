import os
import requests
from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)

    @app.route('/validate', methods=['GET', 'POST'])
    def validate():
        results = None

        if request.method == 'POST':
            email = request.form.get('email')
            phone = request.form.get('phone')

            email_api_key = os.getenv("EMAIL_API_KEY")
            phone_api_key = os.getenv("PHONE_API_KEY")

            email_response = requests.get(
                f"https://emailvalidation.abstractapi.com/v1/?api_key={email_api_key}&email={email}")
            phone_response = requests.get(
                f"http://apilayer.net/api/validate?access_key={phone_api_key}&number={phone}&country_code=US&format=1")

            results = {
                'email_valid': email_response.json(),
                'phone_valid': phone_response.json()
            }

        return render_template('form.html', results=results)

    return app
