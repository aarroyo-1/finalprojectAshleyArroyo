from flask import Flask, request, render_template
import os

app = Flask(
    __name__,
    template_folder=os.path.join('flaskr', 'templates')  #To find folder
)

@app.route('/validate', methods=['GET', 'POST'])
def validate():
    email = ""
    phone = ""
    errors = []
    carrier = None
    email_type = None

    if request.method == 'POST':
        email = request.form.get('email')
        phone = request.form.get('phone')

        if not email or '@' not in email:
            errors.append("Invalid email address format.")

    return render_template('form.html', errors=errors, email=email, phone=phone)

if __name__ == '__main__':
    app.run(debug=True)
