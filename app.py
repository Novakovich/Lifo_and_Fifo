import json
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def home_page():
    return render_template('index.html')

#@app.route('/donate')
#def donate():
#    return 'Hello World! '

@app.route('/request/donation')
def donation():
    with open ('data.json', 'r', encoding='utf-8') as data:
        data_list = json.load(data)
        item = data_list.pop()
    return f" here {item['name']} {item['amount']} "

@app.route('/request/donation')
def page():
    return f"""<html>
        <body>
            <a href="{url_for('index')}">Return main</a>
        </body>
    </html>"""

if __name__ == '__main__':
    app.run(debug=True)
