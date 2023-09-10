from flask import Flask, render_template, request, send_file
import random
import re
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

paste_url = "https://hastebytrhacknon.trhacknon.repl.co/raw/eqomozazecuv"

def get_lines_from_paste():
    response = requests.get(paste_url)
    if response.status_code == 200:
        lines = response.text.split('\n')
        return lines
    else:
        return []

lines = get_lines_from_paste()

password_from_env = os.getenv("pass")

@app.route('/')
def random_line():
    if lines:
        random_index = random.randint(0, len(lines) - 1)
        random_entry = lines[random_index].strip()
        if "Expires at:" in random_entry:
            match = re.match(r'(.+):(.+) \| Expires at: (.+)', random_entry)
            if match:
                email, password, expiration_date = match.groups()
            else:
                email, password, expiration_date = random_entry, None, None
        else:
            match = re.match(r'(.+):(.+)', random_entry)
            if match:
                email, password = match.groups()
                expiration_date = None
            else:
                email, password, expiration_date = random_entry, None, None
        email_html = f'<span style="color: #FF5733;">E-mail:</span> {email}'
        password_html = f'<span style="color: #0000FF;">Mot de passe:</span> {password}' if password else ""
        expiration_date_html = f'<span style="color: #FFD700;">Date d\'expiration:</span> {expiration_date}' if expiration_date else ""
        return render_template('index.html', email=email_html, password=password_html, expiration_date=expiration_date_html)
    else:
        return "Aucune donnée disponible depuis la paste."

@app.route('/premium', methods=['GET', 'POST'])
def premium_access():
    if request.method == 'POST' and request.form.get('password') == password_from_env:
        random_lines = random.sample(lines, 50)
        return render_template('premium.html', random_lines=random_lines)
    else:
        return render_template('premium_login.html')

@app.route('/download')
def download_lines():
    if lines:
        file_content = "\n".join(random.sample(lines, 50))
        with open("premium_lines.txt", "w") as temp_file:
            temp_file.write(file_content)
        return send_file("premium_lines.txt", as_attachment=True, download_name="premium_lines.txt")
    else:
        return "Aucune donnée disponible pour le téléchargement."

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)