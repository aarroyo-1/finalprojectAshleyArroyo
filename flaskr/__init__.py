import os
import requests
from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv

def create_app():
    load_dotenv()

    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder="templates"  # ✅ Corrected this line
    )

    app.config.from_mapping(SECRET_KEY='dev')

    @app.route('/')
    def index():
        return redirect(url_for('validate'))

    @app.route('/validate', methods=['GET', 'POST'])
    def validate():
        if request.method == 'POST':
            email = request.form.get('email')
            phone = request.form.get('phone')

            errors = []

            if not email or '@' not in email:
                errors.append("Invalid email address.")

            if not phone or not phone.isdigit() or len(phone) != 10:
                errors.append("Invalid phone number. Must be 10 digits.")

            return render_template('form.html', email=email, phone=phone, errors=errors)

        return render_template('form.html')

    return app
